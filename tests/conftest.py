"""Configuration file for the test suite"""
import os
import sys
import pytest

GO_BACK_A_DIRECTORY = "/../"
GO_INTO_DIRECTORY = "pytest_encourage"

PREVIOUS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PREVIOUS_DIRECTORY + GO_BACK_A_DIRECTORY + GO_INTO_DIRECTORY)


pytest_plugins = ["pytester"]


@pytest.fixture
def temp_config_file_all_enabled(tmpdir):
    """ Fixture to generate a temporary config file and return its path """
    config = tmpdir.join(".encouragerc")
    config.write("""\
[comparison checks]
is_double_negative=true
is_none_compare=true
is_len_check=true

[constant checks]
is_true=true
is_false=true

[boolean operation checks]
has_too_many_ands=true
    """)
    return str(config)
