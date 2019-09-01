#!/usr/bin/env python
# coding: utf8

VERSION = '0.1.3'

import sys

from setuptools import setup

extra_args = {}
if (sys.version_info[0] >= 3):
    extra_args['use_2to3'] = True

setup(name='backtesting',
      version=VERSION,
      description='backtesting',
      author='Jeroen Verschuuren',
      url='https://github.com/ILoveHubGit/backtesting',
      packages=['backtesting'],
      install_requires=['numpy>=1.11',
                        'pandas>=0.19',
                        'pyyaml',
                        'cached_property'],
      **extra_args)
