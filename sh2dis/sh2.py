"""SH2 disassembler"""

from __future__ import print_function
from collections import namedtuple

try:
    from Queue import Queue
except ImportError:
    from queue import Queue

import struct

from . import segment
from .sh2opcodes import OPCODES


CodeExtra = namedtuple('CodeExtra', 'text, opcode, args')


# Opcodes that use delayed branching; an legal instruction should follow.
DELAYED_BRANCHERS = ('bra', 'braf', 'jmp', 'rte', 'rts')

# Opcodes that branch based on the contents of a register.
REGISTER_BRANCHERS = ('braf', 'bsrf', 'jsr', 'jmp')

# Opcodes that branch based on a directly-referenced label.
LABEL_BRANCHERS = ('bf', 'bf/s', 'bra', 'bsr', 'bt', 'bt/s')


class DataField(segment.SegmentData):
    """Metaclass for SH2 data types."""

    def get_instruction(self, no_cmd=False):
        """Produce a GAS-compatible string representation for this type."""
        if no_cmd:
            val = '0x%%0%dX' % (self.width * 2)
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
        if 'unknown_prefix' not in kwargs:
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
            phys = self.model.get_phys(self.location, 2)
            self.extra = struct.unpack('>H', phys)[0]
        except segment.SegmentError:
            self.extra = None


class LongField(DataField):
    """Defines a "long-word" of four bytes."""

    def __init__(self, *args, **kwargs):
        kwargs['width'] = 4
        kwargs['unknown_prefix'] = 'long'
        DataField.__init__(self, *args, **kwargs)
        try:
            phys = self.model.get_phys(self.location, 4)
            self.extra = struct.unpack('>L', phys)[0]
        except segment.SegmentError:
            self.extra = None

        # Make us a reference if we refer to a legitimate address.
        if self.extra is not None:
            try:
                self.model.add_reference(self.extra, self.location)
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
            tgt = self.extra.args['target']
            label = self.model.get_label(tgt)
            if label is None:
                label = '0x%X' % tgt
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
                        if isinstance(meta, (WordField, ByteField)):
                            comments.append('[%s] = 0x%X' % (label,
                                                             meta.extra))
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
    """No matching instruction was found"""
    pass


def parse_args(instruction, opcode):
    """Given an instruction and an opcode, return a dict representing them."""
    realop = {}
    if opcode['m'][0] != 0:
        realop['m'] = (instruction & opcode['m'][0]) >> opcode['m'][1]
    else:
        realop['m'] = None
    if opcode['n'][0] != 0:
        realop['n'] = (instruction & opcode['n'][0]) >> opcode['n'][1]
    else:
        realop['n'] = None
    if opcode['imm'][0] != 0:
        realop['imm'] = (instruction & opcode['imm'][0]) >> opcode['imm'][1]
    else:
        realop['imm'] = None
    if opcode['disp'] != 0:
        realop['disp'] = instruction & opcode['disp']
    else:
        realop['disp'] = None
    return realop


def calculate_disp_target(opcode, args, progc):
    """Calculate the target of an opcode, given it's args and PC."""
    disp = args['disp']
    if disp is not None:
        # 12-bit disp values are signed.
        # sign = 0x800 if opcode['disp'] & 0xF00 != 0 else 0
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
            target += (progc & 0xFFFFFFFC) + 4
        else:
            target += progc + 4

        args['target'] = target
        args['disp'] *= disp_mult
    else:
        args['target'] = disp


def track_registers(opcode, args, location, registers, model):
    """Track register assignments."""
    nval = args['n']
    if nval is None:
        if opcode['args'][1] == 'r0':
            nval = 0
    if nval is not None:
        if opcode['cmd'].startswith('mov'):
            mval = args['m']
            if mval is None:
                if opcode['args'][0] == 'r0':
                    mval = 0
            if mval is None:
                if args['imm'] is not None:
                    registers[nval] = args['imm']
                    return
                if args['disp'] is not None:
                    target = args['target']
                    meta = model.get_location(target)
                    if meta is None:
                        if (opcode['cmd'].endswith('.l') or
                                opcode['args'][1].startswith('@(')):
                            meta = LongField(location=target, model=model)
                            model.set_location(meta)
                        elif opcode['cmd'][-2:] == '.w':
                            meta = WordField(location=target, model=model)
                            model.set_location(meta)
                        else:
                            meta = ByteField(location=target, model=model)
                            model.set_location(meta)
                    model.add_reference(target, location)
                    registers[nval] = meta.extra
                    # registers[nval] = meta.extra if meta is not None else model.get_phys(target)
                    return

        # Any action on a target register that we can't explicitly
        # calculate invalidates any current value. Register estimation
        # is a best-effort kind of thing.
        registers[nval] = None


def lookup_instruction(instruction):
    """Perform a basic lookup of the instruction in our registry."""
    # TODO: brute force sucks, we can do much better here.
    for opcode in OPCODES:
        instbits, instmask = opcode['opmask']
        if instruction & instmask == instbits:
            args = parse_args(instruction, opcode)
            return opcode, args
    raise AssemblyError('no matching instruction for %#x' % instruction)


def disasm_single(instruction, progc, registers, model):
    """Disassemble a single instruction."""
    opcode, args = lookup_instruction(instruction)
    calculate_disp_target(opcode, args, progc)
    track_registers(opcode, args, progc, registers, model)
    instr = [opcode['cmd'], ]
    if opcode['args'][0] != '':
        aval = opcode['args'][0]
        if opcode['args'][1] != '':
            aval = aval + ', ' + opcode['args'][1]
        aval = aval % args
        instr += [aval, ]
    extra = CodeExtra(' '.join(instr), opcode, args)
    return CodeField(location=progc, width=2, extra=extra, model=model)


def disassemble(locations, model, callback=None):
    """Given a memory model and a set of locations within it, disassemble."""
    work_queue = Queue()
    for location, reference in locations:
        work_queue.put((location, reference), False)

    while not work_queue.empty():
        location, reference = work_queue.get()

        # Quick check to make sure we haven't already processed this location.
        try:
            meta = model.get_location(location)
        except segment.SegmentError as segerr:
            print('Unable to retrieve location 0x%x, giving up on that path' % location)
            print('Error was: %s' % segerr)
            continue
        if isinstance(meta, CodeField):
            model.add_reference(meta.location, reference)
            continue

        registers = [None, ] * 16
        branching = False
        branch_countdown = 0

        while not branching or branch_countdown >= 0:
            try:
                model.get_location(location)
                phys = model.get_phys(location, 2)
            except segment.SegmentError:
                break

            instruction = struct.unpack('>H', phys)[0]
            try:
                code = disasm_single(instruction, location, registers, model)
            except AssemblyError as assemerr:
                print('Unable to disassemble location 0x%x, giving up on that path' % location)
                print('Error was: %s' % assemerr)
                break
            model.set_location(code)

            # Handle register-based branches.
            if code.extra.opcode['cmd'] in REGISTER_BRANCHERS:
                reg = registers[code.extra.args['m']]
                if reg is not None:
                    code.extra.args['target'] = reg
                    work_queue.put((reg, location), False)

            elif code.extra.opcode['cmd'] in LABEL_BRANCHERS:
                work_queue.put((code.extra.args['target'], location), False)

            if reference is not None:
                model.add_reference(code.location, reference)
                reference = None

            if callback is not None:
                callback(code, registers, model)

            if code.extra.opcode['cmd'] in DELAYED_BRANCHERS:
                branch_countdown = 1
                branching = True
            if branching:
                branch_countdown -= 1

            location += 2


if __name__ == '__main__':
    print('no tests yet')
