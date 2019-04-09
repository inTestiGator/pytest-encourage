"""Functions for discovering and executing hooks."""

import errno
import io
import logging
import os
import subprocess
import sys
import tempfile

def pytest_runtest_logstart((filename, linenum, testname)):
    # run pylint using filename
