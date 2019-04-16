""" Defines several checks to assess the quality of assertions """
import ast
from typing import Iterator, Tuple


# All checks are enabled by default
COMPARE_CHECKS = (
    is_double_negative,
    is_none_compare,
)


def run_compare_checks(expr: ast.Compare, checks=COMPARE_CHECKS):
    """ Runs all comparison checks and returns those which fail """
    failing = []
    # On all the comparisons in the expression, find the failing checks
    for left, oper, right in get_all_compares(expr):
        for check in checks:
            if not check(left, oper, right):
                failing.append(check.__doc__)  # Docstring used as error msg
    return failing


def get_all_compares(expr: ast.Compare) -> Iterator[Tuple]:
    """ Yields each individual compare from a compound compare expression.
        e.g., the compound compare 1 < 2 < 3 would yield 1 < 2 and 2 < 3. """
    values = [expr.left] + expr.comparators

    # If each AST value is a wrapper for True / False / None, assign it to the
    # value it's wrapping
    values = [v.value if isinstance(v, ast.NameConstant) else v for v in values]

    # Create an iterator representing each individual comparison as a tuple
    # of the form (left value, comparison operation, right value)
    return zip(values, expr.ops, values[1:])


def is_double_negative(_, oper, right) -> bool:
    """ Comparison is a double negative, e.g. `val != False` """
    return isinstance(oper, ast.NotEq) and right is False


def is_none_compare(_, oper, right) -> bool:
    """ Comparison is not sufficiently specific, e.g. `val is not None` """
    return isinstance(oper, ast.IsNot) and right is None
