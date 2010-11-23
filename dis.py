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
            ('RAM', 0xFFFF8000, 0xFFFFB000, None),
            ('REG', 0xFFFFE400, 0xFFFFF860, None),
        )
    elif len(phys) == 0x80000:
        # SH/7055F
        proc = sh7055
        return (
            ('ROM', 0x0, len(phys), phys),
            ('RAM', 0xFFFF6000, 0xFFFFE000, None),
            ('REG', 0xFFFFE400, 0xFFFFF860, None),
        )
    raise ROMError, 'invalid or unrecognized ROM'


def setup_vectors(model):
    """Pre-define the vector table."""
    for i in range(0x0, 0x400, 0x4):
        label = None
        comment = None
        kind = sh2.LongField
        if i in proc.vectors:
            v = proc.vectors[i]
            label = v['name']
            comment = v['comment']
            if v['size'] == 1:
                kind = sh2.ByteField
            elif v['size'] == 2:
                kind = sh2.WordField
        vector = kind(location=i, model=model, label=label, comment=comment)
        model.set_location(vector)
        meta = model.get_location(vector.extra)
        if meta.label is None and vector.label.startswith('v_'):
            meta.label = vector.label[2:]

    for addr, v in proc.registers.items():
        kind = sh2.LongField
        if v['size'] == 1:
            kind = sh2.ByteField
        elif v['size'] == 2:
            kind = sh2.WordField
        meta = kind(location=addr, model=model, label=v['name'], comment=v['comment'])
        model.set_location(meta)


def disassemble_vectors(model):
    """Disassemble the locations referenced by the vector table."""
    for i in range(0x0, 0x400, 0x4):
        if i == 0x4 or i == 0x12:
            # Skip stack pointer addresses.
            continue
        meta = model.get_location(i)
        sh2.disassemble(meta.extra, meta.location, model)

def scan_free_space(model):
    """Scan for contiguous blocks of 0xFF, replace with NullField."""
    for start, end in model.get_phys_ranges():
        countdown = 0
        ff_seen = 0
        for i in range(start, end):
            if countdown > 0:
                countdown -= 1
                continue
            meta = model.get_location(i)
            if meta is None and model.get_phys(i, 1) == chr(0xFF):
                ff_seen += 1
            else:
                if ff_seen > 0x1FF:
                    null = sh2.NullField(location=i-ff_seen, width=ff_seen, model=model)
                    model.set_location(null)
                ff_seen = 0
                if meta is not None:
                    countdown = meta.width - 1

def mitsu_fixup_mova(meta, model):
    # Mitsu seems to love MOVA for jump tables.
    jump_tbl = meta.extra.args['target']
    jump_off = 0
    while True:
        jumper_addr = jump_tbl + jump_off
        jumper = model.get_location(jumper_addr)
        if isinstance(jumper, sh2.CodeField):
            break

        jumper = sh2.WordField(location=jumper_addr, model=model)
        jumper.references[meta.location] = 1
        model.set_location(jumper)

        jumper_ref = jump_tbl + jumper.extra
        sh2.disassemble(jumper_ref, jumper_addr, model)

        jumper.comment = 'jsr %s' % model.get_label(jumper_ref)
        jump_off += 2


def mitsu_fixup_mut(meta, model):
    mut_loc = model.get_location(meta.extra.args['target']).extra
    mut_off = 0
    while True:
        mut_entry = sh2.LongField(location=(mut_loc+(mut_off<<2)), model=model)
        if mut_entry.extra == 0xFFFFFFFF:
            break
        model.set_location(mut_entry)
        mut_target = model.get_location(mut_entry.extra)
        mut_target.label = 'MUT_%X' % mut_off
        mut_off += 1
    mut_entry = model.get_location(mut_loc)
    mut_entry.label = 'MUT_TABLE'


