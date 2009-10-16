#!/usr/bin/env python

"""
TODO:
- Output any labelled or referenced memory addresses as .equ directives.
"""

import getopt, os.path, struct, sys
import segment, sh2, sh7052, sh7055

def get_segments(phys):
    """Determine if this is an Evo VIII (7052) or IX (7055) ROM."""
    global proc
    if len(phys) == 0x40000:
        # SH/7052F
        proc = sh7052
        return (
            ('ROM', 0x0, len(phys), phys),
            ('RAM', 0xFFFF8000, 0x3000, None),
            ('REG', 0xFFFFE400, 0x1460, None),
        )
    # SH/7055F
    proc = sh7055
    return (
        ('ROM', 0x0, len(phys), phys),
        ('RAM', 0xFFFF6000, 0x8000, None),
        ('REG', 0xFFFFE400, 0x1460, None),
    )

def setup_vectors(model):
    """Pre-define the vector table."""
    for i in range(0x0, 0x400, 0x4):
        bytes = model.get_phys(i, 4)
        value = struct.unpack('>L', bytes)[0]
        if i in proc.vectors:
            label = proc.vectors[i]
        else:
            label = None
        model.set_location(sh2.LongField(location=i, extra=value, model=model, label=label))

    for addr, name in proc.registers.items():
        value, meta = model.get_location(addr)
        if meta is None:
            meta = sh2.ByteField(location=addr, extra=0, model=model)
        meta.label = name
        model.set_location(meta)

    # Name a few common vector items.
    value,meta = model.get_location(0)
    value,meta = model.get_location(meta.extra)
    meta.label = 'init'
    value,meta = model.get_location(4)
    value,meta = model.get_location(meta.extra)
    if meta is not None:
        meta.label = 'sp'
    value,meta = model.get_location(0x10)
    value,meta = model.get_location(meta.extra)
    meta.label = 'reset'

def disassemble_vectors(model):
    """Disassemble the locations referenced by the vector table."""
    for i in range(0x0, 0x400, 0x4):
        if i == 0x4 or i == 0x12:
            # Skip stack point addresses.
            continue
        content, meta = model.get_location(i)
        sh2.disassemble(meta.extra, model)

def main(argv):
    if len(argv) != 1:
        print 'No ROM specified.'
        sys.exit(1)
    romname = argv[0]
    if not os.path.isfile(romname):
        print 'No such file:', romname
        sys.exit(1)
    phys = open(romname).read()
    model = segment.MemoryModel(get_segments(phys))
    setup_vectors(model)
    disassemble_vectors(model)

    # Output a moderately-useful disassembly.
    countdown = 0
    code = False
    for i in range(len(phys)):
        if countdown > 0:
            countdown -= 1
            continue
        value, meta = model.get_location(i)
        if code and not isinstance(meta, sh2.CodeField):
            code = False
            print '         !', '-' * 60
        elif not code and isinstance(meta, sh2.CodeField):
            code = True
            print '         !', '-' * 60
        print '%08X' % i,
        if meta is not None:
            countdown = meta.width - 1
            print meta
        else:
            print '                 .byte 0x%02X' % ord(value)

if __name__ == '__main__':
    main(sys.argv[1:])
