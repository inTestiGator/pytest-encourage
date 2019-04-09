"""Functions for discovering and executing hooks."""

import errno
import io
import logging
import os
import subprocess
import sys
import tempfile

from pytest_encourage.util import filter_assertions

def pytest_runtest_logstart(nodeid, location):
    # run pylint using filename, then pass to filter_assertions
    """ signal the start of running a single test item.

    This hook will be called **before** :func:`pytest_runtest_setup`, :func:`pytest_runtest_call` and
    :func:`pytest_runtest_teardown` hooks.

    :param str nodeid: full id of the item
    :param location: a triple of ``(filename, linenum, testname)``
    """
