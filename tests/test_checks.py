""" Tests that functions are linted correctly """
from pytest_encourage.checks import (
    run_checks,
    COMPARE_CHECKS,
    CONSTANT_CHECKS,
    BOOL_OP_CHECKS,
)


def test_compare_checks():
    """ Tests that comparison checks are working """

    def _failing_test():
        assert True != False  # TODO: disable pylint on this line
        assert [] is not None  # Compare to None

    failed = run_checks(_failing_test)
    for check in COMPARE_CHECKS:
        assert check.__doc__ in failed


def test_constant_checks():
    """ Tests that constant checks are working """

    def _failing_test():
        assert True
        assert False

    failed = run_checks(_failing_test)
    for check in CONSTANT_CHECKS:
        assert check.__doc__ in failed


def test_bool_op_checks():
    """ Tests that boolean operation checks are working """

    def _failing_test():
        assert True and True and True and True  # too many "and"s

    failed = run_checks(_failing_test)
    for check in BOOL_OP_CHECKS:
        assert check.__doc__ in failed
