#!/usr/bin/env python

from setuptools import setup

import sh2dis

setup(
    name=sh2dis.__name__,
    description=sh2dis.__doc__,
    version=sh2dis.__version__,
    author=sh2dis.__author__,
    author_email=sh2dis.__email__,
    url=sh2dis.__url__,
    packages=['sh2dis',],
    entry_points={
        'console_scripts': ['sh2dis = sh2dis.__main__:main'],
    },
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Natural Language :: English',
      'Operating System :: POSIX',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Disassemblers',
      'Topic :: Software Development :: Embedded Systems',
    ])
