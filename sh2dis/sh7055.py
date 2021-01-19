# pylint: disable=too-many-lines
"""SH7055 storage layout."""

VECTORS = {
    0x00000000: {
        'name': 'v_power_on_pc',
        'size': 4,
        'comment': 'Power-on reset (PC)',
    },
    0x00000004: {
        'name': 'v_power_on_sp',
        'size': 4,
        'comment': 'Power-on reset (SP)',
    },
    0x00000008: {
        'name': 'v_reset_pc',
        'size': 4,
        'comment': 'Manual reset (PC)',
    },
    0x0000000C: {
        'name': 'v_reset_sp',
        'size': 4,
        'comment': 'Manual reset (SP)',
    },
    0x00000010: {
        'name': 'v_gen_ill_inst',
        'size': 4,
        'comment': 'General illegal instruction',
    },
    0x00000018: {
        'name': 'v_slot_ill_inst',
        'size': 4,
        'comment': 'Slot illegal instruction',
    },
    0x00000024: {
        'name': 'v_cpu_addr_err',
        'size': 4,
        'comment': 'CPU address error',
    },
    0x00000028: {
        'name': 'v_dmac_addr_err',
        'size': 4,
        'comment': 'DMAC address error',
    },
    0x0000002C: {
        'name': 'v_int_nmi',
        'size': 4,
        'comment': 'NMI interrupt',
    },
    0x00000030: {
        'name': 'v_int_ubc',
        'size': 4,
        'comment': 'User break interrupt',
    },
    0x00000034: {
        'name': 'v_fpu_exception',
        'size': 4,
        'comment': 'FPU Exception',
    },
    0x00000038: {
        'name': 'v_h_udi',
        'size': 4,
        'comment': 'H-UDI',
    },
    0x00000100: {
        'name': 'v_int_irq0',
        'size': 4,
        'comment': 'IRQ0 interrupt',
    },
    0x00000104: {
        'name': 'v_int_irq1',
        'size': 4,
        'comment': 'IRQ1 interrupt',
    },
    0x00000108: {
        'name': 'v_int_irq2',
        'size': 4,
        'comment': 'IRQ2 interrupt',
    },
    0x0000010C: {
        'name': 'v_int_irq3',
        'size': 4,
        'comment': 'IRQ3 interrupt',
    },
    0x00000110: {
        'name': 'v_int_irq4',
        'size': 4,
        'comment': 'IRC4 interrupt',
    },
    0x00000114: {
        'name': 'v_int_irq5',
        'size': 4,
        'comment': 'IRC5 interrupt',
    },
    0x00000118: {
        'name': 'v_int_irq6',
        'size': 4,
        'comment': 'IRC6 interrupt',
    },
    0x0000011C: {
        'name': 'v_int_irq7',
        'size': 4,
        'comment': 'IRC7 interrupt',
    },
    0x00000120: {
        'name': 'v_dmac0_dei0',
        'size': 4,
        'comment': 'Direct memory access controller 0 interrupt',
    },
    0x00000128: {
        'name': 'v_dmac1_dei1',
        'size': 4,
        'comment': 'Direct memory access controller 1 interrupt',
    },
    0x00000130: {
        'name': 'v_dmac2_dei2',
        'size': 4,
        'comment': 'Direct memory access controller 2 interrupt',
    },
    0x00000138: {
        'name': 'v_dmac3_dei3',
        'size': 4,
        'comment': 'Direct memory access controller 3 interrupt',
    },
    0x00000140: {
        'name': 'v_atu01_itv',
        'size': 4,
        'comment': 'Advanced timer unit channel 0 interval interrupt',
    },
    0x00000150: {
        'name': 'v_atu02_ici0A',
        'size': 4,
        'comment': 'Advanced timer unit channel 0 input capture interrupt A',
    },
    0x00000158: {
        'name': 'v_atu02_ici0B',
        'size': 4,
        'comment': 'Advanced timer unit channel 0 input capture interrupt B',
    },
    0x00000160: {
        'name': 'v_atu03_ici0C',
        'size': 4,
        'comment': 'Advanced timer unit channel 0 input capture interrupt C',
    },
    0x00000168: {
        'name': 'v_atu03_ici0D',
        'size': 4,
        'comment': 'Advanced timer unit channel 0 input capture interrupt D',
    },
    0x00000170: {
        'name': 'v_atu04_ovi0',
        'size': 4,
        'comment': 'Advanced timer unit channel 0 overflow interrupt',
    },
    0x00000180: {
        'name': 'v_atu11_imi1A',
        'size': 4,
        'comment': ('Advanced timer unit channel 1 input '
                    'capture/compare-match interrupt A'),
    },
    0x00000184: {
        'name': 'v_atu11_imi1B',
        'size': 4,
        'comment': ('Advanced timer unit channel 1 input '
                    'capture/compare-match interrupt B'),
    },
    0x00000188: {
        'name': 'v_atu11_imi1C',
        'size': 4,
        'comment': ('Advanced timer unit channel 1 input '
                    'capture/compare-match interrupt C'),
    },
    0x0000018C: {
        'name': 'v_atu11_imi1D',
        'size': 4,
        'comment': ('Advanced timer unit channel 1 input '
                    'capture/compare-match interrupt D'),
    },
    0x00000190: {
        'name': 'v_atu12_imi1E',
        'size': 4,
        'comment': ('Advanced timer unit channel 1 input '
                    'capture/compare-match interrupt E'),
    },
    0x00000194: {
        'name': 'v_atu12_imi1F',
        'size': 4,
        'comment': ('Advanced timer unit channel 1 input '
                    'capture/compare-match interrupt F'),
    },
    0x00000198: {
        'name': 'v_atu12_imi1G',
        'size': 4,
        'comment': ('Advanced timer unit channel 1 input '
                    'capture/compare-match interrupt G'),
    },
    0x0000019C: {
        'name': 'v_atu12_imi1H',
        'size': 4,
        'comment': ('Advanced timer unit channel 1 input '
                    'capture/compare-match interrupt H'),
    },
    0x000001A0: {
        'name': 'v_atu13_ovi1AB',
        'size': 4,
        'comment': ('Advanced timer unit channel 1 counter overflow '
                    'interrupt A/B'),
    },
    0x000001B0: {
        'name': 'v_atu21_imi2A',
        'size': 4,
        'comment': ('Advanced timer unit channel 2 input '
                    'capture/compare-match interrupt A'),
    },
    0x000001B4: {
        'name': 'v_atu21_imi2B',
        'size': 4,
        'comment': ('Advanced timer unit channel 2 input '
                    'capture/compare-match interrupt B'),
    },
    0x000001B8: {
        'name': 'v_atu21_imi2C',
        'size': 4,
        'comment': ('Advanced timer unit channel 2 input '
                    'capture/compare-match interrupt C'),
    },
    0x000001BC: {
        'name': 'v_atu21_imi2D',
        'size': 4,
        'comment': ('Advanced timer unit channel 2 input '
                    'capture/compare-match interrupt D'),
    },
    0x000001C0: {
        'name': 'v_atu22_imi2E',
        'size': 4,
        'comment': ('Advanced timer unit channel 2 input '
                    'capture/compare-match interrupt E'),
    },
    0x000001C4: {
        'name': 'v_atu22_imi2F',
        'size': 4,
        'comment': ('Advanced timer unit channel 2 input '
                    'capture/compare-match interrupt F'),
    },
    0x000001C8: {
        'name': 'v_atu22_imi2G',
        'size': 4,
        'comment': ('Advanced timer unit channel 2 input '
                    'capture/compare-match interrupt G'),
    },
    0x000001CC: {
        'name': 'v_atu22_imi2H',
        'size': 4,
        'comment': ('Advanced timer unit channel 2 input '
                    'capture/compare-match interrupt H'),
    },
    0x000001D0: {
        'name': 'v_atu23_ovi2AB',
        'size': 4,
        'comment': ('Advanced timer unit channel 2 counter overflow '
                    'interrupt A/B'),
    },
    0x000001E0: {
        'name': 'v_atu31_imi3A',
        'size': 4,
        'comment': ('Advanced timer unit channel 3 input '
                    'capture/compare-match interrupt A'),
    },
    0x000001E4: {
        'name': 'v_atu31_imi3B',
        'size': 4,
        'comment': ('Advanced timer unit channel 3 input '
                    'capture/compare-match interrupt B'),
    },
    0x000001E8: {
        'name': 'v_atu31_imi3C',
        'size': 4,
        'comment': ('Advanced timer unit channel 3 input '
                    'capture/compare-match interrupt C'),
    },
    0x000001EC: {
        'name': 'v_atu31_imi3D',
        'size': 4,
        'comment': ('Advanced timer unit channel 3 input '
                    'capture/compare-match interrupt D'),
    },
    0x000001F0: {
        'name': 'v_atu32_ovi3',
        'size': 4,
        'comment': 'Advanced timer unit channel 3 counter overflow interrupt',
    },
    0x00000200: {
        'name': 'v_atu41_imi4A',
        'size': 4,
        'comment': ('Advanced timer unit channel 4 input '
                    'capture/compare-match interrupt A'),
    },
    0x00000204: {
        'name': 'v_atu41_imi4B',
        'size': 4,
        'comment': ('Advanced timer unit channel 4 input '
                    'capture/compare-match interrupt B'),
    },
    0x00000208: {
        'name': 'v_atu41_imi4C',
        'size': 4,
        'comment': ('Advanced timer unit channel 4 input '
                    'capture/compare-match interrupt C'),
    },
    0x0000020C: {
        'name': 'v_atu41_imi4D',
        'size': 4,
        'comment': ('Advanced timer unit channel 4 input '
                    'capture/compare-match interrupt D'),
    },
    0x00000210: {
        'name': 'v_atu42_ovi4',
        'size': 4,
        'comment': 'Advanced timer unit channel 4 counter overflow interrupt',
    },
    0x00000220: {
        'name': 'v_atu51_imi5A',
        'size': 4,
        'comment': ('Advanced timer unit channel 5 input '
                    'capture/compare-match interrupt A'),
    },
    0x00000224: {
        'name': 'v_atu51_imi5B',
        'size': 4,
        'comment': ('Advanced timer unit channel 5 input '
                    'capture/compare-match interrupt B'),
    },
    0x00000228: {
        'name': 'v_atu51_imi5C',
        'size': 4,
        'comment': ('Advanced timer unit channel 5 input '
                    'capture/compare-match interrupt C'),
    },
    0x0000022C: {
        'name': 'v_atu51_imi5D',
        'size': 4,
        'comment': ('Advanced timer unit channel 5 input '
                    'capture/compare-match interrupt D'),
    },
    0x00000230: {
        'name': 'v_atu52_ovi5',
        'size': 4,
        'comment': 'Advanced timer unit channel 5 counter overflow interrupt',
    },
    0x00000240: {
        'name': 'v_atu6_cmi6A',
        'size': 4,
        'comment': 'Advanced timer unit channel 6 compare-match interrupt A',
    },
    0x00000244: {
        'name': 'v_atu6_cmi6B',
        'size': 4,
        'comment': 'Advanced timer unit channel 6 compare-match interrupt B',
    },
    0x00000248: {
        'name': 'v_atu6_cmi6C',
        'size': 4,
        'comment': 'Advanced timer unit channel 6 compare-match interrupt C',
    },
    0x0000024C: {
        'name': 'v_atu6_cmi6D',
        'size': 4,
        'comment': 'Advanced timer unit channel 6 compare-match interrupt D',
    },
    0x00000250: {
        'name': 'v_atu7_cmi7A',
        'size': 4,
        'comment': 'Advanced timer unit channel 7 compare-match interrupt A',
    },
    0x00000254: {
        'name': 'v_atu7_cmi7B',
        'size': 4,
        'comment': 'Advanced timer unit channel 7 compare-match interrupt B',
    },
    0x00000258: {
        'name': 'v_atu7_cmi7C',
        'size': 4,
        'comment': 'Advanced timer unit channel 7 compare-match interrupt C',
    },
    0x0000025C: {
        'name': 'v_atu7_cmi7D',
        'size': 4,
        'comment': 'Advanced timer unit channel 7 compare-match interrupt D',
    },
    0x00000260: {
        'name': 'v_atu81_osi8A',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt A',
    },
    0x00000264: {
        'name': 'v_atu81_osi8B',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt B',
    },
    0x00000268: {
        'name': 'v_atu81_osi8C',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt C',
    },
    0x0000026C: {
        'name': 'v_atu81_osi8D',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt D',
    },
    0x00000270: {
        'name': 'v_atu82_osi8E',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt E',
    },
    0x00000274: {
        'name': 'v_atu82_osi8F',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt F',
    },
    0x00000278: {
        'name': 'v_atu82_osi8G',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt G',
    },
    0x0000027C: {
        'name': 'v_atu82_osi8H',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt H',
    },
    0x00000280: {
        'name': 'v_atu83_osi8I',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt I',
    },
    0x00000284: {
        'name': 'v_atu83_osi8J',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt J',
    },
    0x00000288: {
        'name': 'v_atu83_osi8K',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt K',
    },
    0x0000028C: {
        'name': 'v_atu83_osi8L',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt L',
    },
    0x00000290: {
        'name': 'v_atu84_osi8M',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt M',
    },
    0x00000294: {
        'name': 'v_atu84_osi8N',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt N',
    },
    0x00000298: {
        'name': 'v_atu84_osi8O',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt O',
    },
    0x0000029C: {
        'name': 'v_atu84_osi8P',
        'size': 4,
        'comment': 'Advanced timer unit channel 8 one-shot end interrupt P',
    },
    0x000002A0: {
        'name': 'v_atu91_cmi9A',
        'size': 4,
        'comment': 'Advanced timer unit channel 9 compare-match interrupt A',
    },
    0x000002A4: {
        'name': 'v_atu91_cmi9B',
        'size': 4,
        'comment': 'Advanced timer unit channel 9 compare-match interrupt B',
    },
    0x000002A8: {
        'name': 'v_atu91_cmi9C',
        'size': 4,
        'comment': 'Advanced timer unit channel 9 compare-match interrupt C',
    },
    0x000002AC: {
        'name': 'v_atu91_cmi9D',
        'size': 4,
        'comment': 'Advanced timer unit channel 9 compare-match interrupt D',
    },
    0x000002B0: {
        'name': 'v_atu92_cmi9E',
        'size': 4,
        'comment': 'Advanced timer unit channel 9 compare-match interrupt E',
    },
    0x000002B8: {
        'name': 'v_atu92_cmi9F',
        'size': 4,
        'comment': 'Advanced timer unit channel 9 compare-match interrupt F',
    },
    0x000002C0: {
        'name': 'v_atu101_cmi10A',
        'size': 4,
        'comment': 'Advanced timer unit channel 10 compare-match interrupt A',
    },
    0x000002C8: {
        'name': 'v_atu101_cmi10B',
        'size': 4,
        'comment': 'Advanced timer unit channel 10 compare-match interrupt B',
    },
    0x000002D0: {
        'name': 'v_atu102_ici10A',
        'size': 4,
        'comment': 'Advanced timer unit channel 10 compare-match interrupt C',
    },
    0x000002E0: {
        'name': 'v_atu11_imi11A',
        'size': 4,
        'comment': ('Advanced timer unit channel 11 input '
                    'capture/compare-match interrupt A'),
    },
    0x000002E8: {
        'name': 'v_atu11_imi11B',
        'size': 4,
        'comment': ('Advanced timer unit channel 11 input '
                    'capture/compare-match interrupt B'),
    },
    0x000002EC: {
        'name': 'v_atu11_ovi11',
        'size': 4,
        'comment': 'Advanced timer unit channel 11 overflow interrupt',
    },
    0x000002F0: {
        'name': 'v_cmti0',
        'size': 4,
        'comment': 'Compare match timer 0 interrupt',
    },
    0x000002F8: {
        'name': 'v_adi0',
        'size': 4,
        'comment': 'A/D converter 0 interrupt',
    },
    0x00000300: {
        'name': 'v_cmti1',
        'size': 4,
        'comment': 'Compare match timer 1 interrupt',
    },
    0x00000308: {
        'name': 'v_adi1',
        'size': 4,
        'comment': 'A/D converter 1 interrupt',
    },
    0x00000310: {
        'name': 'v_adi2',
        'size': 4,
        'comment': 'A/D converter 2 interrupt',
    },
    0x00000320: {
        'name': 'v_sci0_eri0',
        'size': 4,
        'comment': 'Serial communication interface 0 receive-error interrupt',
    },
    0x00000324: {
        'name': 'v_sci0_rxi0',
        'size': 4,
        'comment': ('Serial communication interface 0 receive-data-full '
                    'interrupt'),
    },
    0x00000328: {
        'name': 'v_sci0_txi0',
        'size': 4,
        'comment': ('Serial communication interface 0 transmit-data-empty '
                    'interrupt'),
    },
    0x0000032C: {
        'name': 'v_sci0_tei0',
        'size': 4,
        'comment': 'Serial communication interface 0 transmit-end interrupt',
    },
    0x00000330: {
        'name': 'v_sci1_eri1',
        'size': 4,
        'comment': 'Serial communication interface 1 receive-error interrupt',
    },
    0x00000334: {
        'name': 'v_sci1_rxi1',
        'size': 4,
        'comment': ('Serial communication interface 1 receive-data-full '
                    'interrupt'),
    },
    0x00000338: {
        'name': 'v_sci1_txi1',
        'size': 4,
        'comment': ('Serial communication interface 1 transmit-data-empty '
                    'interrupt'),
    },
    0x0000033C: {
        'name': 'v_sci1_tei1',
        'size': 4,
        'comment': 'Serial communication interface 1 transmit-end interrupt',
    },
    0x00000340: {
        'name': 'v_sci2_eri2',
        'size': 4,
        'comment': 'Serial communication interface 2 receive-error interrupt',
    },
    0x00000344: {
        'name': 'v_sci2_rxi2',
        'size': 4,
        'comment': ('Serial communication interface 2 receive-data-full '
                    'interrupt'),
    },
    0x00000348: {
        'name': 'v_sci2_txi2',
        'size': 4,
        'comment': ('Serial communication interface 2 transmit-data-empty '
                    'interrupt'),
    },
    0x0000034C: {
        'name': 'v_sci2_tei2',
        'size': 4,
        'comment': 'Serial communication interface 2 transmit-end interrupt',
    },
    0x00000350: {
        'name': 'v_sci3_eri3',
        'size': 4,
        'comment': 'Serial communication interface 3 receive-error interrupt',
    },
    0x00000354: {
        'name': 'v_sci3_rxi3',
        'size': 4,
        'comment': ('Serial communication interface 3 receive-data-full '
                    'interrupt'),
    },
    0x00000358: {
        'name': 'v_sci3_txi3',
        'size': 4,
        'comment': ('Serial communication interface 3 transmit-data-empty '
                    'interrupt'),
    },
    0x0000035C: {
        'name': 'v_sci3_tei3',
        'size': 4,
        'comment': 'Serial communication interface 3 transmit-end interrupt',
    },
    0x00000360: {
        'name': 'v_sci4_eri4',
        'size': 4,
        'comment': 'Serial communication interface 4 receive-error interrupt',
    },
    0x00000364: {
        'name': 'v_sci4_rxi4',
        'size': 4,
        'comment': ('Serial communication interface 4 receive-data-full '
                    'interrupt'),
    },
    0x00000368: {
        'name': 'v_sci4_txi4',
        'size': 4,
        'comment': ('Serial communication interface 4 transmit-data-empty '
                    'interrupt'),
    },
    0x0000036C: {
        'name': 'v_sci4_tei4',
        'size': 4,
        'comment': 'Serial communication interface 4 transmit-end interrupt',
    },
    0x00000370: {
        'name': 'v_hcan0_ers',
        'size': 4,
        'comment': 'Error passive interrupt request',
    },
    0x00000374: {
        'name': 'v_hcan0_ovr',
        'size': 4,
        'comment': 'Receive overload warning interrupt',
    },
    0x00000378: {
        'name': 'v_hcan0_rm',
        'size': 4,
        'comment': 'Receive message interrupt',
    },
    0x0000037C: {
        'name': 'v_hcan0_sle',
        'size': 4,
        'comment': 'Mailbox empty interrupt',
    },
    0x00000380: {
        'name': 'v_wdt_iti',
        'size': 4,
        'comment': 'Watchdog timer interval timer interrupt',
    },
    0x00000390: {
        'name': 'v_hcan1_ers',
        'size': 4,
        'comment': 'Error passive interrupt request',
    },
    0x00000394: {
        'name': 'v_hcan1_ovr',
        'size': 4,
        'comment': 'Receive overload warning interrupt',
    },
    0x00000398: {
        'name': 'v_hcan1_rm',
        'size': 4,
        'comment': 'Receive message interrupt',
    },
    0x0000039C: {
        'name': 'v_hcan1_sle',
        'size': 4,
        'comment': 'Mailbox empty interrupt',
    },
}

