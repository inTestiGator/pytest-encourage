"""Configuration file for the test suite"""
import os
import sys
import pytest

GO_BACK_A_DIRECTORY = "/../"
GO_INTO_DIRECTORY = "pytest_encourage"

PREVIOUS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PREVIOUS_DIRECTORY + GO_BACK_A_DIRECTORY + GO_INTO_DIRECTORY)


# pylint: disable=C0103
pytest_plugins = ["pytester"]


@pytest.fixture
def temp_config_file_all_enabled(tmpdir):
    """ Fixture to generate a temporary config file and return its path """
    config = tmpdir.join(".encouragerc")
    config.write(
        """\
[comparison checks]
is_double_negative=true
is_none_compare=true
is_len_check=true

[constant checks]
is_true=true
is_false=true

[boolean operation checks]
has_too_many_ands=true
    """
    )
    return str(config)


@pytest.fixture
def temp_config_file_empty(tmpdir):
    """ Fixture to generate a temporary config file and return its path """
    config = tmpdir.join(".encouragerc")
    config.write(
        """\
[comparison checks]

[constant checks]

[boolean operation checks]
    """
    )
    return str(config)


@pytest.fixture
def temp_config_file_all_disabled(tmpdir):
    """ Fixture to generate a temporary config file and return its path """
    config = tmpdir.join(".encouragerc")
    config.write(
        """\
[comparison checks]
is_double_negative=false
is_none_compare=false
is_len_check=false

[constant checks]
is_true=false
is_false=false

[boolean operation checks]
has_too_many_ands=false
    """
    )
    return str(config)


@pytest.fixture
def fails_compare_checks():
    """ Returns a function designed to fail compare checks """

    def _failing_test():
        # pylint: disable=E0712
        # pylint: disable=C0121
        assert True != False
        assert [] is not None  # Compare to None

    return _failing_test


@pytest.fixture
def fails_constant_checks():
    """ Returns a function designed to fail compare checks """

    def _failing_test():
        assert True
        assert False

    return _failing_test


@pytest.fixture
def fails_bool_op_checks():
    """ Returns a function designed to fail compare checks """

    def _failing_test():
        assert True and True and True and True  # too many "and"s

    return _failing_test
