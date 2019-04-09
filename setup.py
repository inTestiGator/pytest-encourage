#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import setup

# Package meta-data
NAME = 'pytest-encourage'
DESCRIPTION = 'A pytest plugin used for testing data coverage and providing '
    + 'positive reinforcement.'
LICENSE='GNU GPLv3'
AUTHOR = 'Jahlia Finney, Aubrey Collins, Elisia Wright, Jared Scklenski'
AUTHOR_EMAIL= 'finneyj@allegheny.edu, collinsa@allegheny.edu, '
    + 'wrighte@allegheny.edu, scklenskij@allegheny.edu'
URL = 'https://github.com/inTestiGator/pytest-encourage'

# Where it all begins
setup(
    name=NAME,
    description=DESCRIPTION,
    license=LICENSE,
    long_description=read('README.md'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ]
)
