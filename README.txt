sh2dis, an SH2-compatible (Renesas SuperH) disassembler.
Copyright (C) 2009, Edward S. Marshall

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program, in the file "COPYING3".  If not, see
<http://www.gnu.org/licenses/>.

----

That's the licensing stuff out of the way.

sh2dis is a very rudimentary automated disassembly tool for SH2 processors
written in Python. The internal representation and produced output are
inspired somewhat by IDA Pro, a general-purpose multi-platform code
analysis tool.

It can currently do relatively broad automated disassembly by tracking
register assignments loosely and following branches where it can reasonably
discern a destination. It doesn't catch everything yet, and likely never
will; the end goal is not a full-on SH2 simulator.

The example command line tool, "sh2dis", is capable of distinguishing between
SH7052 and SH7055 ROM formats, and will perform an automated disassembly
around the vector interupt table, labelling any known vectors and registers.
This example application may not work well with applications other than ROMs
taken from a Mitsubishi Lancer Evolution ECU, as that is the only platform
I have direct access to.

This software is in the very early stages of development, and likely
contains bugs. If you find one, please let me know at esm@logic.net.

Thanks for looking!

-Ed
