import os
import sys
import inspect
import ast
from pytest_encourage.automate import getpylint_output
from pytest_encourage.util import filter_assertions
from pytest_encourage.checks import is_double_negative

GO_BACK_A_DIRECTORY = "/../"
GO_INTO_DIRECTORY = "pytest_encourage"

# set the system path to contain the previous directory
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + GO_BACK_A_DIRECTORY + GO_INTO_DIRECTORY)


def pytest_runtest_logstart(location):
    # removed `nodeid` from input as it is an unused argument
    filepath, _, _ = location
    messages = getpylint_output(filepath)
    for message in filter_assertions(messages):
        print("{line}:{column} -- {message} ({symbol})".format(**message))


def pytest_runtest_call(item):
    tree = ast.parse(inspect.getsource(item.function))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            if isinstance(node.test, ast.Compare):
                print(is_double_negative(node.test))
    raise Exception()  # Force PyTest to display what we printed