REGISTERS = {
    0xFFFFE400: {
        'name': 'HCAN0_MCR',
        'size': 1,
        'comment': 'HCAN0 Master control register',
    },
    0xFFFFE401: {
        'name': 'HCAN0_GSR',
        'size': 1,
        'comment': 'HCAN0 General status register',
    },
    0xFFFFE402: {
        'name': 'HCAN0_BCR',
        'size': 2,
        'comment': 'HCAN0 Bit configuration register',
    },
    0xFFFFE404: {
        'name': 'HCAN0_MBCR',
        'size': 2,
        'comment': 'HCAN0 Mailbox configuration register',
    },
    0xFFFFE406: {
        'name': 'HCAN0_TXPR',
        'size': 2,
        'comment': 'HCAN0 Transmit wait register',
    },
    0xFFFFE408: {
        'name': 'HCAN0_TXCR',
        'size': 2,
        'comment': 'HCAN0 Transmit wait cancel register',
    },
    0xFFFFE40A: {
        'name': 'HCAN0_TXACK',
        'size': 2,
        'comment': 'HCAN0 Transmit acknowledge register',
    },
    0xFFFFE40C: {
        'name': 'HCAN0_ABACK',
        'size': 2,
        'comment': 'HCAN0 Abort acknowledge register',
    },
    0xFFFFE40E: {
        'name': 'HCAN0_RXPR',
        'size': 2,
        'comment': 'HCAN0 Receive complete register',
    },
    0xFFFFE410: {
        'name': 'HCAN0_RFPR',
        'size': 2,
        'comment': 'HCAN0 Remote request register',
    },
    0xFFFFE412: {
        'name': 'HCAN0_IRR',
        'size': 2,
        'comment': 'HCAN0 Interrupt register',
    },
    0xFFFFE414: {
        'name': 'HCAN0_MBIMR',
        'size': 2,
        'comment': 'HCAN0 Mailbox interrupt mask register',
    },
    0xFFFFE416: {
        'name': 'HCAN0_IMR',
        'size': 2,
        'comment': 'HCAN0 Interrupt mask register',
    },
    0xFFFFE418: {
        'name': 'HCAN0_REC',
        'size': 1,
        'comment': 'HCAN0 Receive error counter',
    },
    0xFFFFE419: {
        'name': 'HCAN0_TEC',
        'size': 1,
        'comment': 'HCAN0 Transmit error counter',
    },
    0xFFFFE41A: {
        'name': 'HCAN0_UMSR',
        'size': 2,
        'comment': 'HCAN0 Unread message status register',
    },
    0xFFFFE41C: {
        'name': 'HCAN0_LAFML',
        'size': 2,
        'comment': 'HCAN0 Local acceptance filter mask L',
    },
    0xFFFFE41E: {
        'name': 'HCAN0_LAFMH',
        'size': 2,
        'comment': 'HCAN0 Local acceptance filter mask H',
    },
    0xFFFFE420: {
        'name': 'HCAN0_MC0_1',
        'size': 1,
        'comment': 'HCAN0 Message control 0 1',
    },
    0xFFFFE421: {
        'name': 'HCAN0_MC0_2',
        'size': 1,
        'comment': 'HCAN0 Message control 0 2',
    },
    0xFFFFE422: {
        'name': 'HCAN0_MC0_3',
        'size': 1,
        'comment': 'HCAN0 Message control 0 3',
    },
    0xFFFFE423: {
        'name': 'HCAN0_MC0_4',
        'size': 1,
        'comment': 'HCAN0 Message control 0 4',
    },
    0xFFFFE424: {
        'name': 'HCAN0_MC0_5',
        'size': 1,
        'comment': 'HCAN0 Message control 0 5',
    },
    0xFFFFE425: {
        'name': 'HCAN0_MC0_6',
        'size': 1,
        'comment': 'HCAN0 Message control 0 6',
    },
    0xFFFFE426: {
        'name': 'HCAN0_MC0_7',
        'size': 1,
        'comment': 'HCAN0 Message control 0 7',
    },
    0xFFFFE427: {
        'name': 'HCAN0_MC0_8',
        'size': 1,
        'comment': 'HCAN0 Message control 0 8',
    },
    0xFFFFE428: {
        'name': 'HCAN0_MC1_1',
        'size': 1,
        'comment': 'HCAN0 Message control 1 1',
    },
    0xFFFFE429: {
        'name': 'HCAN0_MC1_2',
        'size': 1,
        'comment': 'HCAN0 Message control 1 2',
    },
    0xFFFFE42A: {
        'name': 'HCAN0_MC1_3',
        'size': 1,
        'comment': 'HCAN0 Message control 1 3',
    },
    0xFFFFE42B: {
        'name': 'HCAN0_MC1_4',
        'size': 1,
        'comment': 'HCAN0 Message control 1 4',
    },
    0xFFFFE42C: {
        'name': 'HCAN0_MC1_5',
        'size': 1,
        'comment': 'HCAN0 Message control 1 5',
    },
    0xFFFFE42D: {
        'name': 'HCAN0_MC1_6',
        'size': 1,
        'comment': 'HCAN0 Message control 1 6',
    },
    0xFFFFE42E: {
        'name': 'HCAN0_MC1_7',
        'size': 1,
        'comment': 'HCAN0 Message control 1 7',
    },
    0xFFFFE42F: {
        'name': 'HCAN0_MC1_8',
        'size': 1,
        'comment': 'HCAN0 Message control 1 8',
    },
    0xFFFFE430: {
        'name': 'HCAN0_MC2_1',
        'size': 1,
        'comment': 'HCAN0 Message control 2 1',
    },
    0xFFFFE431: {
        'name': 'HCAN0_MC2_2',
        'size': 1,
        'comment': 'HCAN0 Message control 2 2',
    },
    0xFFFFE432: {
        'name': 'HCAN0_MC2_3',
        'size': 1,
        'comment': 'HCAN0 Message control 2 3',
    },
    0xFFFFE433: {
        'name': 'HCAN0_MC2_4',
        'size': 1,
        'comment': 'HCAN0 Message control 2 4',
    },
    0xFFFFE434: {
        'name': 'HCAN0_MC2_5',
        'size': 1,
        'comment': 'HCAN0 Message control 2 5',
    },
    0xFFFFE435: {
        'name': 'HCAN0_MC2_6',
        'size': 1,
        'comment': 'HCAN0 Message control 2 6',
    },
    0xFFFFE436: {
        'name': 'HCAN0_MC2_7',
        'size': 1,
        'comment': 'HCAN0 Message control 2 7',
    },
    0xFFFFE437: {
        'name': 'HCAN0_MC2_8',
        'size': 1,
        'comment': 'HCAN0 Message control 2 8',
    },
    0xFFFFE438: {
        'name': 'HCAN0_MC3_1',
        'size': 1,
        'comment': 'HCAN0 Message control 3 1',
    },
    0xFFFFE439: {
        'name': 'HCAN0_MC3_2',
        'size': 1,
        'comment': 'HCAN0 Message control 3 2',
    },
    0xFFFFE43A: {
        'name': 'HCAN0_MC3_3',
        'size': 1,
        'comment': 'HCAN0 Message control 3 3',
    },
    0xFFFFE43B: {
        'name': 'HCAN0_MC3_4',
        'size': 1,
        'comment': 'HCAN0 Message control 3 4',
    },
    0xFFFFE43C: {
        'name': 'HCAN0_MC3_5',
        'size': 1,
        'comment': 'HCAN0 Message control 3 5',
    },
    0xFFFFE43D: {
        'name': 'HCAN0_MC3_6',
        'size': 1,
        'comment': 'HCAN0 Message control 3 6',
    },
    0xFFFFE43E: {
        'name': 'HCAN0_MC3_7',
        'size': 1,
        'comment': 'HCAN0 Message control 3 7',
    },
    0xFFFFE43F: {
        'name': 'HCAN0_MC3_8',
        'size': 1,
        'comment': 'HCAN0 Message control 3 8',
    },
    0xFFFFE440: {
        'name': 'HCAN0_MC4_1',
        'size': 1,
        'comment': 'HCAN0 Message control 4 1',
    },
    0xFFFFE441: {
        'name': 'HCAN0_MC4_2',
        'size': 1,
        'comment': 'HCAN0 Message control 4 2',
    },
    0xFFFFE442: {
        'name': 'HCAN0_MC4_3',
        'size': 1,
        'comment': 'HCAN0 Message control 4 3',
    },
    0xFFFFE443: {
        'name': 'HCAN0_MC4_4',
        'size': 1,
        'comment': 'HCAN0 Message control 4 4',
    },
    0xFFFFE444: {
        'name': 'HCAN0_MC4_5',
        'size': 1,
        'comment': 'HCAN0 Message control 4 5',
    },
    0xFFFFE445: {
        'name': 'HCAN0_MC4_6',
        'size': 1,
        'comment': 'HCAN0 Message control 4 6',
    },
    0xFFFFE446: {
        'name': 'HCAN0_MC4_7',
        'size': 1,
        'comment': 'HCAN0 Message control 4 7',
    },
    0xFFFFE447: {
        'name': 'HCAN0_MC4_8',
        'size': 1,
        'comment': 'HCAN0 Message control 4 8',
    },
    0xFFFFE448: {
        'name': 'HCAN0_MC5_1',
        'size': 1,
        'comment': 'HCAN0 Message control 5 1',
    },
    0xFFFFE449: {
        'name': 'HCAN0_MC5_2',
        'size': 1,
        'comment': 'HCAN0 Message control 5 2',
    },
    0xFFFFE44A: {
        'name': 'HCAN0_MC5_3',
        'size': 1,
        'comment': 'HCAN0 Message control 5 3',
    },
    0xFFFFE44B: {
        'name': 'HCAN0_MC5_4',
        'size': 1,
        'comment': 'HCAN0 Message control 5 4',
    },
    0xFFFFE44C: {
        'name': 'HCAN0_MC5_5',
        'size': 1,
        'comment': 'HCAN0 Message control 5 5',
    },
    0xFFFFE44D: {
        'name': 'HCAN0_MC5_6',
        'size': 1,
        'comment': 'HCAN0 Message control 5 6',
    },
    0xFFFFE44E: {
        'name': 'HCAN0_MC5_7',
        'size': 1,
        'comment': 'HCAN0 Message control 5 7',
    },
    0xFFFFE44F: {
        'name': 'HCAN0_MC5_8',
        'size': 1,
        'comment': 'HCAN0 Message control 5 8',
    },
    0xFFFFE450: {
        'name': 'HCAN0_MC6_1',
        'size': 1,
        'comment': 'HCAN0 Message control 6 1',
    },
    0xFFFFE451: {
        'name': 'HCAN0_MC6_2',
        'size': 1,
        'comment': 'HCAN0 Message control 6 2',
    },
    0xFFFFE452: {
        'name': 'HCAN0_MC6_3',
        'size': 1,
        'comment': 'HCAN0 Message control 6 3',
    },
    0xFFFFE453: {
        'name': 'HCAN0_MC6_4',
        'size': 1,
        'comment': 'HCAN0 Message control 6 4',
    },
    0xFFFFE454: {
        'name': 'HCAN0_MC6_5',
        'size': 1,
        'comment': 'HCAN0 Message control 6 5',
    },
    0xFFFFE455: {
        'name': 'HCAN0_MC6_6',
        'size': 1,
        'comment': 'HCAN0 Message control 6 6',
    },
    0xFFFFE456: {
        'name': 'HCAN0_MC6_7',
        'size': 1,
        'comment': 'HCAN0 Message control 6 7',
    },
    0xFFFFE457: {
        'name': 'HCAN0_MC6_8',
        'size': 1,
        'comment': 'HCAN0 Message control 6 8',
    },
    0xFFFFE458: {
        'name': 'HCAN0_MC7_1',
        'size': 1,
        'comment': 'HCAN0 Message control 7 1',
    },
    0xFFFFE459: {
        'name': 'HCAN0_MC7_2',
        'size': 1,
        'comment': 'HCAN0 Message control 7 2',
    },
    0xFFFFE45A: {
        'name': 'HCAN0_MC7_3',
        'size': 1,
        'comment': 'HCAN0 Message control 7 3',
    },
    0xFFFFE45B: {
        'name': 'HCAN0_MC7_4',
        'size': 1,
        'comment': 'HCAN0 Message control 7 4',
    },
    0xFFFFE45C: {
        'name': 'HCAN0_MC7_5',
        'size': 1,
        'comment': 'HCAN0 Message control 7 5',
    },
    0xFFFFE45D: {
        'name': 'HCAN0_MC7_6',
        'size': 1,
        'comment': 'HCAN0 Message control 7 6',
    },
    0xFFFFE45E: {
        'name': 'HCAN0_MC7_7',
        'size': 1,
        'comment': 'HCAN0 Message control 7 7',
    },
    0xFFFFE45F: {
        'name': 'HCAN0_MC7_8',
        'size': 1,
        'comment': 'HCAN0 Message control 7 8',
    },
    0xFFFFE460: {
        'name': 'HCAN0_MC8_1',
        'size': 1,
        'comment': 'HCAN0 Message control 8 1',
    },
    0xFFFFE461: {
        'name': 'HCAN0_MC8_2',
        'size': 1,
        'comment': 'HCAN0 Message control 8 2',
    },
    0xFFFFE462: {
        'name': 'HCAN0_MC8_3',
        'size': 1,
        'comment': 'HCAN0 Message control 8 3',
    },
    0xFFFFE463: {
        'name': 'HCAN0_MC8_4',
        'size': 1,
        'comment': 'HCAN0 Message control 8 4',
    },
    0xFFFFE464: {
        'name': 'HCAN0_MC8_5',
        'size': 1,
        'comment': 'HCAN0 Message control 8 5',
    },
    0xFFFFE465: {
        'name': 'HCAN0_MC8_6',
        'size': 1,
        'comment': 'HCAN0 Message control 8 6',
    },
    0xFFFFE466: {
        'name': 'HCAN0_MC8_7',
        'size': 1,
        'comment': 'HCAN0 Message control 8 7',
    },
    0xFFFFE467: {
        'name': 'HCAN0_MC8_8',
        'size': 1,
        'comment': 'HCAN0 Message control 8 8',
    },
    0xFFFFE468: {
        'name': 'HCAN0_MC9_1',
        'size': 1,
        'comment': 'HCAN0 Message control 9 1',
    },
    0xFFFFE469: {
        'name': 'HCAN0_MC9_2',
        'size': 1,
        'comment': 'HCAN0 Message control 9 2',
    },
    0xFFFFE46A: {
        'name': 'HCAN0_MC9_3',
        'size': 1,
        'comment': 'HCAN0 Message control 9 3',
    },
    0xFFFFE46B: {
        'name': 'HCAN0_MC9_4',
        'size': 1,
        'comment': 'HCAN0 Message control 9 4',
    },
    0xFFFFE46C: {
        'name': 'HCAN0_MC9_5',
        'size': 1,
        'comment': 'HCAN0 Message control 9 5',
    },
    0xFFFFE46D: {
        'name': 'HCAN0_MC9_6',
        'size': 1,
        'comment': 'HCAN0 Message control 9 6',
    },
    0xFFFFE46E: {
        'name': 'HCAN0_MC9_7',
        'size': 1,
        'comment': 'HCAN0 Message control 9 7',
    },
    0xFFFFE46F: {
        'name': 'HCAN0_MC9_8',
        'size': 1,
        'comment': 'HCAN0 Message control 9 8',
    },
    0xFFFFE470: {
        'name': 'HCAN0_MC10_1',
        'size': 1,
        'comment': 'HCAN0 Message control 10 1',
    },
    0xFFFFE471: {
        'name': 'HCAN0_MC10_2',
        'size': 1,
        'comment': 'HCAN0 Message control 10 2',
    },
    0xFFFFE472: {
        'name': 'HCAN0_MC10_3',
        'size': 1,
        'comment': 'HCAN0 Message control 10 3',
    },
    0xFFFFE473: {
        'name': 'HCAN0_MC10_4',
        'size': 1,
        'comment': 'HCAN0 Message control 10 4',
    },
    0xFFFFE474: {
        'name': 'HCAN0_MC10_5',
        'size': 1,
        'comment': 'HCAN0 Message control 10 5',
    },
    0xFFFFE475: {
        'name': 'HCAN0_MC10_6',
        'size': 1,
        'comment': 'HCAN0 Message control 10 6',
    },
    0xFFFFE476: {
        'name': 'HCAN0_MC10_7',
        'size': 1,
        'comment': 'HCAN0 Message control 10 7',
    },
    0xFFFFE477: {
        'name': 'HCAN0_MC10_8',
        'size': 1,
        'comment': 'HCAN0 Message control 10 8',
    },
    0xFFFFE478: {
        'name': 'HCAN0_MC11_1',
        'size': 1,
        'comment': 'HCAN0 Message control 11 1',
    },
    0xFFFFE479: {
        'name': 'HCAN0_MC11_2',
        'size': 1,
        'comment': 'HCAN0 Message control 11 2',
    },
    0xFFFFE47A: {
        'name': 'HCAN0_MC11_3',
        'size': 1,
        'comment': 'HCAN0 Message control 11 3',
    },
    0xFFFFE47B: {
        'name': 'HCAN0_MC11_4',
        'size': 1,
        'comment': 'HCAN0 Message control 11 4',
    },
    0xFFFFE47C: {
        'name': 'HCAN0_MC11_5',
        'size': 1,
        'comment': 'HCAN0 Message control 11 5',
    },
    0xFFFFE47D: {
        'name': 'HCAN0_MC11_6',
        'size': 1,
        'comment': 'HCAN0 Message control 11 6',
    },
    0xFFFFE47E: {
        'name': 'HCAN0_MC11_7',
        'size': 1,
        'comment': 'HCAN0 Message control 11 7',
    },
    0xFFFFE47F: {
        'name': 'HCAN0_MC11_8',
        'size': 1,
        'comment': 'HCAN0 Message control 11 8',
    },
    0xFFFFE480: {
        'name': 'HCAN0_MC12_1',
        'size': 1,
        'comment': 'HCAN0 Message control 12 1',
    },
    0xFFFFE481: {
        'name': 'HCAN0_MC12_2',
        'size': 1,
        'comment': 'HCAN0 Message control 12 2',
    },
    0xFFFFE482: {
        'name': 'HCAN0_MC12_3',
        'size': 1,
        'comment': 'HCAN0 Message control 12 3',
    },
    0xFFFFE483: {
        'name': 'HCAN0_MC12_4',
        'size': 1,
        'comment': 'HCAN0 Message control 12 4',
    },
    0xFFFFE484: {
        'name': 'HCAN0_MC12_5',
        'size': 1,
        'comment': 'HCAN0 Message control 12 5',
    },
    0xFFFFE485: {
        'name': 'HCAN0_MC12_6',
        'size': 1,
        'comment': 'HCAN0 Message control 12 6',
    },
    0xFFFFE486: {
        'name': 'HCAN0_MC12_7',
        'size': 1,
        'comment': 'HCAN0 Message control 12 7',
    },
    0xFFFFE487: {
        'name': 'HCAN0_MC12_8',
        'size': 1,
        'comment': 'HCAN0 Message control 12 8',
    },
    0xFFFFE488: {
        'name': 'HCAN0_MC13_1',
        'size': 1,
        'comment': 'HCAN0 Message control 13 1',
    },
    0xFFFFE489: {
        'name': 'HCAN0_MC13_2',
        'size': 1,
        'comment': 'HCAN0 Message control 13 2',
    },
    0xFFFFE48A: {
        'name': 'HCAN0_MC13_3',
        'size': 1,
        'comment': 'HCAN0 Message control 13 3',
    },
    0xFFFFE48B: {
        'name': 'HCAN0_MC13_4',
        'size': 1,
        'comment': 'HCAN0 Message control 13 4',
    },
    0xFFFFE48C: {
        'name': 'HCAN0_MC13_5',
        'size': 1,
        'comment': 'HCAN0 Message control 13 5',
    },
    0xFFFFE48D: {
        'name': 'HCAN0_MC13_6',
        'size': 1,
        'comment': 'HCAN0 Message control 13 6',
    },
    0xFFFFE48E: {
        'name': 'HCAN0_MC13_7',
        'size': 1,
        'comment': 'HCAN0 Message control 13 7',
    },
    0xFFFFE48F: {
        'name': 'HCAN0_MC13_8',
        'size': 1,
        'comment': 'HCAN0 Message control 13 8',
    },
    0xFFFFE490: {
        'name': 'HCAN0_MC14_1',
        'size': 1,
        'comment': 'HCAN0 Message control 14 1',
    },
    0xFFFFE491: {
        'name': 'HCAN0_MC14_2',
        'size': 1,
        'comment': 'HCAN0 Message control 14 2',
    },
    0xFFFFE492: {
        'name': 'HCAN0_MC14_3',
        'size': 1,
        'comment': 'HCAN0 Message control 14 3',
    },
    0xFFFFE493: {
        'name': 'HCAN0_MC14_4',
        'size': 1,
        'comment': 'HCAN0 Message control 14 4',
    },
    0xFFFFE494: {
        'name': 'HCAN0_MC14_5',
        'size': 1,
        'comment': 'HCAN0 Message control 14 5',
    },
    0xFFFFE495: {
        'name': 'HCAN0_MC14_6',
        'size': 1,
        'comment': 'HCAN0 Message control 14 6',
    },
    0xFFFFE496: {
        'name': 'HCAN0_MC14_7',
        'size': 1,
        'comment': 'HCAN0 Message control 14 7',
    },
    0xFFFFE497: {
        'name': 'HCAN0_MC14_8',
        'size': 1,
        'comment': 'HCAN0 Message control 14 8',
    },
    0xFFFFE498: {
        'name': 'HCAN0_MC15_1',
        'size': 1,
        'comment': 'HCAN0 Message control 15 1',
    },
    0xFFFFE499: {
        'name': 'HCAN0_MC15_2',
        'size': 1,
        'comment': 'HCAN0 Message control 15 2',
    },
    0xFFFFE49A: {
        'name': 'HCAN0_MC15_3',
        'size': 1,
        'comment': 'HCAN0 Message control 15 3',
    },
    0xFFFFE49B: {
        'name': 'HCAN0_MC15_4',
        'size': 1,
        'comment': 'HCAN0 Message control 15 4',
    },
    0xFFFFE49C: {
        'name': 'HCAN0_MC15_5',
        'size': 1,
        'comment': 'HCAN0 Message control 15 5',
    },
    0xFFFFE49D: {
        'name': 'HCAN0_MC15_6',
        'size': 1,
        'comment': 'HCAN0 Message control 15 6',
    },
    0xFFFFE49E: {
        'name': 'HCAN0_MC15_7',
        'size': 1,
        'comment': 'HCAN0 Message control 15 7',
    },
    0xFFFFE49F: {
        'name': 'HCAN0_MC15_8',
        'size': 1,
        'comment': 'HCAN0 Message control 15 8',
    },
    0xFFFFE4B0: {
        'name': 'HCAN0_MD0_1',
        'size': 1,
        'comment': 'HCAN0 Message data 0 1',
    },
    0xFFFFE4B1: {
        'name': 'HCAN0_MD0_2',
        'size': 1,
        'comment': 'HCAN0 Message data 0 2',
    },
    0xFFFFE4B2: {
        'name': 'HCAN0_MD0_3',
        'size': 1,
        'comment': 'HCAN0 Message data 0 3',
    },
    0xFFFFE4B3: {
        'name': 'HCAN0_MD0_4',
        'size': 1,
        'comment': 'HCAN0 Message data 0 4',
    },
    0xFFFFE4B4: {
        'name': 'HCAN0_MD0_5',
        'size': 1,
        'comment': 'HCAN0 Message data 0 5',
    },
    0xFFFFE4B5: {
        'name': 'HCAN0_MD0_6',
        'size': 1,
        'comment': 'HCAN0 Message data 0 6',
    },
    0xFFFFE4B6: {
        'name': 'HCAN0_MD0_7',
        'size': 1,
        'comment': 'HCAN0 Message data 0 7',
    },
    0xFFFFE4B7: {
        'name': 'HCAN0_MD0_8',
        'size': 1,
        'comment': 'HCAN0 Message data 0 8',
    },
    0xFFFFE4B8: {
        'name': 'HCAN0_MD1_1',
        'size': 1,
        'comment': 'HCAN0 Message data 1 1',
    },
    0xFFFFE4B9: {
        'name': 'HCAN0_MD1_2',
        'size': 1,
        'comment': 'HCAN0 Message data 1 2',
    },
    0xFFFFE4BA: {
        'name': 'HCAN0_MD1_3',
        'size': 1,
        'comment': 'HCAN0 Message data 1 3',
    },
    0xFFFFE4BB: {
        'name': 'HCAN0_MD1_4',
        'size': 1,
        'comment': 'HCAN0 Message data 1 4',
    },
    0xFFFFE4BC: {
        'name': 'HCAN0_MD1_5',
        'size': 1,
        'comment': 'HCAN0 Message data 1 5',
    },
    0xFFFFE4BD: {
        'name': 'HCAN0_MD1_6',
        'size': 1,
        'comment': 'HCAN0 Message data 1 6',
    },
    0xFFFFE4BE: {
        'name': 'HCAN0_MD1_7',
        'size': 1,
        'comment': 'HCAN0 Message data 1 7',
    },
    0xFFFFE4BF: {
        'name': 'HCAN0_MD1_8',
        'size': 1,
        'comment': 'HCAN0 Message data 1 8',
    },
    0xFFFFE4C0: {
        'name': 'HCAN0_MD2_1',
        'size': 1,
        'comment': 'HCAN0 Message data 2 1',
    },
    0xFFFFE4C1: {
        'name': 'HCAN0_MD2_2',
        'size': 1,
        'comment': 'HCAN0 Message data 2 2',
    },
    0xFFFFE4C2: {
        'name': 'HCAN0_MD2_3',
        'size': 1,
        'comment': 'HCAN0 Message data 2 3',
    },
    0xFFFFE4C3: {
        'name': 'HCAN0_MD2_4',
        'size': 1,
        'comment': 'HCAN0 Message data 2 4',
    },
    0xFFFFE4C4: {
        'name': 'HCAN0_MD2_5',
        'size': 1,
        'comment': 'HCAN0 Message data 2 5',
    },
    0xFFFFE4C5: {
        'name': 'HCAN0_MD2_6',
        'size': 1,
        'comment': 'HCAN0 Message data 2 6',
    },
    0xFFFFE4C6: {
        'name': 'HCAN0_MD2_7',
        'size': 1,
        'comment': 'HCAN0 Message data 2 7',
    },
    0xFFFFE4C7: {
        'name': 'HCAN0_MD2_8',
        'size': 1,
        'comment': 'HCAN0 Message data 2 8',
    },
    0xFFFFE4C8: {
        'name': 'HCAN0_MD3_1',
        'size': 1,
        'comment': 'HCAN0 Message data 3 1',
    },
    0xFFFFE4C9: {
        'name': 'HCAN0_MD3_2',
        'size': 1,
        'comment': 'HCAN0 Message data 3 2',
    },
    0xFFFFE4CA: {
        'name': 'HCAN0_MD3_3',
        'size': 1,
        'comment': 'HCAN0 Message data 3 3',
    },
    0xFFFFE4CB: {
        'name': 'HCAN0_MD3_4',
        'size': 1,
        'comment': 'HCAN0 Message data 3 4',
    },
    0xFFFFE4CC: {
        'name': 'HCAN0_MD3_5',
        'size': 1,
        'comment': 'HCAN0 Message data 3 5',
    },
    0xFFFFE4CD: {
        'name': 'HCAN0_MD3_6',
        'size': 1,
        'comment': 'HCAN0 Message data 3 6',
    },
    0xFFFFE4CE: {
        'name': 'HCAN0_MD3_7',
        'size': 1,
        'comment': 'HCAN0 Message data 3 7',
    },
    0xFFFFE4CF: {
        'name': 'HCAN0_MD3_8',
        'size': 1,
        'comment': 'HCAN0 Message data 3 8',
    },
    0xFFFFE4D0: {
        'name': 'HCAN0_MD4_1',
        'size': 1,
        'comment': 'HCAN0 Message data 4 1',
    },
    0xFFFFE4D1: {
        'name': 'HCAN0_MD4_2',
        'size': 1,
        'comment': 'HCAN0 Message data 4 2',
    },
    0xFFFFE4D2: {
        'name': 'HCAN0_MD4_3',
        'size': 1,
        'comment': 'HCAN0 Message data 4 3',
    },
    0xFFFFE4D3: {
        'name': 'HCAN0_MD4_4',
        'size': 1,
        'comment': 'HCAN0 Message data 4 4',
    },
    0xFFFFE4D4: {
        'name': 'HCAN0_MD4_5',
        'size': 1,
        'comment': 'HCAN0 Message data 4 5',
    },
    0xFFFFE4D5: {
        'name': 'HCAN0_MD4_6',
        'size': 1,
        'comment': 'HCAN0 Message data 4 6',
    },
    0xFFFFE4D6: {
        'name': 'HCAN0_MD4_7',
        'size': 1,
        'comment': 'HCAN0 Message data 4 7',
    },
    0xFFFFE4D7: {
        'name': 'HCAN0_MD4_8',
        'size': 1,
        'comment': 'HCAN0 Message data 4 8',
    },
    0xFFFFE4D8: {
        'name': 'HCAN0_MD5_1',
        'size': 1,
        'comment': 'HCAN0 Message data 5 1',
    },
    0xFFFFE4D9: {
        'name': 'HCAN0_MD5_2',
        'size': 1,
        'comment': 'HCAN0 Message data 5 2',
    },
    0xFFFFE4DA: {
        'name': 'HCAN0_MD5_3',
        'size': 1,
        'comment': 'HCAN0 Message data 5 3',
    },
    0xFFFFE4DB: {
        'name': 'HCAN0_MD5_4',
        'size': 1,
        'comment': 'HCAN0 Message data 5 4',
    },
    0xFFFFE4DC: {
        'name': 'HCAN0_MD5_5',
        'size': 1,
        'comment': 'HCAN0 Message data 5 5',
    },
    0xFFFFE4DD: {
        'name': 'HCAN0_MD5_6',
        'size': 1,
        'comment': 'HCAN0 Message data 5 6',
    },
    0xFFFFE4DE: {
        'name': 'HCAN0_MD5_7',
        'size': 1,
        'comment': 'HCAN0 Message data 5 7',
    },
    0xFFFFE4DF: {
        'name': 'HCAN0_MD5_8',
        'size': 1,
        'comment': 'HCAN0 Message data 5 8',
    },
    0xFFFFE4E0: {
        'name': 'HCAN0_MD6_1',
        'size': 1,
        'comment': 'HCAN0 Message data 6 1',
    },
    0xFFFFE4E1: {
        'name': 'HCAN0_MD6_2',
        'size': 1,
        'comment': 'HCAN0 Message data 6 2',
    },
    0xFFFFE4E2: {
        'name': 'HCAN0_MD6_3',
        'size': 1,
        'comment': 'HCAN0 Message data 6 3',
    },
    0xFFFFE4E3: {
        'name': 'HCAN0_MD6_4',
        'size': 1,
        'comment': 'HCAN0 Message data 6 4',
    },
    0xFFFFE4E4: {
        'name': 'HCAN0_MD6_5',
        'size': 1,
        'comment': 'HCAN0 Message data 6 5',
    },
    0xFFFFE4E5: {
        'name': 'HCAN0_MD6_6',
        'size': 1,
        'comment': 'HCAN0 Message data 6 6',
    },
    0xFFFFE4E6: {
        'name': 'HCAN0_MD6_7',
        'size': 1,
        'comment': 'HCAN0 Message data 6 7',
    },
    0xFFFFE4E7: {
        'name': 'HCAN0_MD6_8',
        'size': 1,
        'comment': 'HCAN0 Message data 6 8',
    },
    0xFFFFE4E8: {
        'name': 'HCAN0_MD7_1',
        'size': 1,
        'comment': 'HCAN0 Message data 7 1',
    },
    0xFFFFE4E9: {
        'name': 'HCAN0_MD7_2',
        'size': 1,
        'comment': 'HCAN0 Message data 7 2',
    },
    0xFFFFE4EA: {
        'name': 'HCAN0_MD7_3',
        'size': 1,
        'comment': 'HCAN0 Message data 7 3',
    },
    0xFFFFE4EB: {
        'name': 'HCAN0_MD7_4',
        'size': 1,
        'comment': 'HCAN0 Message data 7 4',
    },
    0xFFFFE4EC: {
        'name': 'HCAN0_MD7_5',
        'size': 1,
        'comment': 'HCAN0 Message data 7 5',
    },
    0xFFFFE4ED: {
        'name': 'HCAN0_MD7_6',
        'size': 1,
        'comment': 'HCAN0 Message data 7 6',
    },
    0xFFFFE4EE: {
        'name': 'HCAN0_MD7_7',
        'size': 1,
        'comment': 'HCAN0 Message data 7 7',
    },
    0xFFFFE4EF: {
        'name': 'HCAN0_MD7_8',
        'size': 1,
        'comment': 'HCAN0 Message data 7 8',
    },
    0xFFFFE4F0: {
        'name': 'HCAN0_MD8_1',
        'size': 1,
        'comment': 'HCAN0 Message data 8 1',
    },
    0xFFFFE4F1: {
        'name': 'HCAN0_MD8_2',
        'size': 1,
        'comment': 'HCAN0 Message data 8 2',
    },
    0xFFFFE4F2: {
        'name': 'HCAN0_MD8_3',
        'size': 1,
        'comment': 'HCAN0 Message data 8 3',
    },
    0xFFFFE4F3: {
        'name': 'HCAN0_MD8_4',
        'size': 1,
        'comment': 'HCAN0 Message data 8 4',
    },
    0xFFFFE4F4: {
        'name': 'HCAN0_MD8_5',
        'size': 1,
        'comment': 'HCAN0 Message data 8 5',
    },
    0xFFFFE4F5: {
        'name': 'HCAN0_MD8_6',
        'size': 1,
        'comment': 'HCAN0 Message data 8 6',
    },
    0xFFFFE4F6: {
        'name': 'HCAN0_MD8_7',
        'size': 1,
        'comment': 'HCAN0 Message data 8 7',
    },
    0xFFFFE4F7: {
        'name': 'HCAN0_MD8_8',
        'size': 1,
        'comment': 'HCAN0 Message data 8 8',
    },
    0xFFFFE4F8: {
        'name': 'HCAN0_MD9_1',
        'size': 1,
        'comment': 'HCAN0 Message data 9 1',
    },
    0xFFFFE4F9: {
        'name': 'HCAN0_MD9_2',
        'size': 1,
        'comment': 'HCAN0 Message data 9 2',
    },
    0xFFFFE4FA: {
        'name': 'HCAN0_MD9_3',
        'size': 1,
        'comment': 'HCAN0 Message data 9 3',
    },
    0xFFFFE4FB: {
        'name': 'HCAN0_MD9_4',
        'size': 1,
        'comment': 'HCAN0 Message data 9 4',
    },
    0xFFFFE4FC: {
        'name': 'HCAN0_MD9_5',
        'size': 1,
        'comment': 'HCAN0 Message data 9 5',
    },
    0xFFFFE4FD: {
        'name': 'HCAN0_MD9_6',
        'size': 1,
        'comment': 'HCAN0 Message data 9 6',
    },
    0xFFFFE4FE: {
        'name': 'HCAN0_MD9_7',
        'size': 1,
        'comment': 'HCAN0 Message data 9 7',
    },
    0xFFFFE4FF: {
        'name': 'HCAN0_MD9_8',
        'size': 1,
        'comment': 'HCAN0 Message data 9 8',
    },
    0xFFFFE500: {
        'name': 'HCAN0_MD10_1',
        'size': 1,
        'comment': 'HCAN0 Message data 10 1',
    },
    0xFFFFE501: {
        'name': 'HCAN0_MD10_2',
        'size': 1,
        'comment': 'HCAN0 Message data 10 2',
    },
    0xFFFFE502: {
        'name': 'HCAN0_MD10_3',
        'size': 1,
        'comment': 'HCAN0 Message data 10 3',
    },
    0xFFFFE503: {
        'name': 'HCAN0_MD10_4',
        'size': 1,
        'comment': 'HCAN0 Message data 10 4',
    },
    0xFFFFE504: {
        'name': 'HCAN0_MD10_5',
        'size': 1,
        'comment': 'HCAN0 Message data 10 5',
    },
    0xFFFFE505: {
        'name': 'HCAN0_MD10_6',
        'size': 1,
        'comment': 'HCAN0 Message data 10 6',
    },
    0xFFFFE506: {
        'name': 'HCAN0_MD10_7',
        'size': 1,
        'comment': 'HCAN0 Message data 10 7',
    },
    0xFFFFE507: {
        'name': 'HCAN0_MD10_8',
        'size': 1,
        'comment': 'HCAN0 Message data 10 8',
    },
    0xFFFFE508: {
        'name': 'HCAN0_MD11_1',
        'size': 1,
        'comment': 'HCAN0 Message data 11 1',
    },
    0xFFFFE509: {
        'name': 'HCAN0_MD11_2',
        'size': 1,
        'comment': 'HCAN0 Message data 11 2',
    },
    0xFFFFE50A: {
        'name': 'HCAN0_MD11_3',
        'size': 1,
        'comment': 'HCAN0 Message data 11 3',
    },
    0xFFFFE50B: {
        'name': 'HCAN0_MD11_4',
        'size': 1,
        'comment': 'HCAN0 Message data 11 4',
    },
    0xFFFFE50C: {
        'name': 'HCAN0_MD11_5',
        'size': 1,
        'comment': 'HCAN0 Message data 11 5',
    },
    0xFFFFE50D: {
        'name': 'HCAN0_MD11_6',
        'size': 1,
        'comment': 'HCAN0 Message data 11 6',
    },
    0xFFFFE50E: {
        'name': 'HCAN0_MD11_7',
        'size': 1,
        'comment': 'HCAN0 Message data 11 7',
    },
    0xFFFFE50F: {
        'name': 'HCAN0_MD11_8',
        'size': 1,
        'comment': 'HCAN0 Message data 11 8',
    },
    0xFFFFE510: {
        'name': 'HCAN0_MD12_1',
        'size': 1,
        'comment': 'HCAN0 Message data 12 1',
    },
    0xFFFFE511: {
        'name': 'HCAN0_MD12_2',
        'size': 1,
        'comment': 'HCAN0 Message data 12 2',
    },
    0xFFFFE512: {
        'name': 'HCAN0_MD12_3',
        'size': 1,
        'comment': 'HCAN0 Message data 12 3',
    },
    0xFFFFE513: {
        'name': 'HCAN0_MD12_4',
        'size': 1,
        'comment': 'HCAN0 Message data 12 4',
    },
    0xFFFFE514: {
        'name': 'HCAN0_MD12_5',
        'size': 1,
        'comment': 'HCAN0 Message data 12 5',
    },
    0xFFFFE515: {
        'name': 'HCAN0_MD12_6',
        'size': 1,
        'comment': 'HCAN0 Message data 12 6',
    },
    0xFFFFE516: {
        'name': 'HCAN0_MD12_7',
        'size': 1,
        'comment': 'HCAN0 Message data 12 7',
    },
    0xFFFFE517: {
        'name': 'HCAN0_MD12_8',
        'size': 1,
        'comment': 'HCAN0 Message data 12 8',
    },
    0xFFFFE518: {
        'name': 'HCAN0_MD13_1',
        'size': 1,
        'comment': 'HCAN0 Message data 13 1',
    },
    0xFFFFE519: {
        'name': 'HCAN0_MD13_2',
        'size': 1,
        'comment': 'HCAN0 Message data 13 2',
    },
    0xFFFFE51A: {
        'name': 'HCAN0_MD13_3',
        'size': 1,
        'comment': 'HCAN0 Message data 13 3',
    },
    0xFFFFE51B: {
        'name': 'HCAN0_MD13_4',
        'size': 1,
        'comment': 'HCAN0 Message data 13 4',
    },
    0xFFFFE51C: {
        'name': 'HCAN0_MD13_5',
        'size': 1,
        'comment': 'HCAN0 Message data 13 5',
    },
    0xFFFFE51D: {
        'name': 'HCAN0_MD13_6',
        'size': 1,
        'comment': 'HCAN0 Message data 13 6',
    },
    0xFFFFE51E: {
        'name': 'HCAN0_MD13_7',
        'size': 1,
        'comment': 'HCAN0 Message data 13 7',
    },
    0xFFFFE51F: {
        'name': 'HCAN0_MD13_8',
        'size': 1,
        'comment': 'HCAN0 Message data 13 8',
    },
    0xFFFFE520: {
        'name': 'HCAN0_MD14_1',
        'size': 1,
        'comment': 'HCAN0 Message data 14 1',
    },
    0xFFFFE521: {
        'name': 'HCAN0_MD14_2',
        'size': 1,
        'comment': 'HCAN0 Message data 14 2',
    },
    0xFFFFE522: {
        'name': 'HCAN0_MD14_3',
        'size': 1,
        'comment': 'HCAN0 Message data 14 3',
    },
    0xFFFFE523: {
        'name': 'HCAN0_MD14_4',
        'size': 1,
        'comment': 'HCAN0 Message data 14 4',
    },
    0xFFFFE524: {
        'name': 'HCAN0_MD14_5',
        'size': 1,
        'comment': 'HCAN0 Message data 14 5',
    },
    0xFFFFE525: {
        'name': 'HCAN0_MD14_6',
        'size': 1,
        'comment': 'HCAN0 Message data 14 6',
    },
    0xFFFFE526: {
        'name': 'HCAN0_MD14_7',
        'size': 1,
        'comment': 'HCAN0 Message data 14 7',
    },
    0xFFFFE527: {
        'name': 'HCAN0_MD14_8',
        'size': 1,
        'comment': 'HCAN0 Message data 14 8',
    },
    0xFFFFE528: {
        'name': 'HCAN0_MD15_1',
        'size': 1,
        'comment': 'HCAN0 Message data 15 1',
    },
    0xFFFFE529: {
        'name': 'HCAN0_MD15_2',
        'size': 1,
        'comment': 'HCAN0 Message data 15 2',
    },
    0xFFFFE52A: {
        'name': 'HCAN0_MD15_3',
        'size': 1,
        'comment': 'HCAN0 Message data 15 3',
    },
    0xFFFFE52B: {
        'name': 'HCAN0_MD15_4',
        'size': 1,
        'comment': 'HCAN0 Message data 15 4',
    },
    0xFFFFE52C: {
        'name': 'HCAN0_MD15_5',
        'size': 1,
        'comment': 'HCAN0 Message data 15 5',
    },
    0xFFFFE52D: {
        'name': 'HCAN0_MD15_6',
        'size': 1,
        'comment': 'HCAN0 Message data 15 6',
    },
    0xFFFFE52E: {
        'name': 'HCAN0_MD15_7',
        'size': 1,
        'comment': 'HCAN0 Message data 15 7',
    },
    0xFFFFE52F: {
        'name': 'HCAN0_MD15_8',
        'size': 1,
        'comment': 'HCAN0 Message data 15 8',
    },
    0xFFFFE600: {
        'name': 'HCAN1_MCR',
        'size': 1,
        'comment': 'HCAN1 Master control register',
    },
    0xFFFFE601: {
        'name': 'HCAN1_GSR',
        'size': 1,
        'comment': 'HCAN1 General status register',
    },
    0xFFFFE602: {
        'name': 'HCAN1_BCR',
        'size': 2,
        'comment': 'HCAN1 Bit configuration register',
    },
    0xFFFFE604: {
        'name': 'HCAN1_MBCR',
        'size': 2,
        'comment': 'HCAN1 Mailbox configuration register',
    },
    0xFFFFE606: {
        'name': 'HCAN1_TXPR',
        'size': 2,
        'comment': 'HCAN1 Transmit wait register',
    },
    0xFFFFE608: {
        'name': 'HCAN1_TXCR',
        'size': 2,
        'comment': 'HCAN1 Transmit wait cancel register',
    },
    0xFFFFE60A: {
        'name': 'HCAN1_TXACK',
        'size': 2,
        'comment': 'HCAN1 Transmit acknowledge register',
    },
    0xFFFFE60C: {
        'name': 'HCAN1_ABACK',
        'size': 2,
        'comment': 'HCAN1 Abort acknowledge register',
    },
    0xFFFFE60E: {
        'name': 'HCAN1_RXPR',
        'size': 2,
        'comment': 'HCAN1 Receive complete register',
    },
    0xFFFFE610: {
        'name': 'HCAN1_RFPR',
        'size': 2,
        'comment': 'HCAN1 Remote request register',
    },
    0xFFFFE612: {
        'name': 'HCAN1_IRR',
        'size': 2,
        'comment': 'HCAN1 Interrupt register',
    },
    0xFFFFE614: {
        'name': 'HCAN1_MBIMR',
        'size': 2,
        'comment': 'HCAN1 Mailbox interrupt mask register',
    },
    0xFFFFE616: {
        'name': 'HCAN1_IMR',
        'size': 2,
        'comment': 'HCAN1 Interrupt mask register',
    },
    0xFFFFE618: {
        'name': 'HCAN1_REC',
        'size': 1,
        'comment': 'HCAN1 Receive error counter',
    },
    0xFFFFE619: {
        'name': 'HCAN1_TEC',
        'size': 1,
        'comment': 'HCAN1 Transmit error counter',
    },
    0xFFFFE61A: {
        'name': 'HCAN1_UMSR',
        'size': 2,
        'comment': 'HCAN1 Unread message status register',
    },
    0xFFFFE61C: {
        'name': 'HCAN1_LAFML',
        'size': 2,
        'comment': 'HCAN1 Local acceptance filter mask L',
    },
    0xFFFFE61E: {
        'name': 'HCAN1_LAFMH',
        'size': 2,
        'comment': 'HCAN1 Local acceptance filter mask H',
    },
    0xFFFFE620: {
        'name': 'HCAN1_MC0_1',
        'size': 1,
        'comment': 'HCAN1 Message control 0 1',
    },
    0xFFFFE621: {
        'name': 'HCAN1_MC0_2',
        'size': 1,
        'comment': 'HCAN1 Message control 0 2',
    },
    0xFFFFE622: {
        'name': 'HCAN1_MC0_3',
        'size': 1,
        'comment': 'HCAN1 Message control 0 3',
    },
    0xFFFFE623: {
        'name': 'HCAN1_MC0_4',
        'size': 1,
        'comment': 'HCAN1 Message control 0 4',
    },
    0xFFFFE624: {
        'name': 'HCAN1_MC0_5',
        'size': 1,
        'comment': 'HCAN1 Message control 0 5',
    },
    0xFFFFE625: {
        'name': 'HCAN1_MC0_6',
        'size': 1,
        'comment': 'HCAN1 Message control 0 6',
    },
    0xFFFFE626: {
        'name': 'HCAN1_MC0_7',
        'size': 1,
        'comment': 'HCAN1 Message control 0 7',
    },
    0xFFFFE627: {
        'name': 'HCAN1_MC0_8',
        'size': 1,
        'comment': 'HCAN1 Message control 0 8',
    },
    0xFFFFE628: {
        'name': 'HCAN1_MC1_1',
        'size': 1,
        'comment': 'HCAN1 Message control 1 1',
    },
    0xFFFFE629: {
        'name': 'HCAN1_MC1_2',
        'size': 1,
        'comment': 'HCAN1 Message control 1 2',
    },
    0xFFFFE62A: {
        'name': 'HCAN1_MC1_3',
        'size': 1,
        'comment': 'HCAN1 Message control 1 3',
    },
    0xFFFFE62B: {
        'name': 'HCAN1_MC1_4',
        'size': 1,
        'comment': 'HCAN1 Message control 1 4',
    },
    0xFFFFE62C: {
        'name': 'HCAN1_MC1_5',
        'size': 1,
        'comment': 'HCAN1 Message control 1 5',
    },
    0xFFFFE62D: {
        'name': 'HCAN1_MC1_6',
        'size': 1,
        'comment': 'HCAN1 Message control 1 6',
    },
    0xFFFFE62E: {
        'name': 'HCAN1_MC1_7',
        'size': 1,
        'comment': 'HCAN1 Message control 1 7',
    },
    0xFFFFE62F: {
        'name': 'HCAN1_MC1_8',
        'size': 1,
        'comment': 'HCAN1 Message control 1 8',
    },
    0xFFFFE630: {
        'name': 'HCAN1_MC2_1',
        'size': 1,
        'comment': 'HCAN1 Message control 2 1',
    },
    0xFFFFE631: {
        'name': 'HCAN1_MC2_2',
        'size': 1,
        'comment': 'HCAN1 Message control 2 2',
    },
    0xFFFFE632: {
        'name': 'HCAN1_MC2_3',
        'size': 1,
        'comment': 'HCAN1 Message control 2 3',
    },
    0xFFFFE633: {
        'name': 'HCAN1_MC2_4',
        'size': 1,
        'comment': 'HCAN1 Message control 2 4',
    },
    0xFFFFE634: {
        'name': 'HCAN1_MC2_5',
        'size': 1,
        'comment': 'HCAN1 Message control 2 5',
    },
    0xFFFFE635: {
        'name': 'HCAN1_MC2_6',
        'size': 1,
        'comment': 'HCAN1 Message control 2 6',
    },
    0xFFFFE636: {
        'name': 'HCAN1_MC2_7',
        'size': 1,
        'comment': 'HCAN1 Message control 2 7',
    },
    0xFFFFE637: {
        'name': 'HCAN1_MC2_8',
        'size': 1,
        'comment': 'HCAN1 Message control 2 8',
    },
    0xFFFFE638: {
        'name': 'HCAN1_MC3_1',
        'size': 1,
        'comment': 'HCAN1 Message control 3 1',
    },
    0xFFFFE639: {
        'name': 'HCAN1_MC3_2',
        'size': 1,
        'comment': 'HCAN1 Message control 3 2',
    },
    0xFFFFE63A: {
        'name': 'HCAN1_MC3_3',
        'size': 1,
        'comment': 'HCAN1 Message control 3 3',
    },
    0xFFFFE63B: {
        'name': 'HCAN1_MC3_4',
        'size': 1,
        'comment': 'HCAN1 Message control 3 4',
    },
    0xFFFFE63C: {
        'name': 'HCAN1_MC3_5',
        'size': 1,
        'comment': 'HCAN1 Message control 3 5',
    },
    0xFFFFE63D: {
        'name': 'HCAN1_MC3_6',
        'size': 1,
        'comment': 'HCAN1 Message control 3 6',
    },
    0xFFFFE63E: {
        'name': 'HCAN1_MC3_7',
        'size': 1,
        'comment': 'HCAN1 Message control 3 7',
    },
    0xFFFFE63F: {
        'name': 'HCAN1_MC3_8',
        'size': 1,
        'comment': 'HCAN1 Message control 3 8',
    },
    0xFFFFE640: {
        'name': 'HCAN1_MC4_1',
        'size': 1,
        'comment': 'HCAN1 Message control 4 1',
    },
    0xFFFFE641: {
        'name': 'HCAN1_MC4_2',
        'size': 1,
        'comment': 'HCAN1 Message control 4 2',
    },
    0xFFFFE642: {
        'name': 'HCAN1_MC4_3',
        'size': 1,
        'comment': 'HCAN1 Message control 4 3',
    },
    0xFFFFE643: {
        'name': 'HCAN1_MC4_4',
        'size': 1,
        'comment': 'HCAN1 Message control 4 4',
    },
    0xFFFFE644: {
        'name': 'HCAN1_MC4_5',
        'size': 1,
        'comment': 'HCAN1 Message control 4 5',
    },
    0xFFFFE645: {
        'name': 'HCAN1_MC4_6',
        'size': 1,
        'comment': 'HCAN1 Message control 4 6',
    },
    0xFFFFE646: {
        'name': 'HCAN1_MC4_7',
        'size': 1,
        'comment': 'HCAN1 Message control 4 7',
    },
    0xFFFFE647: {
        'name': 'HCAN1_MC4_8',
        'size': 1,
        'comment': 'HCAN1 Message control 4 8',
    },
    0xFFFFE648: {
        'name': 'HCAN1_MC5_1',
        'size': 1,
        'comment': 'HCAN1 Message control 5 1',
    },
    0xFFFFE649: {
        'name': 'HCAN1_MC5_2',
        'size': 1,
        'comment': 'HCAN1 Message control 5 2',
    },
    0xFFFFE64A: {
        'name': 'HCAN1_MC5_3',
        'size': 1,
        'comment': 'HCAN1 Message control 5 3',
    },
    0xFFFFE64B: {
        'name': 'HCAN1_MC5_4',
        'size': 1,
        'comment': 'HCAN1 Message control 5 4',
    },
    0xFFFFE64C: {
        'name': 'HCAN1_MC5_5',
        'size': 1,
        'comment': 'HCAN1 Message control 5 5',
    },
    0xFFFFE64D: {
        'name': 'HCAN1_MC5_6',
        'size': 1,
        'comment': 'HCAN1 Message control 5 6',
    },
    0xFFFFE64E: {
        'name': 'HCAN1_MC5_7',
        'size': 1,
        'comment': 'HCAN1 Message control 5 7',
    },
    0xFFFFE64F: {
        'name': 'HCAN1_MC5_8',
        'size': 1,
        'comment': 'HCAN1 Message control 5 8',
    },
    0xFFFFE650: {
        'name': 'HCAN1_MC6_1',
        'size': 1,
        'comment': 'HCAN1 Message control 6 1',
    },
    0xFFFFE651: {
        'name': 'HCAN1_MC6_2',
        'size': 1,
        'comment': 'HCAN1 Message control 6 2',
    },
    0xFFFFE652: {
        'name': 'HCAN1_MC6_3',
        'size': 1,
        'comment': 'HCAN1 Message control 6 3',
    },
    0xFFFFE653: {
        'name': 'HCAN1_MC6_4',
        'size': 1,
        'comment': 'HCAN1 Message control 6 4',
    },
    0xFFFFE654: {
        'name': 'HCAN1_MC6_5',
        'size': 1,
        'comment': 'HCAN1 Message control 6 5',
    },
    0xFFFFE655: {
        'name': 'HCAN1_MC6_6',
        'size': 1,
        'comment': 'HCAN1 Message control 6 6',
    },
    0xFFFFE656: {
        'name': 'HCAN1_MC6_7',
        'size': 1,
        'comment': 'HCAN1 Message control 6 7',
    },
    0xFFFFE657: {
        'name': 'HCAN1_MC6_8',
        'size': 1,
        'comment': 'HCAN1 Message control 6 8',
    },
    0xFFFFE658: {
        'name': 'HCAN1_MC7_1',
        'size': 1,
        'comment': 'HCAN1 Message control 7 1',
    },
    0xFFFFE659: {
        'name': 'HCAN1_MC7_2',
        'size': 1,
        'comment': 'HCAN1 Message control 7 2',
    },
    0xFFFFE65A: {
        'name': 'HCAN1_MC7_3',
        'size': 1,
        'comment': 'HCAN1 Message control 7 3',
    },
    0xFFFFE65B: {
        'name': 'HCAN1_MC7_4',
        'size': 1,
        'comment': 'HCAN1 Message control 7 4',
    },
    0xFFFFE65C: {
        'name': 'HCAN1_MC7_5',
        'size': 1,
        'comment': 'HCAN1 Message control 7 5',
    },
    0xFFFFE65D: {
        'name': 'HCAN1_MC7_6',
        'size': 1,
        'comment': 'HCAN1 Message control 7 6',
    },
    0xFFFFE65E: {
        'name': 'HCAN1_MC7_7',
        'size': 1,
        'comment': 'HCAN1 Message control 7 7',
    },
    0xFFFFE65F: {
        'name': 'HCAN1_MC7_8',
        'size': 1,
        'comment': 'HCAN1 Message control 7 8',
    },
    0xFFFFE660: {
        'name': 'HCAN1_MC8_1',
        'size': 1,
        'comment': 'HCAN1 Message control 8 1',
    },
    0xFFFFE661: {
        'name': 'HCAN1_MC8_2',
        'size': 1,
        'comment': 'HCAN1 Message control 8 2',
    },
    0xFFFFE662: {
        'name': 'HCAN1_MC8_3',
        'size': 1,
        'comment': 'HCAN1 Message control 8 3',
    },
    0xFFFFE663: {
        'name': 'HCAN1_MC8_4',
        'size': 1,
        'comment': 'HCAN1 Message control 8 4',
    },
    0xFFFFE664: {
        'name': 'HCAN1_MC8_5',
        'size': 1,
        'comment': 'HCAN1 Message control 8 5',
    },
    0xFFFFE665: {
        'name': 'HCAN1_MC8_6',
        'size': 1,
        'comment': 'HCAN1 Message control 8 6',
    },
    0xFFFFE666: {
        'name': 'HCAN1_MC8_7',
        'size': 1,
        'comment': 'HCAN1 Message control 8 7',
    },
    0xFFFFE667: {
        'name': 'HCAN1_MC8_8',
        'size': 1,
        'comment': 'HCAN1 Message control 8 8',
    },
    0xFFFFE668: {
        'name': 'HCAN1_MC9_1',
        'size': 1,
        'comment': 'HCAN1 Message control 9 1',
    },
    0xFFFFE669: {
        'name': 'HCAN1_MC9_2',
        'size': 1,
        'comment': 'HCAN1 Message control 9 2',
    },
    0xFFFFE66A: {
        'name': 'HCAN1_MC9_3',
        'size': 1,
        'comment': 'HCAN1 Message control 9 3',
    },
    0xFFFFE66B: {
        'name': 'HCAN1_MC9_4',
        'size': 1,
        'comment': 'HCAN1 Message control 9 4',
    },
    0xFFFFE66C: {
        'name': 'HCAN1_MC9_5',
        'size': 1,
        'comment': 'HCAN1 Message control 9 5',
    },
    0xFFFFE66D: {
        'name': 'HCAN1_MC9_6',
        'size': 1,
        'comment': 'HCAN1 Message control 9 6',
    },
    0xFFFFE66E: {
        'name': 'HCAN1_MC9_7',
        'size': 1,
        'comment': 'HCAN1 Message control 9 7',
    },
    0xFFFFE66F: {
        'name': 'HCAN1_MC9_8',
        'size': 1,
        'comment': 'HCAN1 Message control 9 8',
    },
    0xFFFFE670: {
        'name': 'HCAN1_MC10_1',
        'size': 1,
        'comment': 'HCAN1 Message control 10 1',
    },
    0xFFFFE671: {
        'name': 'HCAN1_MC10_2',
        'size': 1,
        'comment': 'HCAN1 Message control 10 2',
    },
    0xFFFFE672: {
        'name': 'HCAN1_MC10_3',
        'size': 1,
        'comment': 'HCAN1 Message control 10 3',
    },
    0xFFFFE673: {
        'name': 'HCAN1_MC10_4',
        'size': 1,
        'comment': 'HCAN1 Message control 10 4',
    },
    0xFFFFE674: {
        'name': 'HCAN1_MC10_5',
        'size': 1,
        'comment': 'HCAN1 Message control 10 5',
    },
    0xFFFFE675: {
        'name': 'HCAN1_MC10_6',
        'size': 1,
        'comment': 'HCAN1 Message control 10 6',
    },
    0xFFFFE676: {
        'name': 'HCAN1_MC10_7',
        'size': 1,
        'comment': 'HCAN1 Message control 10 7',
    },
    0xFFFFE677: {
        'name': 'HCAN1_MC10_8',
        'size': 1,
        'comment': 'HCAN1 Message control 10 8',
    },
    0xFFFFE678: {
        'name': 'HCAN1_MC11_1',
        'size': 1,
        'comment': 'HCAN1 Message control 11 1',
    },
    0xFFFFE679: {
        'name': 'HCAN1_MC11_2',
        'size': 1,
        'comment': 'HCAN1 Message control 11 2',
    },
    0xFFFFE67A: {
        'name': 'HCAN1_MC11_3',
        'size': 1,
        'comment': 'HCAN1 Message control 11 3',
    },
    0xFFFFE67B: {
        'name': 'HCAN1_MC11_4',
        'size': 1,
        'comment': 'HCAN1 Message control 11 4',
    },
    0xFFFFE67C: {
        'name': 'HCAN1_MC11_5',
        'size': 1,
        'comment': 'HCAN1 Message control 11 5',
    },
    0xFFFFE67D: {
        'name': 'HCAN1_MC11_6',
        'size': 1,
        'comment': 'HCAN1 Message control 11 6',
    },
    0xFFFFE67E: {
        'name': 'HCAN1_MC11_7',
        'size': 1,
        'comment': 'HCAN1 Message control 11 7',
    },
    0xFFFFE67F: {
        'name': 'HCAN1_MC11_8',
        'size': 1,
        'comment': 'HCAN1 Message control 11 8',
    },
    0xFFFFE680: {
        'name': 'HCAN1_MC12_1',
        'size': 1,
        'comment': 'HCAN1 Message control 12 1',
    },
    0xFFFFE681: {
        'name': 'HCAN1_MC12_2',
        'size': 1,
        'comment': 'HCAN1 Message control 12 2',
    },
    0xFFFFE682: {
        'name': 'HCAN1_MC12_3',
        'size': 1,
        'comment': 'HCAN1 Message control 12 3',
    },
    0xFFFFE683: {
        'name': 'HCAN1_MC12_4',
        'size': 1,
        'comment': 'HCAN1 Message control 12 4',
    },
    0xFFFFE684: {
        'name': 'HCAN1_MC12_5',
        'size': 1,
        'comment': 'HCAN1 Message control 12 5',
    },
    0xFFFFE685: {
        'name': 'HCAN1_MC12_6',
        'size': 1,
        'comment': 'HCAN1 Message control 12 6',
    },
    0xFFFFE686: {
        'name': 'HCAN1_MC12_7',
        'size': 1,
        'comment': 'HCAN1 Message control 12 7',
    },
    0xFFFFE687: {
        'name': 'HCAN1_MC12_8',
        'size': 1,
        'comment': 'HCAN1 Message control 12 8',
    },
    0xFFFFE688: {
        'name': 'HCAN1_MC13_1',
        'size': 1,
        'comment': 'HCAN1 Message control 13 1',
    },
    0xFFFFE689: {
        'name': 'HCAN1_MC13_2',
        'size': 1,
        'comment': 'HCAN1 Message control 13 2',
    },
    0xFFFFE68A: {
        'name': 'HCAN1_MC13_3',
        'size': 1,
        'comment': 'HCAN1 Message control 13 3',
    },
    0xFFFFE68B: {
        'name': 'HCAN1_MC13_4',
        'size': 1,
        'comment': 'HCAN1 Message control 13 4',
    },
    0xFFFFE68C: {
        'name': 'HCAN1_MC13_5',
        'size': 1,
        'comment': 'HCAN1 Message control 13 5',
    },
    0xFFFFE68D: {
        'name': 'HCAN1_MC13_6',
        'size': 1,
        'comment': 'HCAN1 Message control 13 6',
    },
    0xFFFFE68E: {
        'name': 'HCAN1_MC13_7',
        'size': 1,
        'comment': 'HCAN1 Message control 13 7',
    },
    0xFFFFE68F: {
        'name': 'HCAN1_MC13_8',
        'size': 1,
        'comment': 'HCAN1 Message control 13 8',
    },
    0xFFFFE690: {
        'name': 'HCAN1_MC14_1',
        'size': 1,
        'comment': 'HCAN1 Message control 14 1',
    },
    0xFFFFE691: {
        'name': 'HCAN1_MC14_2',
        'size': 1,
        'comment': 'HCAN1 Message control 14 2',
    },
    0xFFFFE692: {
        'name': 'HCAN1_MC14_3',
        'size': 1,
        'comment': 'HCAN1 Message control 14 3',
    },
    0xFFFFE693: {
        'name': 'HCAN1_MC14_4',
        'size': 1,
        'comment': 'HCAN1 Message control 14 4',
    },
    0xFFFFE694: {
        'name': 'HCAN1_MC14_5',
        'size': 1,
        'comment': 'HCAN1 Message control 14 5',
    },
    0xFFFFE695: {
        'name': 'HCAN1_MC14_6',
        'size': 1,
        'comment': 'HCAN1 Message control 14 6',
    },
    0xFFFFE696: {
        'name': 'HCAN1_MC14_7',
        'size': 1,
        'comment': 'HCAN1 Message control 14 7',
    },
    0xFFFFE697: {
        'name': 'HCAN1_MC14_8',
        'size': 1,
        'comment': 'HCAN1 Message control 14 8',
    },
    0xFFFFE698: {
        'name': 'HCAN1_MC15_1',
        'size': 1,
        'comment': 'HCAN1 Message control 15 1',
    },
    0xFFFFE699: {
        'name': 'HCAN1_MC15_2',
        'size': 1,
        'comment': 'HCAN1 Message control 15 2',
    },
    0xFFFFE69A: {
        'name': 'HCAN1_MC15_3',
        'size': 1,
        'comment': 'HCAN1 Message control 15 3',
    },
    0xFFFFE69B: {
        'name': 'HCAN1_MC15_4',
        'size': 1,
        'comment': 'HCAN1 Message control 15 4',
    },
    0xFFFFE69C: {
        'name': 'HCAN1_MC15_5',
        'size': 1,
        'comment': 'HCAN1 Message control 15 5',
    },
    0xFFFFE69D: {
        'name': 'HCAN1_MC15_6',
        'size': 1,
        'comment': 'HCAN1 Message control 15 6',
    },
    0xFFFFE69E: {
        'name': 'HCAN1_MC15_7',
        'size': 1,
        'comment': 'HCAN1 Message control 15 7',
    },
    0xFFFFE69F: {
        'name': 'HCAN1_MC15_8',
        'size': 1,
        'comment': 'HCAN1 Message control 15 8',
    },
    0xFFFFE6B0: {
        'name': 'HCAN1_MD0_1',
        'size': 1,
        'comment': 'HCAN1 Message data 0 1',
    },
    0xFFFFE6B1: {
        'name': 'HCAN1_MD0_2',
        'size': 1,
        'comment': 'HCAN1 Message data 0 2',
    },
    0xFFFFE6B2: {
        'name': 'HCAN1_MD0_3',
        'size': 1,
        'comment': 'HCAN1 Message data 0 3',
    },
    0xFFFFE6B3: {
        'name': 'HCAN1_MD0_4',
        'size': 1,
        'comment': 'HCAN1 Message data 0 4',
    },
    0xFFFFE6B4: {
        'name': 'HCAN1_MD0_5',
        'size': 1,
        'comment': 'HCAN1 Message data 0 5',
    },
    0xFFFFE6B5: {
        'name': 'HCAN1_MD0_6',
        'size': 1,
        'comment': 'HCAN1 Message data 0 6',
    },
    0xFFFFE6B6: {
        'name': 'HCAN1_MD0_7',
        'size': 1,
        'comment': 'HCAN1 Message data 0 7',
    },
    0xFFFFE6B7: {
        'name': 'HCAN1_MD0_8',
        'size': 1,
        'comment': 'HCAN1 Message data 0 8',
    },
    0xFFFFE6B8: {
        'name': 'HCAN1_MD1_1',
        'size': 1,
        'comment': 'HCAN1 Message data 1 1',
    },
    0xFFFFE6B9: {
        'name': 'HCAN1_MD1_2',
        'size': 1,
        'comment': 'HCAN1 Message data 1 2',
    },
    0xFFFFE6BA: {
        'name': 'HCAN1_MD1_3',
        'size': 1,
        'comment': 'HCAN1 Message data 1 3',
    },
    0xFFFFE6BB: {
        'name': 'HCAN1_MD1_4',
        'size': 1,
        'comment': 'HCAN1 Message data 1 4',
    },
    0xFFFFE6BC: {
        'name': 'HCAN1_MD1_5',
        'size': 1,
        'comment': 'HCAN1 Message data 1 5',
    },
    0xFFFFE6BD: {
        'name': 'HCAN1_MD1_6',
        'size': 1,
        'comment': 'HCAN1 Message data 1 6',
    },
    0xFFFFE6BE: {
        'name': 'HCAN1_MD1_7',
        'size': 1,
        'comment': 'HCAN1 Message data 1 7',
    },
    0xFFFFE6BF: {
        'name': 'HCAN1_MD1_8',
        'size': 1,
        'comment': 'HCAN1 Message data 1 8',
    },
    0xFFFFE6C0: {
        'name': 'HCAN1_MD2_1',
        'size': 1,
        'comment': 'HCAN1 Message data 2 1',
    },
    0xFFFFE6C1: {
        'name': 'HCAN1_MD2_2',
        'size': 1,
        'comment': 'HCAN1 Message data 2 2',
    },
    0xFFFFE6C2: {
        'name': 'HCAN1_MD2_3',
        'size': 1,
        'comment': 'HCAN1 Message data 2 3',
    },
    0xFFFFE6C3: {
        'name': 'HCAN1_MD2_4',
        'size': 1,
        'comment': 'HCAN1 Message data 2 4',
    },
    0xFFFFE6C4: {
        'name': 'HCAN1_MD2_5',
        'size': 1,
        'comment': 'HCAN1 Message data 2 5',
    },
    0xFFFFE6C5: {
        'name': 'HCAN1_MD2_6',
        'size': 1,
        'comment': 'HCAN1 Message data 2 6',
    },
    0xFFFFE6C6: {
        'name': 'HCAN1_MD2_7',
        'size': 1,
        'comment': 'HCAN1 Message data 2 7',
    },
    0xFFFFE6C7: {
        'name': 'HCAN1_MD2_8',
        'size': 1,
        'comment': 'HCAN1 Message data 2 8',
    },
    0xFFFFE6C8: {
        'name': 'HCAN1_MD3_1',
        'size': 1,
        'comment': 'HCAN1 Message data 3 1',
    },
    0xFFFFE6C9: {
        'name': 'HCAN1_MD3_2',
        'size': 1,
        'comment': 'HCAN1 Message data 3 2',
    },
    0xFFFFE6CA: {
        'name': 'HCAN1_MD3_3',
        'size': 1,
        'comment': 'HCAN1 Message data 3 3',
    },
    0xFFFFE6CB: {
        'name': 'HCAN1_MD3_4',
        'size': 1,
        'comment': 'HCAN1 Message data 3 4',
    },
    0xFFFFE6CC: {
        'name': 'HCAN1_MD3_5',
        'size': 1,
        'comment': 'HCAN1 Message data 3 5',
    },
    0xFFFFE6CD: {
        'name': 'HCAN1_MD3_6',
        'size': 1,
        'comment': 'HCAN1 Message data 3 6',
    },
    0xFFFFE6CE: {
        'name': 'HCAN1_MD3_7',
        'size': 1,
        'comment': 'HCAN1 Message data 3 7',
    },
    0xFFFFE6CF: {
        'name': 'HCAN1_MD3_8',
        'size': 1,
        'comment': 'HCAN1 Message data 3 8',
    },
    0xFFFFE6D0: {
        'name': 'HCAN1_MD4_1',
        'size': 1,
        'comment': 'HCAN1 Message data 4 1',
    },
    0xFFFFE6D1: {
        'name': 'HCAN1_MD4_2',
        'size': 1,
        'comment': 'HCAN1 Message data 4 2',
    },
    0xFFFFE6D2: {
        'name': 'HCAN1_MD4_3',
        'size': 1,
        'comment': 'HCAN1 Message data 4 3',
    },
    0xFFFFE6D3: {
        'name': 'HCAN1_MD4_4',
        'size': 1,
        'comment': 'HCAN1 Message data 4 4',
    },
    0xFFFFE6D4: {
        'name': 'HCAN1_MD4_5',
        'size': 1,
        'comment': 'HCAN1 Message data 4 5',
    },
    0xFFFFE6D5: {
        'name': 'HCAN1_MD4_6',
        'size': 1,
        'comment': 'HCAN1 Message data 4 6',
    },
    0xFFFFE6D6: {
        'name': 'HCAN1_MD4_7',
        'size': 1,
        'comment': 'HCAN1 Message data 4 7',
    },
    0xFFFFE6D7: {
        'name': 'HCAN1_MD4_8',
        'size': 1,
        'comment': 'HCAN1 Message data 4 8',
    },
    0xFFFFE6D8: {
        'name': 'HCAN1_MD5_1',
        'size': 1,
        'comment': 'HCAN1 Message data 5 1',
    },
    0xFFFFE6D9: {
        'name': 'HCAN1_MD5_2',
        'size': 1,
        'comment': 'HCAN1 Message data 5 2',
    },
    0xFFFFE6DA: {
        'name': 'HCAN1_MD5_3',
        'size': 1,
        'comment': 'HCAN1 Message data 5 3',
    },
    0xFFFFE6DB: {
        'name': 'HCAN1_MD5_4',
        'size': 1,
        'comment': 'HCAN1 Message data 5 4',
    },
    0xFFFFE6DC: {
        'name': 'HCAN1_MD5_5',
        'size': 1,
        'comment': 'HCAN1 Message data 5 5',
    },
    0xFFFFE6DD: {
        'name': 'HCAN1_MD5_6',
        'size': 1,
        'comment': 'HCAN1 Message data 5 6',
    },
    0xFFFFE6DE: {
        'name': 'HCAN1_MD5_7',
        'size': 1,
        'comment': 'HCAN1 Message data 5 7',
    },
    0xFFFFE6DF: {
        'name': 'HCAN1_MD5_8',
        'size': 1,
        'comment': 'HCAN1 Message data 5 8',
    },
    0xFFFFE6E0: {
        'name': 'HCAN1_MD6_1',
        'size': 1,
        'comment': 'HCAN1 Message data 6 1',
    },
    0xFFFFE6E1: {
        'name': 'HCAN1_MD6_2',
        'size': 1,
        'comment': 'HCAN1 Message data 6 2',
    },
    0xFFFFE6E2: {
        'name': 'HCAN1_MD6_3',
        'size': 1,
        'comment': 'HCAN1 Message data 6 3',
    },
    0xFFFFE6E3: {
        'name': 'HCAN1_MD6_4',
        'size': 1,
        'comment': 'HCAN1 Message data 6 4',
    },
    0xFFFFE6E4: {
        'name': 'HCAN1_MD6_5',
        'size': 1,
        'comment': 'HCAN1 Message data 6 5',
    },
    0xFFFFE6E5: {
        'name': 'HCAN1_MD6_6',
        'size': 1,
        'comment': 'HCAN1 Message data 6 6',
    },
    0xFFFFE6E6: {
        'name': 'HCAN1_MD6_7',
        'size': 1,
        'comment': 'HCAN1 Message data 6 7',
    },
    0xFFFFE6E7: {
        'name': 'HCAN1_MD6_8',
        'size': 1,
        'comment': 'HCAN1 Message data 6 8',
    },
    0xFFFFE6E8: {
        'name': 'HCAN1_MD7_1',
        'size': 1,
        'comment': 'HCAN1 Message data 7 1',
    },
    0xFFFFE6E9: {
        'name': 'HCAN1_MD7_2',
        'size': 1,
        'comment': 'HCAN1 Message data 7 2',
    },
    0xFFFFE6EA: {
        'name': 'HCAN1_MD7_3',
        'size': 1,
        'comment': 'HCAN1 Message data 7 3',
    },
    0xFFFFE6EB: {
        'name': 'HCAN1_MD7_4',
        'size': 1,
        'comment': 'HCAN1 Message data 7 4',
    },
    0xFFFFE6EC: {
        'name': 'HCAN1_MD7_5',
        'size': 1,
        'comment': 'HCAN1 Message data 7 5',
    },
    0xFFFFE6ED: {
        'name': 'HCAN1_MD7_6',
        'size': 1,
        'comment': 'HCAN1 Message data 7 6',
    },
    0xFFFFE6EE: {
        'name': 'HCAN1_MD7_7',
        'size': 1,
        'comment': 'HCAN1 Message data 7 7',
    },
    0xFFFFE6EF: {
        'name': 'HCAN1_MD7_8',
        'size': 1,
        'comment': 'HCAN1 Message data 7 8',
    },
    0xFFFFE6F0: {
        'name': 'HCAN1_MD8_1',
        'size': 1,
        'comment': 'HCAN1 Message data 8 1',
    },
    0xFFFFE6F1: {
        'name': 'HCAN1_MD8_2',
        'size': 1,
        'comment': 'HCAN1 Message data 8 2',
    },
    0xFFFFE6F2: {
        'name': 'HCAN1_MD8_3',
        'size': 1,
        'comment': 'HCAN1 Message data 8 3',
    },
    0xFFFFE6F3: {
        'name': 'HCAN1_MD8_4',
        'size': 1,
        'comment': 'HCAN1 Message data 8 4',
    },
    0xFFFFE6F4: {
        'name': 'HCAN1_MD8_5',
        'size': 1,
        'comment': 'HCAN1 Message data 8 5',
    },
    0xFFFFE6F5: {
        'name': 'HCAN1_MD8_6',
        'size': 1,
        'comment': 'HCAN1 Message data 8 6',
    },
    0xFFFFE6F6: {
        'name': 'HCAN1_MD8_7',
        'size': 1,
        'comment': 'HCAN1 Message data 8 7',
    },
    0xFFFFE6F7: {
        'name': 'HCAN1_MD8_8',
        'size': 1,
        'comment': 'HCAN1 Message data 8 8',
    },
    0xFFFFE6F8: {
        'name': 'HCAN1_MD9_1',
        'size': 1,
        'comment': 'HCAN1 Message data 9 1',
    },
    0xFFFFE6F9: {
        'name': 'HCAN1_MD9_2',
        'size': 1,
        'comment': 'HCAN1 Message data 9 2',
    },
    0xFFFFE6FA: {
        'name': 'HCAN1_MD9_3',
        'size': 1,
        'comment': 'HCAN1 Message data 9 3',
    },
    0xFFFFE6FB: {
        'name': 'HCAN1_MD9_4',
        'size': 1,
        'comment': 'HCAN1 Message data 9 4',
    },
    0xFFFFE6FC: {
        'name': 'HCAN1_MD9_5',
        'size': 1,
        'comment': 'HCAN1 Message data 9 5',
    },
    0xFFFFE6FD: {
        'name': 'HCAN1_MD9_6',
        'size': 1,
        'comment': 'HCAN1 Message data 9 6',
    },
    0xFFFFE6FE: {
        'name': 'HCAN1_MD9_7',
        'size': 1,
        'comment': 'HCAN1 Message data 9 7',
    },
    0xFFFFE6FF: {
        'name': 'HCAN1_MD9_8',
        'size': 1,
        'comment': 'HCAN1 Message data 9 8',
    },
    0xFFFFE700: {
        'name': 'HCAN1_MD10_1',
        'size': 1,
        'comment': 'HCAN1 Message data 10 1',
    },
    0xFFFFE701: {
        'name': 'HCAN1_MD10_2',
        'size': 1,
        'comment': 'HCAN1 Message data 10 2',
    },
    0xFFFFE702: {
        'name': 'HCAN1_MD10_3',
        'size': 1,
        'comment': 'HCAN1 Message data 10 3',
    },
    0xFFFFE703: {
        'name': 'HCAN1_MD10_4',
        'size': 1,
        'comment': 'HCAN1 Message data 10 4',
    },
    0xFFFFE704: {
        'name': 'HCAN1_MD10_5',
        'size': 1,
        'comment': 'HCAN1 Message data 10 5',
    },
    0xFFFFE705: {
        'name': 'HCAN1_MD10_6',
        'size': 1,
        'comment': 'HCAN1 Message data 10 6',
    },
    0xFFFFE706: {
        'name': 'HCAN1_MD10_7',
        'size': 1,
        'comment': 'HCAN1 Message data 10 7',
    },
    0xFFFFE707: {
        'name': 'HCAN1_MD10_8',
        'size': 1,
        'comment': 'HCAN1 Message data 10 8',
    },
    0xFFFFE708: {
        'name': 'HCAN1_MD11_1',
        'size': 1,
        'comment': 'HCAN1 Message data 11 1',
    },
    0xFFFFE709: {
        'name': 'HCAN1_MD11_2',
        'size': 1,
        'comment': 'HCAN1 Message data 11 2',
    },
    0xFFFFE70A: {
        'name': 'HCAN1_MD11_3',
        'size': 1,
        'comment': 'HCAN1 Message data 11 3',
    },
    0xFFFFE70B: {
        'name': 'HCAN1_MD11_4',
        'size': 1,
        'comment': 'HCAN1 Message data 11 4',
    },
    0xFFFFE70C: {
        'name': 'HCAN1_MD11_5',
        'size': 1,
        'comment': 'HCAN1 Message data 11 5',
    },
    0xFFFFE70D: {
        'name': 'HCAN1_MD11_6',
        'size': 1,
        'comment': 'HCAN1 Message data 11 6',
    },
    0xFFFFE70E: {
        'name': 'HCAN1_MD11_7',
        'size': 1,
        'comment': 'HCAN1 Message data 11 7',
    },
    0xFFFFE70F: {
        'name': 'HCAN1_MD11_8',
        'size': 1,
        'comment': 'HCAN1 Message data 11 8',
    },
    0xFFFFE710: {
        'name': 'HCAN1_MD12_1',
        'size': 1,
        'comment': 'HCAN1 Message data 12 1',
    },
    0xFFFFE711: {
        'name': 'HCAN1_MD12_2',
        'size': 1,
        'comment': 'HCAN1 Message data 12 2',
    },
    0xFFFFE712: {
        'name': 'HCAN1_MD12_3',
        'size': 1,
        'comment': 'HCAN1 Message data 12 3',
    },
    0xFFFFE713: {
        'name': 'HCAN1_MD12_4',
        'size': 1,
        'comment': 'HCAN1 Message data 12 4',
    },
    0xFFFFE714: {
        'name': 'HCAN1_MD12_5',
        'size': 1,
        'comment': 'HCAN1 Message data 12 5',
    },
    0xFFFFE715: {
        'name': 'HCAN1_MD12_6',
        'size': 1,
        'comment': 'HCAN1 Message data 12 6',
    },
    0xFFFFE716: {
        'name': 'HCAN1_MD12_7',
        'size': 1,
        'comment': 'HCAN1 Message data 12 7',
    },
    0xFFFFE717: {
        'name': 'HCAN1_MD12_8',
        'size': 1,
        'comment': 'HCAN1 Message data 12 8',
    },
    0xFFFFE718: {
        'name': 'HCAN1_MD13_1',
        'size': 1,
        'comment': 'HCAN1 Message data 13 1',
    },
    0xFFFFE719: {
        'name': 'HCAN1_MD13_2',
        'size': 1,
        'comment': 'HCAN1 Message data 13 2',
    },
    0xFFFFE71A: {
        'name': 'HCAN1_MD13_3',
        'size': 1,
        'comment': 'HCAN1 Message data 13 3',
    },
    0xFFFFE71B: {
        'name': 'HCAN1_MD13_4',
        'size': 1,
        'comment': 'HCAN1 Message data 13 4',
    },
    0xFFFFE71C: {
        'name': 'HCAN1_MD13_5',
        'size': 1,
        'comment': 'HCAN1 Message data 13 5',
    },
    0xFFFFE71D: {
        'name': 'HCAN1_MD13_6',
        'size': 1,
        'comment': 'HCAN1 Message data 13 6',
    },
    0xFFFFE71E: {
        'name': 'HCAN1_MD13_7',
        'size': 1,
        'comment': 'HCAN1 Message data 13 7',
    },
    0xFFFFE71F: {
        'name': 'HCAN1_MD13_8',
        'size': 1,
        'comment': 'HCAN1 Message data 13 8',
    },
    0xFFFFE720: {
        'name': 'HCAN1_MD14_1',
        'size': 1,
        'comment': 'HCAN1 Message data 14 1',
    },
    0xFFFFE721: {
        'name': 'HCAN1_MD14_2',
        'size': 1,
        'comment': 'HCAN1 Message data 14 2',
    },
    0xFFFFE722: {
        'name': 'HCAN1_MD14_3',
        'size': 1,
        'comment': 'HCAN1 Message data 14 3',
    },
    0xFFFFE723: {
        'name': 'HCAN1_MD14_4',
        'size': 1,
        'comment': 'HCAN1 Message data 14 4',
    },
    0xFFFFE724: {
        'name': 'HCAN1_MD14_5',
        'size': 1,
        'comment': 'HCAN1 Message data 14 5',
    },
    0xFFFFE725: {
        'name': 'HCAN1_MD14_6',
        'size': 1,
        'comment': 'HCAN1 Message data 14 6',
    },
    0xFFFFE726: {
        'name': 'HCAN1_MD14_7',
        'size': 1,
        'comment': 'HCAN1 Message data 14 7',
    },
    0xFFFFE727: {
        'name': 'HCAN1_MD14_8',
        'size': 1,
        'comment': 'HCAN1 Message data 14 8',
    },
    0xFFFFE728: {
        'name': 'HCAN1_MD15_1',
        'size': 1,
        'comment': 'HCAN1 Message data 15 1',
    },
    0xFFFFE729: {
        'name': 'HCAN1_MD15_2',
        'size': 1,
        'comment': 'HCAN1 Message data 15 2',
    },
    0xFFFFE72A: {
        'name': 'HCAN1_MD15_3',
        'size': 1,
        'comment': 'HCAN1 Message data 15 3',
    },
    0xFFFFE72B: {
        'name': 'HCAN1_MD15_4',
        'size': 1,
        'comment': 'HCAN1 Message data 15 4',
    },
    0xFFFFE72C: {
        'name': 'HCAN1_MD15_5',
        'size': 1,
        'comment': 'HCAN1 Message data 15 5',
    },
    0xFFFFE72D: {
        'name': 'HCAN1_MD15_6',
        'size': 1,
        'comment': 'HCAN1 Message data 15 6',
    },
    0xFFFFE72E: {
        'name': 'HCAN1_MD15_7',
        'size': 1,
        'comment': 'HCAN1 Message data 15 7',
    },
    0xFFFFE72F: {
        'name': 'HCAN1_MD15_8',
        'size': 1,
        'comment': 'HCAN1 Message data 15 8',
    },
    0xFFFFE800: {
        'name': 'FCCS',
        'size': 1,
        'comment': 'Flash code control status',
    },
    0xFFFFE801: {
        'name': 'FPCS',
        'size': 1,
        'comment': 'Flash program code select register',
    },
    0xFFFFE802: {
        'name': 'FECS',
        'size': 1,
        'comment': 'Flash erase code select register',
    },
    0xFFFFE804: {
        'name': 'FKEY',
        'size': 1,
        'comment': 'Flash key code register',
    },
    0xFFFFE805: {
        'name': 'FMATS',
        'size': 1,
        'comment': 'Flash MAT select register',
    },
    0xFFFFE806: {
        'name': 'FTDAR',
        'size': 1,
        'comment': 'Flash transfer destination address register',
    },
    0xFFFFEC00: {
        'name': 'UBARH',
        'size': 2,
        'comment': 'User break address register H',
    },
    0xFFFFEC02: {
        'name': 'UBARL',
        'size': 2,
        'comment': 'User break address register L',
    },
    0xFFFFEC04: {
        'name': 'UBAMRH',
        'size': 2,
        'comment': 'User break address mask register H',
    },
    0xFFFFEC06: {
        'name': 'UBAMRL',
        'size': 2,
        'comment': 'User break address mask register L',
    },
    0xFFFFEC08: {
        'name': 'UBBR',
        'size': 2,
        'comment': 'User break bus cycle register',
    },
    0xFFFFEC0A: {
        'name': 'UBCR',
        'size': 2,
        'comment': 'User break control register',
    },
    0xFFFFEC10: {
        'name': 'TCSR',
        'size': 1,
        'comment': 'Timer control/status register',
    },
    0xFFFFEC11: {
        'name': 'TCNT',
        'size': 1,
        'comment': 'Timer counter',
    },
    0xFFFFEC12: {
        'name': 'RSTCSR_W',
        'size': 1,
        'comment': 'Reset control/status register (write)',
    },
    0xFFFFEC13: {
        'name': 'RSTCSR_R',
        'size': 1,
        'comment': 'Reset control/status register (read)',
    },
    0xFFFFEC14: {
        'name': 'SBYCR',
        'size': 1,
        'comment': 'Standby control register',
    },
    0xFFFFEC20: {
        'name': 'BCR1',
        'size': 2,
        'comment': 'Bus control register 1',
    },
    0xFFFFEC22: {
        'name': 'BCR2',
        'size': 2,
        'comment': 'Bus control register 2',
    },
    0xFFFFEC24: {
        'name': 'WCR',
        'size': 2,
        'comment': 'Wait state control register',
    },
    0xFFFFEC26: {
        'name': 'RAMER',
        'size': 2,
        'comment': 'RAM emulation register',
    },
    0xFFFFECB0: {
        'name': 'DMAOR',
        'size': 2,
        'comment': 'Shared DMA operation register',
    },
    0xFFFFECC0: {
        'name': 'SAR0',
        'size': 4,
        'comment': 'DMA source address register 0',
    },
    0xFFFFECC4: {
        'name': 'DAR0',
        'size': 4,
        'comment': 'DMA destination address register 0',
    },
    0xFFFFECC8: {
        'name': 'DMATCR0',
        'size': 4,
        'comment': 'DMA transfer count register 0',
    },
    0xFFFFECCC: {
        'name': 'CHCR0',
        'size': 4,
        'comment': 'DMA channel control register 0',
    },
    0xFFFFECD0: {
        'name': 'SAR1',
        'size': 4,
        'comment': 'DMA source address register 1',
    },
    0xFFFFECD4: {
        'name': 'DAR1',
        'size': 4,
        'comment': 'DMA destination address register 1',
    },
    0xFFFFECD8: {
        'name': 'DMATCR1',
        'size': 4,
        'comment': 'DMA transfer count register 1',
    },
    0xFFFFECDC: {
        'name': 'CHCR1',
        'size': 4,
        'comment': 'DMA channel control register 1',
    },
    0xFFFFECE0: {
        'name': 'SAR2',
        'size': 4,
        'comment': 'DMA source address register 2',
    },
    0xFFFFECE4: {
        'name': 'DAR2',
        'size': 4,
        'comment': 'DMA destination address register 2',
    },
    0xFFFFECE8: {
        'name': 'DMATCR2',
        'size': 4,
        'comment': 'DMA transfer count register 2',
    },
    0xFFFFECEC: {
        'name': 'CHCR2',
        'size': 4,
        'comment': 'DMA channel control register 2',
    },
    0xFFFFECF0: {
        'name': 'SAR3',
        'size': 4,
        'comment': 'DMA source address register 3',
    },
    0xFFFFECF4: {
        'name': 'DAR3',
        'size': 4,
        'comment': 'DMA destination address register 3',
    },
    0xFFFFECF8: {
        'name': 'DMATCR3',
        'size': 4,
        'comment': 'DMA transfer count register 3',
    },
    0xFFFFECFC: {
        'name': 'CHCR3',
        'size': 4,
        'comment': 'DMA channel control register 3',
    },
    0xFFFFED00: {
        'name': 'IPRA',
        'size': 2,
        'comment': 'Interrupt priority register A',
    },
    0xFFFFED02: {
        'name': 'IPRB',
        'size': 2,
        'comment': 'Interrupt priority register B',
    },
    0xFFFFED04: {
        'name': 'IPRC',
        'size': 2,
        'comment': 'Interrupt priority register C',
    },
    0xFFFFED06: {
        'name': 'IPRD',
        'size': 2,
        'comment': 'Interrupt priority register D',
    },
    0xFFFFED08: {
        'name': 'IPRE',
        'size': 2,
        'comment': 'Interrupt priority register E',
    },
    0xFFFFED0A: {
        'name': 'IPRF',
        'size': 2,
        'comment': 'Interrupt priority register F',
    },
    0xFFFFED0C: {
        'name': 'IPRG',
        'size': 2,
        'comment': 'Interrupt priority register G',
    },
    0xFFFFED0E: {
        'name': 'IPRH',
        'size': 2,
        'comment': 'Interrupt priority register H',
    },
    0xFFFFED10: {
        'name': 'IPRI',
        'size': 2,
        'comment': 'Interrupt priority register I',
    },
    0xFFFFED12: {
        'name': 'IPRJ',
        'size': 2,
        'comment': 'Interrupt priority register J',
    },
    0xFFFFED14: {
        'name': 'IPRK',
        'size': 2,
        'comment': 'Interrupt priority register K',
    },
    0xFFFFED16: {
        'name': 'IPRL',
        'size': 2,
        'comment': 'Interrupt priority register L',
    },
    0xFFFFED18: {
        'name': 'ICR',
        'size': 2,
        'comment': 'Interrupt control register',
    },
    0xFFFFED1A: {
        'name': 'ISR',
        'size': 2,
        'comment': 'IRQ status register',
    },
    0xFFFFF000: {
        'name': 'SMR0',
        'size': 1,
        'comment': 'Serial mode register 0',
    },
    0xFFFFF001: {
        'name': 'BRR0',
        'size': 1,
        'comment': 'Bit rate register 0',
    },
    0xFFFFF002: {
        'name': 'SCR0',
        'size': 1,
        'comment': 'Serial control register 0',
    },
    0xFFFFF003: {
        'name': 'TDR0',
        'size': 1,
        'comment': 'Transmit data register 0',
    },
    0xFFFFF004: {
        'name': 'SSR0',
        'size': 1,
        'comment': 'Seria status register 0',
    },
    0xFFFFF005: {
        'name': 'RDR0',
        'size': 1,
        'comment': 'Receive data register 0',
    },
    0xFFFFF006: {
        'name': 'SDCR0',
        'size': 1,
        'comment': 'Serial direction control register 0',
    },
    0xFFFFF008: {
        'name': 'SMR1',
        'size': 1,
        'comment': 'Serial mode register 1',
    },
    0xFFFFF009: {
        'name': 'BRR1',
        'size': 1,
        'comment': 'Bit rate register 1',
    },
    0xFFFFF00A: {
        'name': 'SCR1',
        'size': 1,
        'comment': 'Serial control register 1',
    },
    0xFFFFF00B: {
        'name': 'TDR1',
        'size': 1,
        'comment': 'Transmit data register 1',
    },
    0xFFFFF00C: {
        'name': 'SSR1',
        'size': 1,
        'comment': 'Seria status register 1',
    },
    0xFFFFF00D: {
        'name': 'RDR1',
        'size': 1,
        'comment': 'Receive data register 1',
    },
    0xFFFFF00E: {
        'name': 'SDCR1',
        'size': 1,
        'comment': 'Serial direction control register 1',
    },
    0xFFFFF010: {
        'name': 'SMR2',
        'size': 1,
        'comment': 'Serial mode register 2',
    },
    0xFFFFF011: {
        'name': 'BRR2',
        'size': 1,
        'comment': 'Bit rate register 2',
    },
    0xFFFFF012: {
        'name': 'SCR2',
        'size': 1,
        'comment': 'Serial control register 2',
    },
    0xFFFFF013: {
        'name': 'TDR2',
        'size': 1,
        'comment': 'Transmit data register 2',
    },
    0xFFFFF014: {
        'name': 'SSR2',
        'size': 1,
        'comment': 'Seria status register 2',
    },
    0xFFFFF015: {
        'name': 'RDR2',
        'size': 1,
        'comment': 'Receive data register 2',
    },
    0xFFFFF016: {
        'name': 'SDCR2',
        'size': 1,
        'comment': 'Serial direction control register 2',
    },
    0xFFFFF018: {
        'name': 'SMR3',
        'size': 1,
        'comment': 'Serial mode register 3',
    },
    0xFFFFF019: {
        'name': 'BRR3',
        'size': 1,
        'comment': 'Bit rate register 3',
    },
    0xFFFFF01A: {
        'name': 'SCR3',
        'size': 1,
        'comment': 'Serial control register 3',
    },
    0xFFFFF01B: {
        'name': 'TDR3',
        'size': 1,
        'comment': 'Transmit data register 3',
    },
    0xFFFFF01C: {
        'name': 'SSR3',
        'size': 1,
        'comment': 'Seria status register 3',
    },
    0xFFFFF01D: {
        'name': 'RDR3',
        'size': 1,
        'comment': 'Receive data register 3',
    },
    0xFFFFF01E: {
        'name': 'SDCR3',
        'size': 1,
        'comment': 'Serial direction control register 3',
    },
    0xFFFFF020: {
        'name': 'SMR4',
        'size': 1,
        'comment': 'Serial mode register 4',
    },
    0xFFFFF021: {
        'name': 'BRR4',
        'size': 1,
        'comment': 'Bit rate register 4',
    },
    0xFFFFF022: {
        'name': 'SCR4',
        'size': 1,
        'comment': 'Serial control register 4',
    },
    0xFFFFF023: {
        'name': 'TDR4',
        'size': 1,
        'comment': 'Transmit data register 4',
    },
    0xFFFFF024: {
        'name': 'SSR4',
        'size': 1,
        'comment': 'Seria status register 4',
    },
    0xFFFFF025: {
        'name': 'RDR4',
        'size': 1,
        'comment': 'Receive data register 4',
    },
    0xFFFFF026: {
        'name': 'SDCR4',
        'size': 1,
        'comment': 'Serial direction control register 4',
    },
    0xFFFFF400: {
        'name': 'TSTR2',
        'size': 1,
        'comment': 'Common timer start register 2',
    },
    0xFFFFF401: {
        'name': 'TSTR1',
        'size': 1,
        'comment': 'Common timer start register 1',
    },
    0xFFFFF402: {
        'name': 'TSTR3',
        'size': 1,
        'comment': 'Common timer start register 3',
    },
    0xFFFFF404: {
        'name': 'PSCR1',
        'size': 1,
        'comment': 'Common prescaler register 1',
    },
    0xFFFFF406: {
        'name': 'PSCR2',
        'size': 1,
        'comment': 'Common prescaler register 2',
    },
    0xFFFFF408: {
        'name': 'PSCR3',
        'size': 1,
        'comment': 'Common prescaler register 3',
    },
    0xFFFFF40A: {
        'name': 'PSCR4',
        'size': 1,
        'comment': 'Common prescaler register 4',
    },
    0xFFFFF420: {
        'name': 'ICR0DH',
        'size': 2,
        'comment': 'Input capture register 0DH',
    },
    0xFFFFF422: {
        'name': 'ICR0DL',
        'size': 2,
        'comment': 'Input capture register 0DL',
    },
    0xFFFFF424: {
        'name': 'ITVRR1',
        'size': 1,
        'comment': 'Timer interval interrupt request register 1',
    },
    0xFFFFF426: {
        'name': 'ITVRR2A',
        'size': 1,
        'comment': 'Timer interval interrupt request register 2A',
    },
    0xFFFFF428: {
        'name': 'ITVRR2B',
        'size': 1,
        'comment': 'Timer interval interrupt request register 2B',
    },
    0xFFFFF42A: {
        'name': 'TIOR0',
        'size': 1,
        'comment': 'Timer I/O control register',
    },
    0xFFFFF42C: {
        'name': 'TSR0',
        'size': 2,
        'comment': 'Timer status register 0',
    },
    0xFFFFF42E: {
        'name': 'TIER0',
        'size': 2,
        'comment': 'Timer interrupt enable register 0',
    },
    0xFFFFF430: {
        'name': 'TCNT0H',
        'size': 2,
        'comment': 'Free-running counter 0H',
    },
    0xFFFFF432: {
        'name': 'TCNT0L',
        'size': 2,
        'comment': 'Free-running counter 0L',
    },
    0xFFFFF434: {
        'name': 'ICR0AH',
        'size': 2,
        'comment': 'Input capture register 0AH',
    },
    0xFFFFF436: {
        'name': 'ICR0AL',
        'size': 2,
        'comment': 'Input capture register 0AL',
    },
    0xFFFFF438: {
        'name': 'ICR0BH',
        'size': 2,
        'comment': 'Input capture register 0BH',
    },
    0xFFFFF43A: {
        'name': 'ICR0BL',
        'size': 2,
        'comment': 'Input capture register 0BL',
    },
    0xFFFFF43C: {
        'name': 'ICR0CH',
        'size': 2,
        'comment': 'Input capture register 0CH',
    },
    0xFFFFF43E: {
        'name': 'ICR0CL',
        'size': 2,
        'comment': 'Input capture register 0CL',
    },
    0xFFFFF440: {
        'name': 'TCNT1A',
        'size': 2,
        'comment': 'Free-running counter 1A',
    },
    0xFFFFF442: {
        'name': 'TCNT1B',
        'size': 2,
        'comment': 'Free-running counter 1B',
    },
    0xFFFFF444: {
        'name': 'GR1A',
        'size': 2,
        'comment': 'General register 1A',
    },
    0xFFFFF446: {
        'name': 'GR1B',
        'size': 2,
        'comment': 'General register 1B',
    },
    0xFFFFF448: {
        'name': 'GR1C',
        'size': 2,
        'comment': 'General register 1C',
    },
    0xFFFFF44A: {
        'name': 'GR1D',
        'size': 2,
        'comment': 'General register 1D',
    },
    0xFFFFF44C: {
        'name': 'GR1E',
        'size': 2,
        'comment': 'General register 1E',
    },
    0xFFFFF44E: {
        'name': 'GR1F',
        'size': 2,
        'comment': 'General register 1F',
    },
    0xFFFFF450: {
        'name': 'GR1G',
        'size': 2,
        'comment': 'General register 1G',
    },
    0xFFFFF452: {
        'name': 'GR1H',
        'size': 2,
        'comment': 'General register 1H',
    },
    0xFFFFF454: {
        'name': 'OCR1',
        'size': 2,
        'comment': 'Output compare register 1',
    },
    0xFFFFF456: {
        'name': 'OSBR1',
        'size': 2,
        'comment': 'Offset base register 1',
    },
    0xFFFFF458: {
        'name': 'TIOR1B',
        'size': 1,
        'comment': 'Timer I/O control register 1B',
    },
    0xFFFFF459: {
        'name': 'TIOR1A',
        'size': 1,
        'comment': 'Timer I/O control register 1A',
    },
    0xFFFFF45A: {
        'name': 'TIOR1D',
        'size': 1,
        'comment': 'Timer I/O control register 1D',
    },
    0xFFFFF45B: {
        'name': 'TIOR1C',
        'size': 1,
        'comment': 'Timer I/O control register 1C',
    },
    0xFFFFF45C: {
        'name': 'TCR1B',
        'size': 1,
        'comment': 'Timer control register 1B',
    },
    0xFFFFF45D: {
        'name': 'TCR1A',
        'size': 1,
        'comment': 'Timer control register 1A',
    },
    0xFFFFF45E: {
        'name': 'TSR1A',
        'size': 2,
        'comment': 'Timer status register 1A',
    },
    0xFFFFF460: {
        'name': 'TSR1B',
        'size': 2,
        'comment': 'Timer status register 1B',
    },
    0xFFFFF462: {
        'name': 'TIER1A',
        'size': 2,
        'comment': 'Timer interrupt enable register 1A',
    },
    0xFFFFF464: {
        'name': 'TIER1B',
        'size': 2,
        'comment': 'Timer interrupt enable register 1B',
    },
    0xFFFFF466: {
        'name': 'TRGMDR',
        'size': 1,
        'comment': 'Trigger mode register',
    },
    0xFFFFF480: {
        'name': 'TSR3',
        'size': 2,
        'comment': 'Timer status register 3',
    },
    0xFFFFF482: {
        'name': 'TIER3',
        'size': 2,
        'comment': 'Timer interrupt enable register 3',
    },
    0xFFFFF484: {
        'name': 'TMDR',
        'size': 1,
        'comment': 'Timer mode register',
    },
    0xFFFFF4A0: {
        'name': 'TCNT3',
        'size': 2,
        'comment': 'Free-running conuter 3',
    },
    0xFFFFF4A2: {
        'name': 'GR3A',
        'size': 2,
        'comment': 'General register 3A',
    },
    0xFFFFF4A4: {
        'name': 'GR3B',
        'size': 2,
        'comment': 'General register 3B',
    },
    0xFFFFF4A6: {
        'name': 'GR3C',
        'size': 2,
        'comment': 'General register 3C',
    },
    0xFFFFF4A8: {
        'name': 'GR3D',
        'size': 2,
        'comment': 'General register 3D',
    },
    0xFFFFF4AA: {
        'name': 'TIOR3B',
        'size': 1,
        'comment': 'Timer I/O control register 3B',
    },
    0xFFFFF4AB: {
        'name': 'TIOR3A',
        'size': 1,
        'comment': 'Timer I/O control register 3A',
    },
    0xFFFFF4AC: {
        'name': 'TCR3',
        'size': 1,
        'comment': 'Timer control register 3',
    },
    0xFFFFF4C0: {
        'name': 'TCNT4',
        'size': 2,
        'comment': 'Free-running counter 4',
    },
    0xFFFFF4C2: {
        'name': 'GR4A',
        'size': 2,
        'comment': 'General register 4A',
    },
    0xFFFFF4C4: {
        'name': 'GR4B',
        'size': 2,
        'comment': 'General register 4B',
    },
    0xFFFFF4C6: {
        'name': 'GR4C',
        'size': 2,
        'comment': 'General register 4C',
    },
    0xFFFFF4C8: {
        'name': 'GR4D',
        'size': 2,
        'comment': 'General register 4D',
    },
    0xFFFFF4CA: {
        'name': 'TIOR4B',
        'size': 1,
        'comment': 'Timer I/O control register 4B',
    },
    0xFFFFF4CB: {
        'name': 'TIOR4A',
        'size': 1,
        'comment': 'Timer I/O control register 4A',
    },
    0xFFFFF4CC: {
        'name': 'TCR4',
        'size': 1,
        'comment': 'Timer control register 4',
    },
    0xFFFFF4E0: {
        'name': 'TCNT5',
        'size': 2,
        'comment': 'Free-running counter 5',
    },
    0xFFFFF4E2: {
        'name': 'GR5A',
        'size': 2,
        'comment': 'General register 5A',
    },
    0xFFFFF4E4: {
        'name': 'GR5B',
        'size': 2,
        'comment': 'General register 5B',
    },
    0xFFFFF4E6: {
        'name': 'GR5C',
        'size': 2,
        'comment': 'General register 5C',
    },
    0xFFFFF4E8: {
        'name': 'GR5D',
        'size': 2,
        'comment': 'General register 5D',
    },
    0xFFFFF4EA: {
        'name': 'TIOR5B',
        'size': 1,
        'comment': 'Timer I/O control register 5B',
    },
    0xFFFFF4EB: {
        'name': 'TIOR5A',
        'size': 1,
        'comment': 'Timer I/O control register 5A',
    },
    0xFFFFF4EC: {
        'name': 'TCR5',
        'size': 1,
        'comment': 'Timer control register 5',
    },
    0xFFFFF500: {
        'name': 'TCNT6A',
        'size': 2,
        'comment': 'Free-running counter 6A',
    },
    0xFFFFF502: {
        'name': 'TCNT6B',
        'size': 2,
        'comment': 'Free-running counter 6B',
    },
    0xFFFFF504: {
        'name': 'TCNT6C',
        'size': 2,
        'comment': 'Free-running counter 6C',
    },
    0xFFFFF506: {
        'name': 'TCNT6D',
        'size': 2,
        'comment': 'Free-running counter 6D',
    },
    0xFFFFF508: {
        'name': 'CYLR6A',
        'size': 2,
        'comment': 'Cycle register 6A',
    },
    0xFFFFF50A: {
        'name': 'CYLR6B',
        'size': 2,
        'comment': 'Cycle register 6B',
    },
    0xFFFFF50C: {
        'name': 'CYLR6C',
        'size': 2,
        'comment': 'Cycle register 6C',
    },
    0xFFFFF50E: {
        'name': 'CYLR6D',
        'size': 2,
        'comment': 'Cycle register 6D',
    },
    0xFFFFF510: {
        'name': 'BFR6A',
        'size': 2,
        'comment': 'Buffer register 6A',
    },
    0xFFFFF512: {
        'name': 'BFR6B',
        'size': 2,
        'comment': 'Buffer register 6B',
    },
    0xFFFFF514: {
        'name': 'BFR6C',
        'size': 2,
        'comment': 'Buffer register 6C',
    },
    0xFFFFF516: {
        'name': 'BFR6D',
        'size': 2,
        'comment': 'Buffer register 6D',
    },
    0xFFFFF518: {
        'name': 'DTR6A',
        'size': 2,
        'comment': 'Duty register 6A',
    },
    0xFFFFF51A: {
        'name': 'DTR6B',
        'size': 2,
        'comment': 'Duty register 6B',
    },
    0xFFFFF51C: {
        'name': 'DTR6C',
        'size': 2,
        'comment': 'Duty register 6C',
    },
    0xFFFFF51E: {
        'name': 'DTR6D',
        'size': 2,
        'comment': 'Duty register 6D',
    },
    0xFFFFF520: {
        'name': 'TCR6B',
        'size': 1,
        'comment': 'Timer control register 6A',
    },
    0xFFFFF521: {
        'name': 'TCR6A',
        'size': 1,
        'comment': 'Timer control register 6B',
    },
    0xFFFFF522: {
        'name': 'TSR6',
        'size': 2,
        'comment': 'Timer status register 6',
    },
    0xFFFFF524: {
        'name': 'TIER6',
        'size': 2,
        'comment': 'Timer interrupt enable register 6',
    },
    0xFFFFF526: {
        'name': 'PMDR',
        'size': 1,
        'comment': 'PWM mode register',
    },
    0xFFFFF580: {
        'name': 'TCNT7A',
        'size': 2,
        'comment': 'Free-running counter 7A',
    },
    0xFFFFF582: {
        'name': 'TCNT7B',
        'size': 2,
        'comment': 'Free-running counter 7B',
    },
    0xFFFFF584: {
        'name': 'TCNT7C',
        'size': 2,
        'comment': 'Free-running counter 7C',
    },
    0xFFFFF586: {
        'name': 'TCNT7D',
        'size': 2,
        'comment': 'Free-running counter 7D',
    },
    0xFFFFF588: {
        'name': 'CYLR7A',
        'size': 2,
        'comment': 'Cycle register 7A',
    },
    0xFFFFF58A: {
        'name': 'CYLR7B',
        'size': 2,
        'comment': 'Cycle register 7B',
    },
    0xFFFFF58C: {
        'name': 'CYLR7C',
        'size': 2,
        'comment': 'Cycle register 7C',
    },
    0xFFFFF58E: {
        'name': 'CYLR7D',
        'size': 2,
        'comment': 'Cycle register 7D',
    },
    0xFFFFF590: {
        'name': 'BFR7A',
        'size': 2,
        'comment': 'Buffer register 7A',
    },
    0xFFFFF592: {
        'name': 'BFR7B',
        'size': 2,
        'comment': 'Buffer register 7B',
    },
    0xFFFFF594: {
        'name': 'BFR7C',
        'size': 2,
        'comment': 'Buffer register 7C',
    },
    0xFFFFF596: {
        'name': 'BFR7D',
        'size': 2,
        'comment': 'Buffer register 7D',
    },
    0xFFFFF598: {
        'name': 'DTR7A',
        'size': 2,
        'comment': 'Duty register 7A',
    },
    0xFFFFF59A: {
        'name': 'DTR7B',
        'size': 2,
        'comment': 'Duty register 7B',
    },
    0xFFFFF59C: {
        'name': 'DTR7C',
        'size': 2,
        'comment': 'Duty register 7C',
    },
    0xFFFFF59E: {
        'name': 'DTR7D',
        'size': 2,
        'comment': 'Duty register 7D',
    },
    0xFFFFF5A0: {
        'name': 'TCR7B',
        'size': 1,
        'comment': 'Timer control register 7B',
    },
    0xFFFFF5A1: {
        'name': 'TCR7A',
        'size': 1,
        'comment': 'Timer control register 7A',
    },
    0xFFFFF5A2: {
        'name': 'TSR7',
        'size': 2,
        'comment': 'Timer status register 7',
    },
    0xFFFFF5A4: {
        'name': 'TIER7',
        'size': 2,
        'comment': 'Timer interrupt enable register 7',
    },
    0xFFFFF5C0: {
        'name': 'TCNT11',
        'size': 2,
        'comment': 'Free-running counter 11',
    },
    0xFFFFF5C2: {
        'name': 'GR11A',
        'size': 2,
        'comment': 'General register 11A',
    },
    0xFFFFF5C4: {
        'name': 'GR11B',
        'size': 2,
        'comment': 'General register 11B',
    },
    0xFFFFF5C6: {
        'name': 'TIOR11',
        'size': 1,
        'comment': 'Timer I/O control register 11',
    },
    0xFFFFF5C8: {
        'name': 'TCR11',
        'size': 1,
        'comment': 'Timer control register 11',
    },
    0xFFFFF5CA: {
        'name': 'TSR11',
        'size': 2,
        'comment': 'Timer status register 11',
    },
    0xFFFFF5CC: {
        'name': 'TIER11',
        'size': 2,
        'comment': 'Timer interrupt enable register 11',
    },
    0xFFFFF600: {
        'name': 'TCNT2A',
        'size': 2,
        'comment': 'Free-running counter 2A',
    },
    0xFFFFF602: {
        'name': 'TCNT2B',
        'size': 2,
        'comment': 'Free-running counter 2B',
    },
    0xFFFFF604: {
        'name': 'GR2A',
        'size': 2,
        'comment': 'General register 2A',
    },
    0xFFFFF606: {
        'name': 'GR2B',
        'size': 2,
        'comment': 'General register 2B',
    },
    0xFFFFF608: {
        'name': 'GR2C',
        'size': 2,
        'comment': 'General register 2C',
    },
    0xFFFFF60A: {
        'name': 'GR2D',
        'size': 2,
        'comment': 'General register 2D',
    },
    0xFFFFF60C: {
        'name': 'GR2E',
        'size': 2,
        'comment': 'General register 2E',
    },
    0xFFFFF60E: {
        'name': 'GR2F',
        'size': 2,
        'comment': 'General register 2F',
    },
    0xFFFFF610: {
        'name': 'GR2G',
        'size': 2,
        'comment': 'General register 2G',
    },
    0xFFFFF612: {
        'name': 'GR2H',
        'size': 2,
        'comment': 'General register 2H',
    },
    0xFFFFF614: {
        'name': 'OCR2A',
        'size': 2,
        'comment': 'Output compare register 2A',
    },
    0xFFFFF616: {
        'name': 'OCR2B',
        'size': 2,
        'comment': 'Output compare register 2B',
    },
    0xFFFFF618: {
        'name': 'OCR2C',
        'size': 2,
        'comment': 'Output compare register 2C',
    },
    0xFFFFF61A: {
        'name': 'OCR2D',
        'size': 2,
        'comment': 'Output compare register 2D',
    },
    0xFFFFF61C: {
        'name': 'OCR2E',
        'size': 2,
        'comment': 'Output compare register 2E',
    },
    0xFFFFF61E: {
        'name': 'OCR2F',
        'size': 2,
        'comment': 'Output compare register 2F',
    },
    0xFFFFF620: {
        'name': 'OCR2G',
        'size': 2,
        'comment': 'Output compare register 2G',
    },
    0xFFFFF622: {
        'name': 'OCR2H',
        'size': 2,
        'comment': 'Output compare register 2H',
    },
    0xFFFFF624: {
        'name': 'OSBR2',
        'size': 2,
        'comment': 'Offset base register 2',
    },
    0xFFFFF626: {
        'name': 'TIOR2B',
        'size': 1,
        'comment': 'Timer I/O control register 2B',
    },
    0xFFFFF627: {
        'name': 'TIOR2A',
        'size': 1,
        'comment': 'Timer I/O control register 2A',
    },
    0xFFFFF628: {
        'name': 'TIOR2D',
        'size': 1,
        'comment': 'Timer I/O control register 2D',
    },
    0xFFFFF629: {
        'name': 'TIOR2C',
        'size': 1,
        'comment': 'Timer I/O control register 2C',
    },
    0xFFFFF62A: {
        'name': 'TCR2B',
        'size': 1,
        'comment': 'Timer control register 2B',
    },
    0xFFFFF62B: {
        'name': 'TCR2A',
        'size': 1,
        'comment': 'Timer control register 2A',
    },
    0xFFFFF62C: {
        'name': 'TSR2A',
        'size': 2,
        'comment': 'Timer status register 2A',
    },
    0xFFFFF62E: {
        'name': 'TSR2B',
        'size': 2,
        'comment': 'Timer status register 2B',
    },
    0xFFFFF630: {
        'name': 'TIER2A',
        'size': 2,
        'comment': 'Timer interrupt enable register 2A',
    },
    0xFFFFF632: {
        'name': 'TIER2B',
        'size': 2,
        'comment': 'Timer interrupt enable register 2B',
    },
    0xFFFFF640: {
        'name': 'DCNT8A',
        'size': 2,
        'comment': 'Down-counter 8A',
    },
    0xFFFFF642: {
        'name': 'DNCT8B',
        'size': 2,
        'comment': 'Down-counter 8B',
    },
    0xFFFFF644: {
        'name': 'DNCT8C',
        'size': 2,
        'comment': 'Down-counter 8C',
    },
    0xFFFFF646: {
        'name': 'DCNT8D',
        'size': 2,
        'comment': 'Down-counter 8D',
    },
    0xFFFFF648: {
        'name': 'DCNT8E',
        'size': 2,
        'comment': 'Down-counter 8E',
    },
    0xFFFFF64A: {
        'name': 'DCNT8F',
        'size': 2,
        'comment': 'Down-counter 8F',
    },
    0xFFFFF64C: {
        'name': 'DCNT8G',
        'size': 2,
        'comment': 'Down-counter 8G',
    },
    0xFFFFF64E: {
        'name': 'DCNT8H',
        'size': 2,
        'comment': 'Down-counter 8H',
    },
    0xFFFFF650: {
        'name': 'DCNT8I',
        'size': 2,
        'comment': 'Down-counter 8I',
    },
    0xFFFFF652: {
        'name': 'DCNT8J',
        'size': 2,
        'comment': 'Down-counter 8J',
    },
    0xFFFFF654: {
        'name': 'DCNT8K',
        'size': 2,
        'comment': 'Down-counter 8K',
    },
    0xFFFFF656: {
        'name': 'DCNT8L',
        'size': 2,
        'comment': 'Down-counter 8L',
    },
    0xFFFFF658: {
        'name': 'DCNT8M',
        'size': 2,
        'comment': 'Down-counter 8M',
    },
    0xFFFFF65A: {
        'name': 'DCNT8N',
        'size': 2,
        'comment': 'Down-counter 8N',
    },
    0xFFFFF65C: {
        'name': 'DCNT8O',
        'size': 2,
        'comment': 'Down-counter 8O',
    },
    0xFFFFF65E: {
        'name': 'DCNT8P',
        'size': 2,
        'comment': 'Down-counter 8P',
    },
    0xFFFFF660: {
        'name': 'RLDR8',
        'size': 2,
        'comment': 'Reload register 8',
    },
    0xFFFFF662: {
        'name': 'TCNR',
        'size': 2,
        'comment': 'Timer connection register',
    },
    0xFFFFF664: {
        'name': 'OTR',
        'size': 2,
        'comment': 'One-shot pulse terminate register',
    },
    0xFFFFF666: {
        'name': 'DSTR',
        'size': 2,
        'comment': 'Down-count start register',
    },
    0xFFFFF668: {
        'name': 'TCR8',
        'size': 1,
        'comment': 'Timer control register 8',
    },
    0xFFFFF66A: {
        'name': 'TSR8',
        'size': 2,
        'comment': 'Timer status register 8',
    },
    0xFFFFF66C: {
        'name': 'TIER8',
        'size': 2,
        'comment': 'Timer interrupt enable register 8',
    },
    0xFFFFF66E: {
        'name': 'RLDENR',
        'size': 1,
        'comment': 'Reload enable register',
    },
    0xFFFFF680: {
        'name': 'ECNT9A',
        'size': 1,
        'comment': 'Event counter 9A',
    },
    0xFFFFF682: {
        'name': 'ECNT9B',
        'size': 1,
        'comment': 'Event counter 9B',
    },
    0xFFFFF684: {
        'name': 'ECNT9C',
        'size': 1,
        'comment': 'Event counter 9C',
    },
    0xFFFFF686: {
        'name': 'ECNT9D',
        'size': 1,
        'comment': 'Event counter 9D',
    },
    0xFFFFF688: {
        'name': 'ECNT9E',
        'size': 1,
        'comment': 'Event counter 9E',
    },
    0xFFFFF68A: {
        'name': 'ECNT9F',
        'size': 1,
        'comment': 'Event counter 9F',
    },
    0xFFFFF68C: {
        'name': 'GR9A',
        'size': 1,
        'comment': 'General register 9A',
    },
    0xFFFFF68E: {
        'name': 'GR9B',
        'size': 1,
        'comment': 'General register 9B',
    },
    0xFFFFF690: {
        'name': 'GR9C',
        'size': 1,
        'comment': 'General register 9C',
    },
    0xFFFFF692: {
        'name': 'GR9D',
        'size': 1,
        'comment': 'General register 9D',
    },
    0xFFFFF694: {
        'name': 'GR9E',
        'size': 1,
        'comment': 'General register 9E',
    },
    0xFFFFF696: {
        'name': 'GR9F',
        'size': 1,
        'comment': 'General register 9F',
    },
    0xFFFFF698: {
        'name': 'TCR9A',
        'size': 1,
        'comment': 'Timer control register 9A',
    },
    0xFFFFF69A: {
        'name': 'TCR9B',
        'size': 1,
        'comment': 'Timer control register 9B',
    },
    0xFFFFF69C: {
        'name': 'TCR9C',
        'size': 1,
        'comment': 'Timer control register 9C',
    },
    0xFFFFF69E: {
        'name': 'TSR9',
        'size': 2,
        'comment': 'Timer status register 9',
    },
    0xFFFFF6A0: {
        'name': 'TIER9',
        'size': 2,
        'comment': 'Timer interrupt enable register 9',
    },
    0xFFFFF6C0: {
        'name': 'TCNT10AH',
        'size': 2,
        'comment': 'Free-running counter 10AH',
    },
    0xFFFFF6C2: {
        'name': 'TCNT10AL',
        'size': 2,
        'comment': 'Free-running conuter 10AL',
    },
    0xFFFFF6C4: {
        'name': 'TCNT10B',
        'size': 2,
        'comment': 'Event counter 10B',
    },
    0xFFFFF6C6: {
        'name': 'TCNT10C',
        'size': 2,
        'comment': 'Reload counter 10C',
    },
    0xFFFFF6C8: {
        'name': 'TCNT10D',
        'size': 1,
        'comment': 'Correction counter 10D',
    },
    0xFFFFF6CA: {
        'name': 'TCNT10E',
        'size': 2,
        'comment': 'Correction angle counter 10E',
    },
    0xFFFFF6CC: {
        'name': 'TCNT10F',
        'size': 2,
        'comment': 'Correction angle counter 10F',
    },
    0xFFFFF6CE: {
        'name': 'TCNT10G',
        'size': 2,
        'comment': 'Free-running counter 10G',
    },
    0xFFFFF6D0: {
        'name': 'ICR10AH',
        'size': 2,
        'comment': 'Input capture register 10AH',
    },
    0xFFFFF6D2: {
        'name': 'ICR10AL',
        'size': 2,
        'comment': 'Input capture register 10AL',
    },
    0xFFFFF6D4: {
        'name': 'OCR10AH',
        'size': 2,
        'comment': 'Output compare register 10AH',
    },
    0xFFFFF6D6: {
        'name': 'OCR10AL',
        'size': 2,
        'comment': 'Output compare register 10AL',
    },
    0xFFFFF6D8: {
        'name': 'OCR10B',
        'size': 1,
        'comment': 'Output compare register 10B',
    },
    0xFFFFF6DA: {
        'name': 'RLD10C',
        'size': 2,
        'comment': 'Reload register 10C',
    },
    0xFFFFF6DC: {
        'name': 'GR10G',
        'size': 2,
        'comment': 'General register 10G',
    },
    0xFFFFF6DE: {
        'name': 'TCNT10H',
        'size': 1,
        'comment': 'Noise canceler counter 10H',
    },
    0xFFFFF6E0: {
        'name': 'NCR10',
        'size': 1,
        'comment': 'Noise canceler register 10',
    },
    0xFFFFF6E2: {
        'name': 'TIOR10',
        'size': 1,
        'comment': 'Timer I/O counter register 10',
    },
    0xFFFFF6E4: {
        'name': 'TCR10',
        'size': 1,
        'comment': 'Timer control register 10',
    },
    0xFFFFF6E6: {
        'name': 'TCCLR10',
        'size': 2,
        'comment': 'Correction counter clear register 10',
    },
    0xFFFFF6E8: {
        'name': 'TSR10',
        'size': 2,
        'comment': 'Timer status register 10',
    },
    0xFFFFF6EA: {
        'name': 'TIER10',
        'size': 2,
        'comment': 'Timer interrupt enable register 10',
    },
    0xFFFFF700: {
        'name': 'POPCR',
        'size': 2,
        'comment': 'Pulse output port control register',
    },
    0xFFFFF708: {
        'name': 'SYSCR',
        'size': 1,
        'comment': 'System control register',
    },
    0xFFFFF70A: {
        'name': 'MSTCR_W',
        'size': 1,
        'comment': 'Module standby control register (write)',
    },
    0xFFFFF70B: {
        'name': 'MSTCR_R',
        'size': 1,
        'comment': 'Module standby control register (read)',
    },
    0xFFFFF710: {
        'name': 'CMSTR',
        'size': 2,
        'comment': 'Shared compare match timer start register',
    },
    0xFFFFF712: {
        'name': 'CMCSR0',
        'size': 2,
        'comment': 'Compare match timer control/status register 0',
    },
    0xFFFFF714: {
        'name': 'CMCNT0',
        'size': 2,
        'comment': 'Compare match timer counter 0',
    },
    0xFFFFF716: {
        'name': 'CMCOR0',
        'size': 2,
        'comment': 'Compare match timer constant register 0',
    },
    0xFFFFF718: {
        'name': 'CMCSR1',
        'size': 2,
        'comment': 'Compare match timer control/status register 1',
    },
    0xFFFFF71A: {
        'name': 'CMCNT1',
        'size': 2,
        'comment': 'Compare match timer counter 1',
    },
    0xFFFFF71C: {
        'name': 'CMCOR1',
        'size': 2,
        'comment': 'Compare match timer constant register 1',
    },
    0xFFFFF720: {
        'name': 'PAIOR',
        'size': 2,
        'comment': 'Port A IO register',
    },
    0xFFFFF722: {
        'name': 'PACRH',
        'size': 2,
        'comment': 'Port A control register H',
    },
    0xFFFFF724: {
        'name': 'PACRL',
        'size': 2,
        'comment': 'Port A control register L',
    },
    0xFFFFF726: {
        'name': 'PADR',
        'size': 2,
        'comment': 'Port A data register',
    },
    0xFFFFF728: {
        'name': 'PHIOR',
        'size': 2,
        'comment': 'Port H IO register',
    },
    0xFFFFF72A: {
        'name': 'PHCR',
        'size': 2,
        'comment': 'Port H control register',
    },
    0xFFFFF72C: {
        'name': 'PHDR',
        'size': 2,
        'comment': 'Port H data register',
    },
    0xFFFFF72E: {
        'name': 'ADTRGR1',
        'size': 1,
        'comment': 'A/D trigger register 1',
    },
    0xFFFFF730: {
        'name': 'PBIOR',
        'size': 1,
        'comment': 'Port B IO register',
    },
    0xFFFFF732: {
        'name': 'PBCRH',
        'size': 2,
        'comment': 'Port B control register H',
    },
    0xFFFFF734: {
        'name': 'PBCRL',
        'size': 2,
        'comment': 'Port B control register L',
    },
    0xFFFFF736: {
        'name': 'PBIR',
        'size': 2,
        'comment': 'Port B invert register',
    },
    0xFFFFF738: {
        'name': 'PBDR',
        'size': 2,
        'comment': 'Port B data register',
    },
    0xFFFFF73A: {
        'name': 'PCIOR',
        'size': 2,
        'comment': 'Port C IO register',
    },
    0xFFFFF73C: {
        'name': 'PCCR',
        'size': 2,
        'comment': 'Port C control register',
    },
    0xFFFFF73E: {
        'name': 'PCDR',
        'size': 2,
        'comment': 'Port C data register',
    },
    0xFFFFF740: {
        'name': 'PDIOR',
        'size': 2,
        'comment': 'Port D IO register',
    },
    0xFFFFF742: {
        'name': 'PDCRH',
        'size': 2,
        'comment': 'Port D control register H',
    },
    0xFFFFF744: {
        'name': 'PDCRL',
        'size': 2,
        'comment': 'Port D control register L',
    },
    0xFFFFF746: {
        'name': 'PDDR',
        'size': 2,
        'comment': 'Port D data register',
    },
    0xFFFFF748: {
        'name': 'PFIOR',
        'size': 2,
        'comment': 'Port F IO register',
    },
    0xFFFFF74A: {
        'name': 'PFCRH',
        'size': 2,
        'comment': 'Port F control register H',
    },
    0xFFFFF74C: {
        'name': 'PFCRL',
        'size': 2,
        'comment': 'Port F control register L',
    },
    0xFFFFF74E: {
        'name': 'PFDR',
        'size': 2,
        'comment': 'Port F data register',
    },
    0xFFFFF750: {
        'name': 'PEIOR',
        'size': 2,
        'comment': 'Port E IO register',
    },
    0xFFFFF752: {
        'name': 'PECR',
        'size': 2,
        'comment': 'Port E control register',
    },
    0xFFFFF754: {
        'name': 'PEDR',
        'size': 2,
        'comment': 'Port E data register',
    },
    0xFFFFF760: {
        'name': 'PGIOR',
        'size': 2,
        'comment': 'Port G IO register',
    },
    0xFFFFF762: {
        'name': 'PGCR',
        'size': 2,
        'comment': 'Port G control register',
    },
    0xFFFFF764: {
        'name': 'PGDR',
        'size': 2,
        'comment': 'Port G data register',
    },
    0xFFFFF766: {
        'name': 'PJIOR',
        'size': 2,
        'comment': 'Port J IO register',
    },
    0xFFFFF768: {
        'name': 'PJCRH',
        'size': 2,
        'comment': 'Port J control register H',
    },
    0xFFFFF76A: {
        'name': 'PJCRL',
        'size': 2,
        'comment': 'Port J control register L',
    },
    0xFFFFF76C: {
        'name': 'PJDR',
        'size': 2,
        'comment': 'Port J data register',
    },
    0xFFFFF76E: {
        'name': 'ADTRGR0',
        'size': 1,
        'comment': 'A/D trigger register 0',
    },
    0xFFFFF770: {
        'name': 'PKIOR',
        'size': 2,
        'comment': 'Port K IO register',
    },
    0xFFFFF772: {
        'name': 'PKCRH',
        'size': 2,
        'comment': 'Port K control register H',
    },
    0xFFFFF774: {
        'name': 'PKCRL',
        'size': 2,
        'comment': 'Port K control register L',
    },
    0xFFFFF776: {
        'name': 'PKIR',
        'size': 2,
        'comment': 'Port K invert register',
    },
    0xFFFFF778: {
        'name': 'PKDR',
        'size': 2,
        'comment': 'Port K data register',
    },
    0xFFFFF780: {
        'name': 'PAPR',
        'size': 2,
        'comment': 'Port A port register',
    },
    0xFFFFF782: {
        'name': 'PBPR',
        'size': 2,
        'comment': 'Port B port register',
    },
    0xFFFFF784: {
        'name': 'PDPR',
        'size': 2,
        'comment': 'Port D port register',
    },
    0xFFFFF786: {
        'name': 'PJPR',
        'size': 2,
        'comment': 'Port J port register',
    },
    0xFFFFF788: {
        'name': 'PLPR',
        'size': 2,
        'comment': 'Port L port register',
    },
    0xFFFFF7C2: {
        'name': 'SDSR',
        'size': 2,
        'comment': 'High-performance user debug interface status register',
    },
    0xFFFFF7C4: {
        'name': 'SDDRH',
        'size': 2,
        'comment': 'High-performance user debug interface data register H',
    },
    0xFFFFF7C6: {
        'name': 'SDDRL',
        'size': 2,
        'comment': 'High-performance user debug interface data register L',
    },
    0xFFFFF800: {
        'name': 'ADDR0H',
        'size': 1,
        'comment': 'A/D data register 0H',
    },
    0xFFFFF801: {
        'name': 'ADDR0L',
        'size': 1,
        'comment': 'A/D data register 0L',
    },
    0xFFFFF802: {
        'name': 'ADDR1H',
        'size': 1,
        'comment': 'A/D data register 1H',
    },
    0xFFFFF803: {
        'name': 'ADDR1L',
        'size': 1,
        'comment': 'A/D data register 1L',
    },
    0xFFFFF804: {
        'name': 'ADDR2H',
        'size': 1,
        'comment': 'A/D data register 2H',
    },
    0xFFFFF805: {
        'name': 'ADDR2L',
        'size': 1,
        'comment': 'A/D data register 2L',
    },
    0xFFFFF806: {
        'name': 'ADDR3H',
        'size': 1,
        'comment': 'A/D data register 3H',
    },
    0xFFFFF807: {
        'name': 'ADDR3L',
        'size': 1,
        'comment': 'A/D data register 3L',
    },
    0xFFFFF808: {
        'name': 'ADDR4H',
        'size': 1,
        'comment': 'A/D data register 4H',
    },
    0xFFFFF809: {
        'name': 'ADDR4L',
        'size': 1,
        'comment': 'A/D data register 4L',
    },
    0xFFFFF80A: {
        'name': 'ADDR5H',
        'size': 1,
        'comment': 'A/D data register 5H',
    },
    0xFFFFF80B: {
        'name': 'ADDR5L',
        'size': 1,
        'comment': 'A/D data register 5L',
    },
    0xFFFFF80C: {
        'name': 'ADDR6H',
        'size': 1,
        'comment': 'A/D data register 6H',
    },
    0xFFFFF80D: {
        'name': 'ADDR6L',
        'size': 1,
        'comment': 'A/D data register 6L',
    },
    0xFFFFF80E: {
        'name': 'ADDR7H',
        'size': 1,
        'comment': 'A/D data register 7H',
    },
    0xFFFFF80F: {
        'name': 'ADDR7L',
        'size': 1,
        'comment': 'A/D data register 7L',
    },
    0xFFFFF810: {
        'name': 'ADDR8H',
        'size': 1,
        'comment': 'A/D data register 8H',
    },
    0xFFFFF811: {
        'name': 'ADDR8L',
        'size': 1,
        'comment': 'A/D data register 8L',
    },
    0xFFFFF812: {
        'name': 'ADDR9H',
        'size': 1,
        'comment': 'A/D data register 9H',
    },
    0xFFFFF813: {
        'name': 'ADDR9L',
        'size': 1,
        'comment': 'A/D data register 9L',
    },
    0xFFFFF814: {
        'name': 'ADDR10H',
        'size': 1,
        'comment': 'A/D data register 10H',
    },
    0xFFFFF815: {
        'name': 'ADDR10L',
        'size': 1,
        'comment': 'A/D data register 10L',
    },
    0xFFFFF816: {
        'name': 'ADDR11H',
        'size': 1,
        'comment': 'A/D data register 11H',
    },
    0xFFFFF817: {
        'name': 'ADDR11L',
        'size': 1,
        'comment': 'A/D data register 11L',
    },
    0xFFFFF818: {
        'name': 'ADCSR0',
        'size': 1,
        'comment': 'A/D control/status register 0',
    },
    0xFFFFF819: {
        'name': 'ADCR0',
        'size': 1,
        'comment': 'A/D control register 0',
    },
    0xFFFFF820: {
        'name': 'ADDR12H',
        'size': 1,
        'comment': 'A/D data register 12H',
    },
    0xFFFFF821: {
        'name': 'ADDR12L',
        'size': 1,
        'comment': 'A/D data register 12L',
    },
    0xFFFFF822: {
        'name': 'ADDR13H',
        'size': 1,
        'comment': 'A/D data register 13H',
    },
    0xFFFFF823: {
        'name': 'ADDR13L',
        'size': 1,
        'comment': 'A/D data register 13L',
    },
    0xFFFFF824: {
        'name': 'ADDR14H',
        'size': 1,
        'comment': 'A/D data register 14H',
    },
    0xFFFFF825: {
        'name': 'ADDR14L',
        'size': 1,
        'comment': 'A/D data register 14L',
    },
    0xFFFFF826: {
        'name': 'ADDR15H',
        'size': 1,
        'comment': 'A/D data register 15H',
    },
    0xFFFFF827: {
        'name': 'ADDR15L',
        'size': 1,
        'comment': 'A/D data register 15L',
    },
    0xFFFFF838: {
        'name': 'ADCSR1',
        'size': 1,
        'comment': 'A/D control/status register 1',
    },
    0xFFFFF839: {
        'name': 'ADCR1',
        'size': 1,
        'comment': 'A/D control register 1',
    },
    0xFFFFF858: {
        'name': 'ADCSR2',
        'size': 1,
        'comment': 'A/D control/status register 2',
    },
    0xFFFFF859: {
        'name': 'ADCR2',
        'size': 1,
        'comment': 'A/D control register 2',
    },
}
