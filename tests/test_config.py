""" Tests for using the config file to change plugin functionality """

from pytest_encourage.checks import get_enabled_checks_from_config, check_is_enabled
from pytest_encourage.checks import COMPARE_CHECKS, CONSTANT_CHECKS, BOOL_OP_CHECKS


def test_check_is_enabled_all(temp_config_file_all_enabled):
    """ Looking up a check in the config file should return true if check
        is enabled """
    for check in COMPARE_CHECKS + CONSTANT_CHECKS + BOOL_OP_CHECKS:
        assert check_is_enabled(check, config_path=temp_config_file_all_enabled)


def test_check_is_enabled_none(temp_config_file_all_disabled):
    """ Looking up a check in the config file should return false if check
        is disabled """
    for check in COMPARE_CHECKS + CONSTANT_CHECKS + BOOL_OP_CHECKS:
        assert not check_is_enabled(check, config_path=temp_config_file_all_disabled)


def test_check_is_enabled_empty(temp_config_file_empty):
    """ If the config file is empty, all checks should be enabled """
    for check in COMPARE_CHECKS + CONSTANT_CHECKS + BOOL_OP_CHECKS:
        assert check_is_enabled(check, config_path=temp_config_file_empty)


def test_config_file_enables_checks(temp_config_file_all_enabled):
    """ Config file should allow checks to be enabled """
    checks = get_enabled_checks_from_config(config_path=temp_config_file_all_enabled)
    assert isinstance(checks, dict)
    assert "COMPARE" in checks
    assert "CONSTANT" in checks
    assert "BOOL" in checks
    assert checks["COMPARE"] == list(COMPARE_CHECKS)
    assert checks["CONSTANT"] == list(CONSTANT_CHECKS)
    assert checks["BOOL"] == list(BOOL_OP_CHECKS)


def test_empty_config_file(temp_config_file_empty):
    """ If the config file is empty, all checks should be enabled """
    checks = get_enabled_checks_from_config(config_path=temp_config_file_empty)
    assert isinstance(checks, dict)
    assert "COMPARE" in checks
    assert "CONSTANT" in checks
    assert "BOOL" in checks
    assert checks["COMPARE"] == list(COMPARE_CHECKS)
    assert checks["CONSTANT"] == list(CONSTANT_CHECKS)
    assert checks["BOOL"] == list(BOOL_OP_CHECKS)


def test_config_file_disables_checks(temp_config_file_all_disabled):
    """ Config file should allow checks to be disabled """
    checks = get_enabled_checks_from_config(config_path=temp_config_file_all_disabled)
    assert "COMPARE" in checks
    assert "CONSTANT" in checks
    assert "BOOL" in checks
    assert checks["COMPARE"] == []
    assert checks["CONSTANT"] == []
    assert checks["BOOL"] == []
