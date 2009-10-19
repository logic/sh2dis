#!/usr/bin/env python

"""
TODO:
- Output any labelled or referenced memory addresses as .equ directives.
"""


import optparse, os.path, sys
import segment, sh2, sh7052, sh7055


version='0.99'


class ROMError(StandardError):
    pass


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
    elif len(phys) == 0x80000:
        # SH/7055F
        proc = sh7055
        return (
            ('ROM', 0x0, len(phys), phys),
            ('RAM', 0xFFFF6000, 0x8000, None),
            ('REG', 0xFFFFE400, 0x1460, None),
        )
    raise ROMError, 'invalid or unrecognized ROM'


def setup_vectors(model):
    """Pre-define the vector table."""
    for i in range(0x0, 0x400, 0x4):
        if i in proc.vectors:
            label = proc.vectors[i]
        else:
            label = None
        vector = sh2.LongField(location=i, model=model, label=label)
        model.set_location(vector)
        meta = model.get_location(vector.extra)
        if meta.label is None and vector.label.startswith('v_'):
            meta.label = vector.label[2:]

    for addr, name in proc.registers.items():
        meta = model.get_location(addr)
        if meta is None:
            meta = sh2.ByteField(location=addr, model=model)
        meta.label = name
        model.set_location(meta)

    # Name a few common vector items.
    meta = model.get_location(0)
    meta = model.get_location(meta.extra)
    meta.label = 'init'
    meta = model.get_location(4)
    meta = model.get_location(meta.extra)
    if meta is not None:
        meta.label = 'sp'
    meta = model.get_location(0x10)
    meta = model.get_location(meta.extra)
    meta.label = 'reset'


def disassemble_vectors(model):
    """Disassemble the locations referenced by the vector table."""
    for i in range(0x0, 0x400, 0x4):
        if i == 0x4 or i == 0x12:
            # Skip stack point addresses.
            continue
        meta = model.get_location(i)
        sh2.disassemble(meta.extra, model)


def disassemble(phys, outfile=sys.stdout):
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
        meta = model.get_location(i)
        if code and not isinstance(meta, sh2.CodeField):
            code = False
            print >> outfile, '         !', '-' * 60
        elif not code and isinstance(meta, sh2.CodeField):
            code = True
            print >> outfile, '         !', '-' * 60
        if meta is None:
            meta = sh2.ByteField(location=i, model=model)
        countdown = meta.width - 1
        print >> outfile, '%08X %s' % (i, meta)


def main():
    parser = optparse.OptionParser(
      usage='Usage: %prog [options] <ROM file>',
      version=version)
    parser.add_option('-o', '--output', dest='file', default=None,
      help='specify a destination file (default is standard output)')
    options, args = parser.parse_args()

    if len(args) != 1:
        print >> sys.stderr, 'No ROM file specified!\n'
        parser.print_help(sys.stderr)
        sys.exit(1)

    romname = args[0]
    if not os.path.isfile(romname):
        print >> sys.stderr, 'No such ROM file `%s\'!\n' % romname
        parser.print_help(sys.stderr)
        sys.exit(1)
    phys = open(romname).read()

    if options.file is None:
        output = sys.stdout
    else:
        output = open(options.file, 'w')

    disassemble(phys, output)


if __name__ == '__main__':
    main()
