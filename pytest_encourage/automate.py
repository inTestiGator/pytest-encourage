"""run pylint automaticaly"""
import subprocess
from os import path
import ast
import inspect

from pylint.checkers import base
from checks import is_double_negative


def run_checks(item):
    """Function that calls the tool's checks"""
    task = ast.parse(inspect.getsource(item.function)) #  Unused variable
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):  # condition for assertion statements
            if isinstance(node.test, ast.Compare):  # condition for comparisons
                checks.is_double_negative()


def getpylint_output(path_to_file):
    """get output"""
    list = ["pipenv", "run", "pylint", path_to_file, "-f", "json"]
    try:
        automate = subprocess.check_output(list, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as automate:
        output = automate.output
        output.decode()
        return output.decode()
