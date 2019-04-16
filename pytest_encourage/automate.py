import subprocess
import os.path
from os import path

from pylint.checkers import base

def runChecks():
    try:
    fh = open('/path/to/file', 'r')
    # Store configuration file values
        if fh is not none:


def getpylint_output(path_to_file):
    list = ["pipenv", "run", "pylint", path_to_file, "-f", "json"]
    try:
        automate = subprocess.check_output(list, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as automate:
        output = automate.output
        output.decode()
        return output.decode()
