""" Defines hook functions for Pytest """
import sys
from pytest_encourage.automate import getpylint_output
from pytest_encourage.util import filter_assertions
from pytest_encourage.checks import run_checks

GO_BACK_A_DIRECTORY = "/../"
GO_INTO_DIRECTORY = "pytest_encourage"

# set the system path to contain the previous directory
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + GO_BACK_A_DIRECTORY + GO_INTO_DIRECTORY)


def pytest_runtest_call(item):
    """ Runs linting checks on the function Pytest is currently testing """
    failed = run_checks(item.function)
    for failed_check_msg in failed:
        print(failed_check_msg)
