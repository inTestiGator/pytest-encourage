""" Tests for using the config file to change plugin functionality """

from pytest_encourage.checks import get_enabled_checks_from_config
from pytest_encourage.checks import COMPARE_CHECKS, CONSTANT_CHECKS, BOOL_OP_CHECKS


@pytest.mark.xfail
def test_config_file_enables_checks(temp_config_file_all_enabled):
    """ Config file should allow checks to be enabled """
    # pylint: disable=E1111
    checks = get_enabled_checks_from_config(config_path=temp_config_file_all_enabled)
    assert isinstance(checks, dict)
    assert "COMPARE" in checks
    assert "CONSTANT" in checks
    assert "BOOL" in checks
    assert checks["COMPARE"] == list(COMPARE_CHECKS)
    assert checks["CONSTANT"] == list(CONSTANT_CHECKS)
    assert checks["BOOL"] == list(BOOL_OP_CHECKS)


@pytest.mark.xfail
def test_empty_config_file(temp_config_file_empty):
    """ If the config file is empty, all checks should be enabled """
    # pylint: disable=E1111
    checks = get_enabled_checks_from_config(config_path=temp_config_file_empty)
    assert isinstance(checks, dict)
    assert "COMPARE" in checks
    assert "CONSTANT" in checks
    assert "BOOL" in checks
    assert checks["COMPARE"] == list(COMPARE_CHECKS)
    assert checks["CONSTANT"] == list(CONSTANT_CHECKS)
    assert checks["BOOL"] == list(BOOL_OP_CHECKS)


@pytest.mark.xfail
def test_config_file_disables_checks(temp_config_file_all_disabled):
    """ Config file should allow checks to be disabled """
    # pylint: disable=E1111
    checks = get_enabled_checks_from_config(config_path=temp_config_file_all_disabled)
    assert "COMPARE" in checks
    assert "CONSTANT" in checks
    assert "BOOL" in checks
    assert checks["COMPARE"] == []
    assert checks["CONSTANT"] == []
    assert checks["BOOL"] == []
