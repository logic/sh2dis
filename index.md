---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: sh2dis
layout: home
---
## An SH2-compatible (Renesas SuperH) disassembler

sh2dis is a very rudimentary automated disassembly tool for SH2 processors
written in Python. The internal representation and produced output are inspired
somewhat by IDA Pro, a general-purpose multi-platform code analysis tool.

It can currently do relatively broad automated disassembly by tracking register
assignments loosely and following branches where it can reasonably discern a
destination. It doesn't catch everything yet, and likely never will; the end
goal is not a full-on SH2 simulator.

This software is in the very early stages of development, and likely contains
bugs. If you find one, please let me know at esm@logic.net.

Thanks for looking!

-Ed

## Dependencies

* Python

## Install

Click the links at the top of the page, or see the download section below, to
grab the current state of the repository. Extract this anywhere, and run
"dis.py" with your installed python interpreter.

The example command line tool, "dis.py", is capable of distinguishing between
SH7052 and SH7055 ROM formats, and will perform an automated disassembly around
the vector interupt table, labelling any known vectors and registers. This
example application may not work well with applications other than ROMs taken
from a Mitsubishi Lancer Evolution ECU, as that is the only platform I have
direct access to.

## License

sh2dis, an SH2-compatible (Renesas SuperH) disassembler.

Copyright (C) 2009-2018, Edward S. Marshall <esm@logic.net>

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program, in the file "COPYING3". If not, see http://www.gnu.org/licenses/

## Authors

* Ed Marshall <esm@logic.net>

## Download

The source code lives on [Github](https://github.com/logic/sh2dis/), or you
can download an archive of the latest source code in either
[zip](https://github.com/logic/sh2dis/zipball/master) or
[tar](https://github.com/logic/sh2dis/tarball/master) formats.

You can also clone the project with git by running:

```
$ git clone git://github.com/logic/sh2dis
```
