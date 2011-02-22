#!/usr/bin/env python


from __future__ import print_function


import csv, segment, struct, string
from sh2opcodes import opcodes
from collections import namedtuple


CodeExtra = namedtuple('CodeExtra', 'text, opcode, args')


# Opcodes that use delayed branching; an legal instruction should follow.
delayed_branchers = ('bra','braf','jmp','rte','rts')

# Opcodes that branch based on the contents of a register.
register_branchers = ('braf','bsrf','jsr','jmp')

# Opcodes that branch based on a directly-referenced label.
label_branchers = ('bf','bf/s','bra','bsr','bt','bt/s')


class DataField(segment.SegmentData):
    """Metaclass for SH2 data types."""

    def get_instruction(self, no_cmd=False):
        """A GAS-compatible string representation for this data type."""
        if no_cmd:
            val = '0x%%0%dX' % (self.width*2)
        else:
            name = self.__class__.__name__.lower().replace('field', '')
            val = '.%s 0x%%0%dX' % (name, (self.width * 2))
        if self.extra is None:
            self.extra = 0
        return val % self.extra


class ByteField(DataField):
    """Defines a single byte."""

    def __init__(self, *args, **kwargs):
        kwargs['width'] = 1
        if not 'unknown_prefix' in kwargs:
            kwargs['unknown_prefix'] = 'byte'
        DataField.__init__(self, *args, **kwargs)
        try:
            self.extra = ord(self.model.get_phys(self.location, 1))
        except segment.SegmentError:
            self.extra = None

    def generate_comments(self):
        comments = DataField.generate_comments(self)
        if chr(self.extra).isalnum():
            comments.append('\'%c\'' % self.extra)
        return comments


class WordField(DataField):
    """Defines a "word" of two bytes."""

    def __init__(self, *args, **kwargs):
        kwargs['width'] = 2
        kwargs['unknown_prefix'] = 'word'
        DataField.__init__(self, *args, **kwargs)
        try:
            bytes = self.model.get_phys(self.location, 2)
            self.extra = struct.unpack('>H', bytes)[0]
        except segment.SegmentError:
            self.extra = None


class LongField(DataField):
    """Defines a "long-word" of four bytes."""

    def __init__(self, *args, **kwargs):
        kwargs['width'] = 4
        kwargs['unknown_prefix'] = 'long'
        DataField.__init__(self, *args, **kwargs)
        try:
            bytes = self.model.get_phys(self.location, 4)
            self.extra = struct.unpack('>L', bytes)[0]
        except segment.SegmentError:
            self.extra = None

        # Make us a reference if we refer to a legitimate address.
        if self.extra is not None:
            try:
                if self.model.get_location(self.extra) is None:
                    create_reference(referer=self.location, location=self.extra, model=self.model)
            except segment.SegmentError:
                pass

    def get_instruction(self, no_cmd=False):
        name = self.__class__.__name__.lower().replace('field', '')
        if self.extra is None:
            return '.%s 0x00000000' % name
        try:
            text = self.model.get_label(self.extra)
        except segment.SegmentError:
            text = None
        if text is None:
            text = '0x%%0%dX' % (self.width * 2)
            text = text % self.extra
        if no_cmd:
            return text
        return '.%s %s' % (name, text)


class CodeField(DataField):
    """Defines a single assembly instruction."""

    def __init__(self, *args, **kwargs):
        kwargs['unknown_prefix'] = 'sub'
        DataField.__init__(self, *args, **kwargs)

    def get_instruction(self, no_cmd=False):
        if 'label' in self.extra.text and not no_cmd:
            t = self.extra.args['target']
            label = self.model.get_label(t)
            if label is None:
                label = '0x%X' % t
            return self.extra.text.replace('label', label)
        return self.extra.text

    def generate_comments(self):
        comments = DataField.generate_comments(self)
        if 'target' in self.extra.args:
            target = self.extra.args['target']
            if target is not None:
                label = self.model.get_label(target)
                if label is not None:
                    meta = self.model.get_location(target)
                    if isinstance(meta, LongField):
                        try:
                            t2label = self.model.get_label(meta.extra)
                        except segment.SegmentError:
                            t2label = None
                        if t2label is None:
                            t2label = '0x%X' % meta.extra
                        comments.append('[%s] = %s' % (label, t2label))
                    elif 'label' not in self.extra.text:
                        if isinstance(meta, WordField) or isinstance(meta, ByteField):
                            comments.append('[%s] = 0x%X' % (label, meta.extra))
                        else:
                            comments.append(label)
        return comments


class NullField(segment.SegmentData):
    """Defines a section of unused space."""

    def __init__(self, *args, **kwargs):
        segment.SegmentData.__init__(self, *args, **kwargs)

    def get_instruction(self, no_cmd=False):
        return '.org 0x%X' % (self.location + self.width)

    def generate_comments(self):
        comments = segment.SegmentData.generate_comments(self)
        comments.append('%d bytes of free space' % self.width)
        return comments


class AssemblyError(Exception):
    pass


def create_reference(referer, location, model, metatype=ByteField, known_reference=False):
    meta = model.get_location(location)
    if meta is None:
        if known_reference:
            meta = metatype(location=location, model=model)
        else:
            meta = metatype(location=location, model=model, unknown_prefix='unk')
        model.set_location(meta)
    if referer is not None:
        meta.references[referer] = 1
    return meta


