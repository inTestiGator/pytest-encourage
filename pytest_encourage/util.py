""" Utility functions """
import json
from typing import List, Dict, Union

import automate
def read_source_file(filepath: str) -> List[str]:
    """ Function which returns the lines of a file """
    # pylint: disable=invalid-name
    with open(filepath, "r") as f:
        lines = f.read().split("\n")
        return lines


# Define custom type for a Pylint message
LintMsg = Dict[str, Union[str, int]]


def lint_message_is_in_assertion(msg: LintMsg) -> bool:
    """ Checks whether a Pylint message is referring to an assert statement """
    path, line_num = msg["path"], msg["line"]
    # Line numbers start with 1, not 0
    line = read_source_file(path)[line_num - 1]
    # Remove indentation from start of line
    line = line.strip()
    return line.startswith("assert")


def filter_assertions(msgs: Union[str, List[LintMsg]]) -> List[LintMsg]:
    """ Filters Pylint output to include only messages which refer to
        assert statements """
    filtered_output = automate.getpylint_output()
    print(filtered_output)
    if isinstance(msgs, str):
        # If passing in a JSON string, parse it to get a List[LintMsg] object
        msgs = json.loads(msgs)
    return list(filter(lint_message_is_in_assertion, msgs))

if __name__ == "__main__":
    filtered_output = automate.getpylint_output()
    filter_assertions(filtered_output)
    print(filter_assertions(filtered_output))
