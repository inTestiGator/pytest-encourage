#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import setup

# Package meta-data
NAME = 'pytest-encourage'
VERSION = '0.1.0'
DESCRIPTION = 'A pytest plugin used for testing data coverage and providing positive reinforcement.'
LICENSE= 'GNU GPLv3'
AUTHOR = 'Jahlia Finney, Aubrey Collins, Elisia Wright, Jared Scklenski, Chih Jung Chen'
AUTHOR_EMAIL = 'finneyj@allegheny.edu, collinsa@allegheny.edu, chenc@allegheny.edu, wrighte@allegheny.edu, scklenskij@allegheny.edu'
URL = 'https://github.com/inTestiGator/pytest-encourage'


def read(filename):
    """ This function is reads in the file with the file path """
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filepath, mode="r", encoding="utf-8") as f:
        return f.read()


# Where it all begins
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    license=LICENSE,
    long_description=read('README.md'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    py_modules=['pytest_encourage'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['encourage = pytest_encourage.plugin', ], },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ]
)
