#!/usr/bin/env python

for fn in ('501.txt','502.txt','503.txt','504.txt','505.txt','506.txt','507.txt','508.txt','509.txt'):
    with open(fn,'r') as f:
        for line in f:
            bits, cmd = line.strip().split(' ', 1)
            if ' ' in cmd:
                cmd, args = cmd.split(' ', 1)
            else:
                args = ''
            bytes = (bits[0:4], bits[4:8], bits[8:12], bits[12:16])
            inst = mask = ''
            for b in bytes:
                if b[0] in '01':
                    x = 0
                    if b[0] == '1':
                        x = x + 8
                    if b[1] == '1':
                        x = x + 4
                    if b[2] == '1':
                        x = x + 2
                    if b[3] == '1':
                        x = x + 1
                    inst = inst + hex(x)[2]
                    mask = mask + 'f'
                else:
                    inst = inst + '0'
                    mask = mask + '0'

            n = nshift = 0
            if bits[4] == 'n':
                n |= 0x0f00
                nshift = 8
            if bits[8] == 'n':
                n |= 0x00f0
                nshift = 4
                

            m = mshift = 0
            if bits[4] == 'm':
                m |= 0x0f00
                mshift = 8
            elif bits[8] == 'm':
                m |= 0x00f0
                mshift = 4

            imm = ishift = 0
            if bits[8] == 'i':
                imm |= 0x00f0
                ishift = 4
            if bits[12] == 'i':
                imm |= 0x000f
                ishift = 0

            disp = 0
            if bits[12] == 'd':
                disp |= 0x000f
                if bits[8] == 'd':
                    disp |= 0x00f0
                    if bits[4] == 'd':
                        disp |= 0x0f00

            cmd = cmd.lower()
            args = args.replace('label', 'LABEL')
            args = args.replace('disp', '0x{disp:X}')
            args = args.replace('#imm', '#0x{imm:X}')
            args = args.replace('Rm', 'R{m}')
            args = args.replace('Rn', 'R{n}')
            args = args.lower()

            print '0x%s,0x%s,0x%04x,%d,0x%04x,%d,0x%04x,%d,0x%04x,"%s","%s","%s"' % (inst, mask, m, mshift, n, nshift, imm, ishift, disp, bits, cmd.lower(), args)
