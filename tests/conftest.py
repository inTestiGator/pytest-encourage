"""Configuration file for the test suite"""

import os
import sys
import json
import pytest
import warnings


if not sys.version_info >= (3, 5):
warnings.simplefilter("error", category=DeprecationWarning)


pytest_plugins = ["pytester"]


MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + "/../")


@pytest.fixture(scope="session")
def​ generate_json(tmpdir_factory):
    """ make a temp directory in jason"""
    a_dir = tmpdir_factory.mktemp('mydir')
    a_file = a_dir.join('something.txt')
    a_file.write('contents may settle during shipping')
    another_file.write('something different')
