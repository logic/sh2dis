#!/usr/bin/env python


"""
TODO:
- Byte, Long, and Word fields should do their own data conversion, rather
  than the caller doing the struct work.
- fix reference bug in disassemble()
- make some sort of note with the code about both resolved and unresolved
  branch targets.
- DataField.get_label() should be smart enough to infer the common idiom
  "label+1".
"""


import csv, segment, struct
from sh2opcodes import opcodes


# Opcodes that use delayed branching; an legal instruction should follow.
delayed_branchers = ('bra','braf','jmp','rte','rts')

# Opcodes that branch based on the contents of a register.
register_branchers = ('braf','bsrf','jsr','jmp')

# Opcodes that branch based on a directly-referenced label.
label_branchers = ('bf','bf/s','bra','bsr','bt','bt/s')


class DataField(segment.SegmentData):
    """Metaclass for SH2 data types."""

    def __str__(self):
        """A GAS-compatible string representation for this data type."""
        name = self.__class__.__name__.lower().replace('field', '')
        return '{0:16} .{1} 0x{2:0{3}x}'.format(self.get_label(), name, self.extra, self.width)

    def get_label(self):
        if self.label is None and len(self.references) > 0:
            return 'unk_{0:X}:'.format(self.location)
        if self.label is not None:
            return self.label + ':'
        return ''


class ByteField(DataField):
    """Defines a single byte."""

    def __init__(self, *args, **kwargs):
        kwargs['width'] = 1
        DataField.__init__(self, *args, **kwargs)


class WordField(DataField):
    """Defines a "word" of two bytes."""

    def __init__(self, *args, **kwargs):
        kwargs['width'] = 2
        DataField.__init__(self, *args, **kwargs)


class LongField(DataField):
    """Defines a "long-word" of four bytes."""

    def __init__(self, *args, **kwargs):
        kwargs['width'] = 4
        DataField.__init__(self, *args, **kwargs)

        # Make us a reference if we refer to a legitimate address.
        try:
            value, meta = self.model.get_location(self.extra)
            if meta is None:
                self.model.set_location(ByteField(location=self.extra,extra=ord(value),model=self.model))
                value, meta = self.model.get_location(self.extra)
                meta.references.append(self.location)
        except segment.SegmentError:
            pass

    def __str__(self):
        name = self.__class__.__name__.lower().replace('field', '')
        try:
            value, meta = self.model.get_location(self.extra)
            if meta is not None:
                if meta.get_label() != '':
                    value = meta.get_label()[:-1]
                else:
                    value = '0x{0:0{1}x}'.format(self.extra, self.width)
            else:
                value = '0x{0:0{1}x}'.format(self.extra, self.width)
        except segment.SegmentError:
            value = '0x{0:0{1}x}'.format(self.extra, self.width)
        return '{0:16} .{1} {2}'.format(self.get_label(), name, value)


class CodeField(DataField):
    """Defines a single assembly instruction."""

    def __init__(self, *args, **kwargs):
        DataField.__init__(self, *args, **kwargs)

    def __str__(self):
        if 'label' in self.extra['text']:
            value, meta = self.model.get_location(self.extra['args']['target'])
            if meta is not None:
                target = meta.get_label()
            else:
                target = 'sub_{0:X}'.format(self.extra['args']['target'])
            text = self.extra['text'].replace('label', target)
        else:
            text = self.extra['text']
        label = self.label + ':' if self.label is not None else ''
        return '{0:16} {1}'.format(self.get_label(), text)

    def get_label(self):
        if self.label is None and len(self.references) > 0:
            return 'sub_{0:X}:'.format(self.location)
        if self.label is not None:
            return self.label + ':'
        return ''


class NullField(segment.SegmentData):
    """Defines a section of unused space."""

    def __init__(self, *args, **kwargs):
        segment.SegmentData.__init__(self, *args, **kwargs)

    def __str__(self):
        return '.org 0x{0:8x}'.format(self.location + self.width)


