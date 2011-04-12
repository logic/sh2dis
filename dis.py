#!/usr/bin/env python

"""
TODO:
- Output any labelled or referenced memory addresses as .equ directives.
"""


from __future__ import print_function
import optparse, os.path, sys
import segment, sh2, sh7052, sh7055


version='0.99'


class ROMError(Exception):
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
    raise ROMError('invalid or unrecognized ROM')


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
        vector = kind(location=i, model=model, comment=comment)
        model.set_location(vector)
        model.set_label(i, label)
        if label is not None and label.startswith('v_'):
            model.set_label(vector.extra, label[2:])
        #meta = model.get_location(vector.extra)
        #if meta.label is None and vector.label.startswith('v_'):
        #    meta.label = vector.label[2:]

    for addr, v in list(proc.registers.items()):
        kind = sh2.LongField
        if v['size'] == 1:
            kind = sh2.ByteField
        elif v['size'] == 2:
            kind = sh2.WordField
        meta = kind(location=addr, model=model, comment=v['comment'])
        model.set_location(meta)
        model.set_label(addr, v['name'])


def disassemble_vectors(model, cb=None):
    """Disassemble the locations referenced by the vector table."""
    vectors = [ ]
    for i in range(0x0, 0x400, 0x4):
        meta = model.get_location(i)
        try:
            # Make sure this is a real address (ie. not a stack pointer)
            model.get_phys(meta.extra)
        except segment.SegmentError:
            continue
        vectors.append((meta.extra, meta.location))
    sh2.disassemble(vectors, model, cb)


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


axes = { }
def mitsu_callback(meta, registers, model):
    """Automatically generate tables and their axes, if possible."""
    # TODO: This has the potential to clobber itself. Should simply do
    # collection of axis and table locations here, for later processing,
    # and mark the location with a reference. Then, process all axes in
    # order. Then process all tables in order. 96940013 has a few tables
    # where the table (or axis) contents are referred to directly, which
    # screws us up if ordering is wrong; need to do better than "isset"
    # to determine if we can clobber existing structures. (ie. don't
    # worry about isset() on the first element of a table?)
    if meta.extra.opcode['cmd'] in sh2.register_branchers:
        r = registers[meta.extra.args['m']]

        # All axis/table lookups store the table location in R4.
        if r is not None and registers[4] is not None:

            # Axes
            if r == 0xCC6:
                tbl_loc = registers[4]
                tbl = model.get_location(tbl_loc)
                if tbl is None:
                    # Result address.
                    tbl = sh2.LongField(location=tbl_loc, model=model, comment='Result address')
                    model.set_location(tbl)

                    # Address of value to look up.
                    model.set_location(sh2.LongField(location=tbl_loc+4, model=model, comment='Lookup value address'))

                    # Length of the axis.
                    tbl_len = sh2.WordField(location=tbl_loc+8, model=model, comment='Axis length')
                    model.set_location(tbl_len)

                    # Axis data and composite structure.
                    cdata = segment.CompositeData(items_per_line=tbl_len.extra, model=model)
                    for i in range(tbl_loc+10, tbl_loc+10+(tbl_len.extra*2), 2):
                        tbl_data = sh2.WordField(location=i, member_of=cdata, model=model)
                        cdata.members.append(tbl_data)
                        model.set_location(tbl_data)

                    model.add_reference(meta.location, tbl_loc)
                    model.add_reference(tbl_loc, meta.location)
                    axes[tbl.extra] = tbl.location

            # Tables (byte- and word-width)
            elif r == 0xC28 or r == 0xE02:
                tbl_loc = registers[4]
                tbl = model.get_location(tbl_loc)

                if tbl is None:
                    # Width: sub_C28 is byte-width tables, sub_E02 is word-width.
                    tbl_width = 1 if r == 0xC28 else 2
                    tbl_type = sh2.ByteField if tbl_width == 1 else sh2.WordField

                    # Table header: 2D or 3D.
                    tbl = tbl_type(location=tbl_loc, model=model)
                    model.set_location(tbl)
                    tbl.comment = '%dD %s-width table' % (tbl.extra, 'byte' if tbl_width == 1 else 'word')

                    # Adder.
                    model.set_location(tbl_type(location=tbl_loc+tbl_width, model=model, comment='Adder'))

                    # Y-axis position.
                    yaxis = sh2.LongField(location=tbl_loc+(2*tbl_width), model=model, comment='Y-Axis')
                    yaxis_len = 0
                    if yaxis.extra in axes:
                        yaxis.comment = 'Y-Axis: 0x%X' % model.get_location(axes[yaxis.extra]).location
                        yaxis_len = model.get_location(axes[yaxis.extra]+8).extra
                    model.set_location(yaxis)

                    # X-axis?
                    tbl_pos = 4 + (tbl_width * 2)
                    xaxis_len = 1 # Always at least one row. :)
                    if tbl.extra == 3:
                        xaxis = sh2.LongField(location=tbl_loc+tbl_pos, model=model, comment='X-Axis')
                        xaxis_len = 0
                        if xaxis.extra in axes:
                            xaxis.comment = 'X-Axis: 0x%X' % model.get_location(axes[xaxis.extra]).location
                            xaxis_len = model.get_location(axes[xaxis.extra]+8).extra
                        model.set_location(xaxis)
                        tbl_pos += 4
                        model.set_location(tbl_type(location=tbl_loc+tbl_pos, model=model, comment='Row length'))
                        tbl_pos += tbl_width

                    if yaxis_len > 0:
                        cdata = segment.CompositeData(items_per_line=yaxis_len, model=model)
                        for i in range(tbl_loc+tbl_pos, tbl_loc+tbl_pos+(yaxis_len*xaxis_len*tbl_width), tbl_width):
                            if model.location_isset(i) or (tbl_width == 2 and model.location_isset(i+1)):
                                # Issue a warning about a poorly-defined table.
                                # This is a legitimate problem on some ROMs (9694, etc).
                                print('!!!!! Short table: 0x%X (at 0x%X)' % (tbl_loc, i))
                                break
                            tdata = tbl_type(location=i, model=model, member_of=cdata)
                            model.set_location(tdata)
                            cdata.members.append(tdata)


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
        model.set_location(jumper)
        model.add_reference(jumper_addr, meta.location)

        jumper_ref = jump_tbl + jumper.extra
        sh2.disassemble([(jumper_ref, jumper_addr)], model)

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
        model.set_label(mut_entry.extra, 'MUT_%X' % mut_off)
        mut_off += 1
    model.set_label(mut_loc, 'MUT_TABLE')


