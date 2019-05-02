"""Functions for discovering and executing hooks."""

import errno
# unused import io
# unused import logging
# unused import os
import subprocess
import sys
# unused import tempfile

# unused from pytest_encourage.util import filter_assertions


def pytest_runtest_logstart(nodeid, location):
    """ signal the start of running a single test item.
    This hook will be called
    **before** :func:`pytest_runtest_setup`, :func:`pytest_runtest_call` and
    :func:`pytest_runtest_teardown` hooks.

    :param str nodeid: full id of the item
    :param location: a triple of ``(filename, linenum, testname)``
    """
    # file = os.path.basename(nodeid)
    # name = os.path.splitext(location)[0]


def run_pylint(script_path, cwd="."):
    # script_path pulled from nodeid?
    # just leveraged this, needs work
    """Execute a script from a working directory.
    :param script_path: Absolute path to the script to run.
    :param cwd: The directory to run the script from.
    """
    # calls and runs pylint
    from pylint import epylint as lint
    # pilint_stdout, pylint_stderr unused
    (pylint_stdout, pylint_stderr) = lint.py_run("module_name.py", return_std=True)

    # leveraged code
    run_thru_shell = sys.platform.startswith("pyl")
    if script_path.endswith(".py"):
        script_command = [sys.executable, script_path]
    else:
        script_command = [script_path]

    utils.make_executable(script_path) # utils unused

    try:
        proc = subprocess.Popen(script_command, shell=run_thru_shell, cwd=cwd)
        exit_status = proc.wait()
        if exit_status != EXIT_SUCCESS:
            raise FailedHookException(
                "Hook script failed (exit status: {})".format(exit_status)
            )
    except OSError as os_error:
        if os_error.errno == errno.ENOEXEC:
            raise FailedHookException("Hook script failed, might be an empty file")
        raise FailedHookException("Hook script failed (error: {})".format(os_error))
