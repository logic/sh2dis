"""A disassembler for SuperH SH2 ROMs."""

from __future__ import print_function

from . import __main__

from . import mitsubishi
from . import segment
from . import sh2
from . import sh7052
from . import sh7055


__author__ = 'Ed Marshall'
__email__ = 'esm@logic.net'
__url__ = 'http://github.com/logic/sh2dis'
__version__ = '1.0'

__copyright__ = 'Copyright (C) 2010-2017, Ed Marshall'
__license__ = 'GPL3'


class ROMError(Exception):
    """An error related to parsing the supplied ROM data."""
    pass
