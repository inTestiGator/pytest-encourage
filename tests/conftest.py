"""Configuration file for the test suite"""
import os
import sys

GO_BACK_A_DIRECTORY = "/../"
GO_INTO_DIRECTORY = "pytest_encourage"

PREVIOUS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PREVIOUS_DIRECTORY + GO_BACK_A_DIRECTORY + GO_INTO_DIRECTORY)


pytest_plugins = ["pytester"]
