"""get pylint to run and get the output"""
import subprocess
from os import path
import ast
import inspect

from pylint.checkers import base
from checks import is_double_negative


def runChecks(item):
    """find double negative"""
    task = ast.parse(inspect.getsource(item.function))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            if isinstance(node.test, ast.Compare):
                checks.is_double_negative()


def getpylint_output(path_to_file):
    """get output from pylint"""
    list = ["pipenv", "run", "pylint", path_to_file, "-f", "json"]
    try:
        automate = subprocess.check_output(list, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as automate:
        output = automate.output
        output.decode()
        return output.decode()
