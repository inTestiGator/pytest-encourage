#!/usr/bin/env python

import io
import os

from setuptools import setup

# Package meta-data
NAME = 'pytest-encourage'
DESCRIPTION = ''
AUTHOR = 'Jahlia Finney, Aubrey Collins, Elisia Wright, Jared Scklenski'
AUTHOR_EMAIL= 'finneyj@allegheny.edu, collinsa@allegheny.edu, wrighte@allegheny.edu, + scklenskij@allegheny.edu'
URL = 'https://github.com/inTestiGator/pytest-encourage'

# Where it all begins
setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=read('README.md'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
)
