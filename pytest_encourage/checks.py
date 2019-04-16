""" Defines several checks to assess the quality of assertions """
import ast


def is_double_negative(expr: ast.Compare) -> bool:
    """ Checks whether a node of the abstract syntax tree represents a
        value != False comparison """
    # Note that Python comparisons can have more than two parts;
    # e.g. 1 < 2 != 3 is a valid expression which evaluates to True
    values = [expr.left] + expr.comparators
    values = [v.value for v in values]  # Map ast.NameConstant to their values
    operations = expr.ops
    for oper in reversed(operations):
        val = values.pop()
        if isinstance(oper, ast.NotEq) and val is False:  # "val != False"
            return True
    return False
