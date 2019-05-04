""" Defines hook functions for Pytest """
from pytest_encourage.checks import run_checks


def pytest_runtest_call(item):
    """ Runs linting checks on the function Pytest is currently testing """
    print("Pytest called hook")
    failed = run_checks(item.function)
    for failed_check_msg in failed:
        print(failed_check_msg)
