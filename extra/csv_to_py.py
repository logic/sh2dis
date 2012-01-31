#!/usr/bin/env python

from __future__ import print_function

import csv
import sys

c = csv.reader(sys.stdin)
block = """    {{
        'opmask': (0x{opcode:04X}, 0x{opmask:04X}),
        'm': (0x{m:04X}, 0x{mmask:X}),
        'n': (0x{n:04X}, 0x{nmask:X}),
        'imm': (0x{imm:04X}, 0x{immmask:X}),
        'disp': 0x{disp:04X},
        'bits': '{bits}',
        'cmd': '{cmd}',
        'args': {args},
    }},"""

opcodes = []
print("""#!/usr/bin/env python

opcodes = (""")
for row in c:
    if row[11] == '':
        args = 'None'
    elif row[12] == '':
        args = "('{0}', ),".format(row[11])
    else:
        args = "('{0}', '{1}'),".format(row[11], row[12])

    print(block.format(opcode=int(row[0], 16), opmask=int(row[1], 16),
                       m=int(row[2], 16), mmask=int(row[3], 16),
                       n=int(row[4], 16), nmask=int(row[5], 16),
                       imm=int(row[6], 16), immmask=int(row[7], 16),
                       disp=int(row[8], 16), bits=row[9], cmd=row[10],
                       args=args))
print(')')
