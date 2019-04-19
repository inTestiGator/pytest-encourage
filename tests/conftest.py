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
    """ make a temp directory in json"""
    a_dir = tmpdir_factory.mktemp('mydir') # make a new directory ti store temp files
    a_file = a_dir.join('copieddata.json') # make a file in the a_dir directory
    # read the file and save it as data
    with open(MYPATH, 'a') as data:
    jdata = json.dumps(data) # convert data to json
    a_file.write(jdata) # save jdata in a_file

    return jdata
