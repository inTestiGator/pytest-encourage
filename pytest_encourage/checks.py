""" Defines several checks to assess the quality of assertions """
import ast
from typing import Iterator
from .customtypes import ASTValue, Comparison


# Checks to be run when the expression being asserted is a comparison


def get_all_compares(expr: ast.Compare) -> Iterator[Comparison]:
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
            if check(left, oper, right):
                failing.append(check.__doc__)  # Docstring used as error msg
    return failing


# Checks to be run when the expression being asserted is a constant


def is_true(const: ast.NameConstant) -> bool:
    """ Constant expression will never fail, e.g. `assert True` """
    return const.value == True


def is_false(const: ast.NameConstant) -> bool:
    """ Constant expression will always fail, e.g. `assert False` """
    return const.value == False


CONSTANT_CHECKS = (
    is_true,
    is_false
)


def run_constant_checks(expr: ast.NameConstant, checks=CONSTANT_CHECKS):
    """ Runs all constant checks and returns those which fail """
    failing = []
    for check in checks:
        if check(expr):
            failing.append(check.__doc__)
    return failing


# Checks to be run when the expression being asserted is a boolean operation
# (i.e. consists of multiple statements joined with `and` or `or`)


def has_too_many_ands(expr: ast.BoolOp) -> bool:
    """ Too many `and` statements; should be multiple assertions """
    return len(expr.values) > 2


BOOL_OP_CHECKS = (
    has_too_many_ands,
)


def run_bool_op_checks(expr: ast.BoolOp, checks=BOOL_OP_CHECKS):
    """ Runs all boolean operation checks and returns those which fail """
    failing = []
    for check in checks:
        if check(expr):
            failing.append(check.__doc__)
    return failing

def is_len_checks(_, oper, right) -> bool:
    """ Checks the length of a container"""
    return isinstance(oper, ast.IsLen)