class AssemblyError(StandardError):
    pass


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


def disasm_single(instruction):
    """Disassemble a single instruction."""
    # TODO: brute force sucks, we can do much better here.
    for opcode in opcodes:
        instbits, instmask = opcode['opmask']
        if instruction & instmask == instbits:
            args = parse_args(instruction, opcode)
            return opcode, args

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
        if opcode['cmd'][-2:] == '.b':
            disp_mult = 1
        elif opcode['cmd'][-2:] == '.l' or opcode['cmd'] == 'mova':
            disp_mult = 4
        else:
            disp_mult = 2

        if disp & sign != 0 and opcode['cmd'][0:3] != 'mov':
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
    if n is not None:
        if opcode['cmd'][:3] == 'mov':
            if args['m'] is None:
                if args['imm'] is not None:
                    registers[n] = args['imm']
                    return
                if args['disp'] is not None:
                    target = args['target']
                    val, meta = model.get_location(target)
                    # TODO: BUG! If the location is set to a word,
                    # but we're only grabbing a byte here, we'll
                    # get the wrong value in the register!
                    if meta is None:
                        if opcode['cmd'][-2:] == '.l' or opcode['cmd'] == 'mova':
                            val = LongField(location=target,model=model)
                            model.set_location(val)
                            val, meta = model.get_location(target)
                            meta.extra = struct.unpack('>L', val)[0]
                        elif opcode['cmd'][-2:] == '.w':
                            val = WordField(location=target,model=model)
                            model.set_location(val)
                            val, meta = model.get_location(target)
                            meta.extra = struct.unpack('>H', val)[0]
                        else:
                            val = ByteField(location=target,model=model)
                            model.set_location(val)
                            val, meta = model.get_location(target)
                            meta.extra = struct.unpack('>B', val)[0]
                    if location not in meta.references:
                        meta.references.append(location)
                    registers[n] = meta.extra
                    return

        # Any action on a target register that we can't explicitly
        # calculate invalidates any current value. Register estimation
        # is a best-effort kind of thing.
        registers[n] = None
    elif opcode['args'][-3:] == ',r0':
        registers[0] = None


def disassemble(location, model):
    """Given a memory model and a location within it, disassemble."""
    work_queue = [(location,None),]

    while len(work_queue) > 0:
        location, reference = work_queue.pop()
        registers = [None,] * 16
        branching = False
        branch_countdown = 0

        # Quick check to make sure we haven't already processed this location.
        value, meta = model.get_location(location)
        if isinstance(meta, CodeField):
            continue

        while not branching or branch_countdown >= 0:
            try:
                bytes, orig = model.get_location(location)
                bytes = model.get_phys(location, 2)
            except segment.SegmentError:
                break

            instruction = struct.unpack('>H', bytes)[0]
            opcode, args = disasm_single(instruction)
            calculate_disp_target(opcode, args, location)
            track_registers(opcode, args, location, registers, model)

            # Handle register-based branches.
            if opcode['cmd'] in register_branchers:
                if registers[args['m']] is not None:
                    work_queue.append((registers[args['m']], location))
                # TODO: Make some kind of note about unresolved branches.
                #else:
                #    print 'unresolved branch at 0x{0:x}'.format(location)
            if opcode['cmd'] in label_branchers:
                work_queue.append((args['target'], location))

            extra = {
                'text': ' '.join((opcode['cmd'], opcode['args'].format(**args))),
                'opcode': opcode,
                'args': args,
            }
            code = CodeField(location=location, width=2, extra=extra, model=model)
            if reference is not None:
                code.references.append(reference)
                reference = None
            if orig is not None:
                code.label = orig.label
            model.set_location(code)

            if opcode['cmd'] in delayed_branchers:
                branch_countdown = 1
                branching = True
                if args['target'] is not None:
                    work_queue.append((args['target'], location))
            if branching:
                branch_countdown -= 1

            location += 2

if __name__ == '__main__':
    print 'no tests yet'
