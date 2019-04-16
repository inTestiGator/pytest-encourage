"""Configuration file for the test suite"""

import os
import sys
import inspect
import ast
from pytest_encourage.automate import getpylint_output
from pytest_encourage.util import filter_assertions
from pytest_encourage.checks import is_double_negative

pytest_plugins = ["pytester"]
