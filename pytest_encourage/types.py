""" Defines custom type annotations in order to clarify what our functions
    take as arguments and what they return """

import ast
from typing import Tuple, Union

# Type annotation for the different kinds of syntax tree nodes
# which represent different types of Python objects
ASTValue = Union[
    ast.Name,  # A named variable
    ast.NameConstant,  # True, False, or None
    bool,  # NameConstants may be transformed into their actual values
    None,
    ast.Num,  # A number literal
    ast.Str,  # A string literal
    ast.Bytes,  # A bytes object
    ast.List,  # A list literal
    ast.Tuple,  # A tuple literal
    ast.Dict,  # A dict literal
    ast.Set,  # A set literal
]

# Type annotation representing a comparison statement:
# (left value, comparison operation, right value)
Comparison = Tuple[ASTValue, ast.cmpop, ASTValue]