def mitsu_fixups(model):
    # Rename a few common vector items.
    meta = model.get_location(0)
    meta = model.get_location(meta.extra)
    meta.label = 'init'

    meta = model.get_location(4)
    meta = model.get_location(meta.extra)
    meta.label = 'sp'

    meta = model.get_location(0x10)
    meta = model.get_location(meta.extra)
    meta.label = 'reset'

    meta = sh2.WordField(location=0xF34, model=model)
    model.set_location(meta)

    meta = sh2.WordField(location=0xF3C, model=model)
    model.set_location(meta)

    for p in range(0xF40, 0xF5B, 2):
        meta = sh2.WordField(location=p, model=model)
        if p == 0xF44:
            meta.label = 'ECU_ID1'
        elif p == 0xF54:
            meta.label = 'ECU_ID2'
        model.set_location(meta)

    for p in range(0xF6A, 0xF89, 4):
        meta = sh2.LongField(location=p, model=model)
        model.set_location(meta)

    for p in range(0xF8A, 0xF8A + (16*9), 16):
        meta = sh2.WordField(location=p, model=model)
        if p == 0xFFA:
            meta.label = 'periphery_IMMOB'
        else:
            meta.label = 'periphery_%X' % p
        model.set_location(meta)
        for p1 in range(p + 2, p + 16, 2):
            meta = sh2.WordField(location=p1, model=model)
            model.set_location(meta)

    meta = sh2.WordField(location=0x3FFCE, model=model, label='immobilizer')
    model.set_location(meta)

    # Temporary hack to see if tables work.
    members = []
    for p in range(0x33bd, 0x34cb):
        meta = sh2.ByteField(location=p, model=model)
        model.set_location(meta)
        members.append(meta)
    members[0].label = 'HiOctFuel'
    tbl = segment.CompositeData(members=members, items_per_line=15, model=model)
    for meta in members:
        meta.member_of = tbl
    # End temporary hack.

    for start, end in model.get_phys_ranges():
        countdown = 0
        movw_found = shll2_found = mut_found = False
        for i in range(start, end):
            if countdown > 0:
                countdown -= 1
                continue
            meta = model.get_location(i)
            if isinstance(meta, sh2.CodeField):
                if meta.extra.opcode['cmd'] == 'mova':
                    mitsu_fixup_mova(meta, model)

                elif not mut_found:
                    if not movw_found and meta.extra.opcode['cmd'] == 'mov.w':
                        if meta.extra.args['target'] is not None:
                            target = model.get_location(meta.extra.args['target'])
                            if target is not None and target.extra == 0xBF:
                                movw_found = True
                    elif movw_found and meta.extra.opcode['cmd'] == 'shll2':
                        if shll2_found:
                            movw_found = shll2_found = False
                        else:
                            shll2_found = True
                    elif movw_found and shll2_found:
                        if meta.extra.opcode['cmd'] == 'mov.l':
                            if meta.extra.args['target'] is not None:
                                mitsu_fixup_mut(meta, model)
                                mut_found = True
                        movw_found = shll2_found = False
            if meta is not None:
                countdown = meta.width - 1


output_separator = '         ! ' + '-' * 60
def final_output(model, outfile=sys.stdout, output_ram=False):
    # Output a moderately-useful disassembly.
    countdown = 0
    code = False
    ranges = [ ]
    if output_ram:
        for segment in model.segments:
             ranges.append((segment.start, segment.end))
    else:
        ranges = model.get_phys_ranges()
    for start, end in ranges:
        for i in range(start, end):
            if countdown > 0:
                countdown -= 1
                continue
            meta = model.get_location(i)
            if code and not isinstance(meta, sh2.CodeField):
                code = False
                print >> outfile, output_separator
            elif not code and isinstance(meta, sh2.CodeField):
                code = True
                print >> outfile, output_separator
            if meta is None:
                # Create this as a throwaway byte, to save memory.
                meta = sh2.ByteField(location=i, model=model, unknown_prefix='unk')
            countdown = meta.width - 1
            if isinstance(meta, sh2.NullField):
                print >> outfile, output_separator
            o = str(meta)
            if len(o):
                print >> outfile, meta
            if isinstance(meta, sh2.NullField):
                print >> outfile, output_separator


def main():
    parser = optparse.OptionParser(
      usage='Usage: %prog [options] <ROM file>',
      version=version)
    parser.add_option('-o', '--output', dest='file', default=None,
      help='specify a destination file (default is standard output)')
    parser.add_option('-m', '--mitsu', action='store_true', dest='mitsu',
      help='perform fixups specific to Mitsubishi ECUs')
    parser.add_option('-r', '--ram', action='store_true', dest='output_ram',
      help='include RAM addresses in output')
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
    phys = open(romname, mode='rb').read()

    model = segment.MemoryModel(get_segments(phys))
    setup_vectors(model)
    disassemble_vectors(model)
    if options.mitsu:
        mitsu_fixups(model)
    scan_free_space(model)

    if options.file is None:
        output = sys.stdout
    else:
        output = open(options.file, 'w')
    final_output(model, output, options.output_ram)


if __name__ == '__main__':
    main()
