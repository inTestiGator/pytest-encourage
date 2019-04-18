"""Configuration file for the test suite"""
import json
import pytest


@pytest.fixture(scope="session")
def​ generate_json(tmpdir_factory):
    """ make a temp directory in jason"""
    a_dir = tmpdir_factory.mktemp('mydir')
    a_file = a_dir.join('something.txt')
    a_file.write('contents may settle during shipping')
    another_file.write('something different')

pytest_plugins = ["pytester"]
