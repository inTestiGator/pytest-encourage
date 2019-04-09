"""Configuration file for the test suite"""

import os
import sys
from pytest_encourage.automate import getpylint_output
from pytest_encourage.util import filter_assertions

GO_BACK_A_DIRECTORY = "/../"
GO_INTO_DIRECTORY = "pytest_encourage"

# set the system path to contain the previous directory
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + GO_BACK_A_DIRECTORY + GO_INTO_DIRECTORY)

def pytest_runtest_logstart(nodeid, location):
    filepath, _, _ = location
    messages = getpylint_output(filepath)
    for message in filter_assertions(messages):
        print(message)
