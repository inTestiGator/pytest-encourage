""" Utility functions """
import json
from typing import List, Dict, Union


def read_source_file(filepath: str) -> List[str]:
    """ Decorator which reads the lines of a file and passes as arg to func """
    with open(filepath, "r") as f:
        lines = f.read().split("\n")
        return lines


def lint_message_is_in_assertion(msg: Dict[str, Union[str, int]]):
    """ Checks whether a PyLint message is referring to an assert statement """
    path, line_num = msg["path"], msg["line"]
    line = read_source_file(path)[line_num - 1]  # Line numbers start with 1, not 0
    line = line.strip()  # Remove indentation from start of line
    return line.startswith("assert")


def pylint_assertion_messages(pylint_json_string):
    """ Filters PyLint output to include only messages referring to assert statements """
    msgs = json.loads(pylint_json_string)
    return list(filter(lint_message_is_in_assertion, msgs))
