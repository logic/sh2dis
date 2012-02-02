#!/usr/bin/env python

from distutils.core import setup

import sh2dis

setup(
    name=sh2dis.__name__,
    description=sh2dis.__doc__,
    version=sh2dis.__version__,
    author=sh2dis.__author__,
    author_email=sh2dis.__email__,
    url=sh2dis.__url__,
    packages=['sh2dis',],
    scripts=['bin/sh2dis',],
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Natural Language :: English',
      'Operating System :: POSIX',
      'Programming Language :: Python',
      'Topic :: Software Development :: Disassemblers',
      'Topic :: Software Development :: Embedded Systems',
    ])