def mitsu_fixups(model):
    # Rename a few common vector items.
    meta = model.get_location(0)
    model.set_label(meta.extra, 'init')

    meta = model.get_location(4)
    model.set_label(meta.extra, 'sp')

    meta = model.get_location(0x10)
    model.set_label(meta.extra, 'reset')

    meta = sh2.WordField(location=0xF34, model=model)
    model.set_location(meta)

    meta = sh2.WordField(location=0xF3C, model=model)
    model.set_location(meta)

    for p in range(0xF40, 0xF5B, 2):
        meta = sh2.WordField(location=p, model=model)
        if p == 0xF44:
            model.set_label(p, 'ECU_ID1')
        elif p == 0xF54:
            model.set_label(p, 'ECU_ID2')
        model.set_location(meta)

    for p in range(0xF6A, 0xF89, 4):
        meta = sh2.LongField(location=p, model=model)
        model.set_location(meta)

    for p in range(0xF8A, 0xF8A + (16*9), 16):
        meta = sh2.WordField(location=p, model=model)
        if p == 0xFFA:
            model.set_label(p, 'periphery_IMMOB')
        else:
            model.set_label(p, 'periphery_%X' % p)
        model.set_location(meta)
        for p1 in range(p + 2, p + 16, 2):
            meta = sh2.WordField(location=p1, model=model)
            model.set_location(meta)

    meta = sh2.WordField(location=0x3FFCE, model=model)
    model.set_location(meta)
    model.set_label(meta.location, 'immobilizer')

    model.set_label(0xC28, 'tbl_lookup_byte')
    model.set_label(0xCC6, 'axis_lookup')
    model.set_label(0xE02, 'tbl_lookup_word')

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
                print(output_separator, file=outfile)
            elif not code and isinstance(meta, sh2.CodeField):
                code = True
                print(output_separator, file=outfile)
            elif code:
                rts = model.get_location(i-4) 
                if isinstance(rts, sh2.CodeField) and rts.extra.opcode['cmd'] == 'rts':
                    if isinstance(meta, sh2.CodeField):
                        print(output_separator, file=outfile)
            if meta is None:
                # Create this as a throwaway byte, to save memory.
                meta = sh2.ByteField(location=i, model=model, unknown_prefix='unk')
            countdown = meta.width - 1
            if isinstance(meta, sh2.NullField):
                print(output_separator, file=outfile)
            o = str(meta)
            if len(o):
                print(o, file=outfile)
            if isinstance(meta, sh2.NullField):
                print(output_separator, file=outfile)


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
        print('No ROM file specified!\n', file=sys.stderr)
        parser.print_help(sys.stderr)
        sys.exit(1)

    romname = args[0]
    if not os.path.isfile(romname):
        print('No such ROM file `%s\'!\n' % romname, file=sys.stderr)
        parser.print_help(sys.stderr)
        sys.exit(1)
    phys = open(romname, mode='rb').read()

    model = segment.MemoryModel(get_segments(phys))
    setup_vectors(model)
    disassemble_vectors(model, mitsu_callback if options.mitsu else None)
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
