#!/usr/bin/env python

from distutils.core import setup

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, Python 2 isn't supported.")

setup(name='bitcoincharts',
      version='0.1.0',
      description='A quick Python API for parts of bitcoincharts.com',
      author='Brendan Smith',
      author_email='brendan.smith.93@gmail.com',
      url='https://github.com/brendancsmith/bitcoincharts',
      packages=['bitcoincharts'],
      install_requires=[
        'beautifulsoup4',
        'pandas'
      ],
      )
