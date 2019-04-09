"""Functions for discovering and executing hooks."""

from _ import _

def pytest_runtest_logstart((filename, linenum, testname)):
    # run pylint using filename
