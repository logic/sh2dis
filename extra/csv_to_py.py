#!/usr/bin/env python

import csv, pprint

opcodes = [ ]
with open('opcodes.csv') as i:
    c = csv.reader(i)
    print 'opcodes = ('
    for row in c:
        print '    {'
        print '        "opmask": (0x{0:04X}, 0x{1:04X}),'.format(int(row[0], 16), int(row[1], 16))
        print '        "m"     : (0x{0:04X}, 0x{1:X}),'.format(int(row[2], 16), int(row[3], 16))
        print '        "n"     : (0x{0:04X}, 0x{1:X}),'.format(int(row[4], 16), int(row[5], 16))
        print '        "imm"   : (0x{0:04X}, 0x{1:X}),'.format(int(row[6], 16), int(row[7], 16))
        print '        "disp"  : 0x{0:04X},'.format(int(row[8], 16))
        print '        "bits"  : "{0}",'.format(row[9])
        print '        "cmd"   : "{0}",'.format(row[10])
        print '        "args"  : "{0}",'.format(row[11])
        print '    },'
    print ')'