def parse_args(instruction, opcode):
    op = { }
    if opcode['m'][0] != 0:
        op['m'] = (instruction & opcode['m'][0]) >> opcode['m'][1]
    else:
        op['m'] = None
    if opcode['n'][0] != 0:
        op['n'] = (instruction & opcode['n'][0]) >> opcode['n'][1]
    else:
        op['n'] = None
    if opcode['imm'][0] != 0:
        op['imm'] = (instruction & opcode['imm'][0]) >> opcode['imm'][1]
    else:
        op['imm'] = None
    if opcode['disp'] != 0:
        op['disp'] = instruction & opcode['disp']
    else:
        op['disp'] = None
    return op


def calculate_disp_target(opcode, args, pc):
    disp = args['disp']
    if disp is not None:
        # 12-bit disp values are signed.
        #sign = 0x800 if opcode['disp'] & 0xF00 != 0 else 0
        sign = 0
        if opcode['disp'] & 0xF00 != 0:
            sign = 0x800
        elif opcode['disp'] & 0xF0 != 0:
            sign = 0x80
        elif opcode['disp'] & 0xF != 0:
            sign = 0x8
        else:
            sign = 0

        # 1-, 2-, or 4-byte multiplier determination.
        if opcode['cmd'].endswith('.b'):
            disp_mult = 1
        elif opcode['cmd'].endswith('.l') or opcode['cmd'] == 'mova':
            disp_mult = 4
        else:
            disp_mult = 2

        if disp & sign != 0 and not opcode['cmd'].startswith('mov'):
            target = -((sign << 1) - ((disp - sign) * disp_mult))
        else:
            target = disp * disp_mult

        # Long disp values require a PC alignment mask.
        if disp_mult == 4:
            target += (pc & 0xFFFFFFFC) + 4
        else:
            target += pc + 4

        args['target'] = target
        args['disp'] *= disp_mult
    else:
        args['target'] = disp


def track_registers(opcode, args, location, registers, model):
    """Track register assignments."""
    n = args['n']
    if n is None:
        if opcode['args'][1] == 'r0':
            n = 0
    if n is not None:
        if opcode['cmd'].startswith('mov'):
            m = args['m']
            if m is None:
                if opcode['args'][0] == 'r0':
                    m = 0
            if m is None:
                if args['imm'] is not None:
                    registers[n] = args['imm']
                    return
                if args['disp'] is not None:
                    target = args['target']
                    meta = model.get_location(target)
                    if meta is None:
                        if opcode['cmd'].endswith('.l') or opcode['args'][1].startswith('@('):
                            meta_type = LongField
                        elif opcode['cmd'][-2:] == '.w':
                            meta_type = WordField
                        else:
                            meta_type = ByteField
                        meta = create_reference(referer=location, location=target, model=model, metatype=meta_type, known_reference=True)
                    registers[n] = meta.extra
                    return

        # Any action on a target register that we can't explicitly
        # calculate invalidates any current value. Register estimation
        # is a best-effort kind of thing.
        registers[n] = None


def lookup_instruction(instruction):
    """Perform a basic lookup of the instruction in our registry."""
    # TODO: brute force sucks, we can do much better here.
    for opcode in opcodes:
        instbits, instmask = opcode['opmask']
        if instruction & instmask == instbits:
            args = parse_args(instruction, opcode)
            return opcode, args
    raise AssemblyError('no matching instruction for %#x' % instruction)


def disasm_single(instruction, pc, registers, model):
    """Disassemble a single instruction."""
    opcode, args = lookup_instruction(instruction)
    calculate_disp_target(opcode, args, pc)
    track_registers(opcode, args, pc, registers, model)
    a = opcode['args'][0]
    if opcode['args'][1] != '':
        a = a + ', ' + opcode['args'][1]
    extra = CodeExtra(' '.join((opcode['cmd'], a % args)), opcode, args)
    return CodeField(location=pc, width=2, extra=extra, model=model)


def disassemble(location, reference, model, callback=None):
    """Given a memory model and a location within it, disassemble."""
    work_queue = [ (location, reference), ]

    while len(work_queue) > 0:
        location, reference = work_queue.pop()
        registers = [None,] * 16
        branching = False
        branch_countdown = 0

        # Quick check to make sure we haven't already processed this location.
        meta = model.get_location(location)
        if isinstance(meta, CodeField):
            meta.references[reference] = 1
            continue

        while not branching or branch_countdown >= 0:
            try:
                orig = model.get_location(location)
                bytes = model.get_phys(location, 2)
            except segment.SegmentError:
                break

            instruction = struct.unpack('>H', bytes)[0]
            code = disasm_single(instruction, location, registers, model)

            # Handle register-based branches.
            if code.extra.opcode['cmd'] in register_branchers:
                r = registers[code.extra.args['m']]
                if r is not None:
                    code.extra.args['target'] = r
                    work_queue.append((r, location))

            elif code.extra.opcode['cmd'] in label_branchers:
                work_queue.append((code.extra.args['target'], location))

            if reference is not None:
                code.references[reference] = 1
                reference = None
            if orig is not None:
                code.label = orig.label

            model.set_location(code)

            if callback is not None:
                callback(code, registers, model)

            if code.extra.opcode['cmd'] in delayed_branchers:
                branch_countdown = 1
                branching = True
            if branching:
                branch_countdown -= 1

            location += 2

if __name__ == '__main__':
    print('no tests yet')
