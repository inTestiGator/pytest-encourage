""" Defines several checks to assess the quality of assertions """
import ast


def is_double_negative(expr: ast.Compare) -> bool:
    """ Checks whether a node of the abstract syntax tree represents a
        value != False comparison """
    # Note that Python comparisons can have more than two parts;
    # e.g. 1 < 2 != 3 is a valid expression which evaluates to True
    values = [expr.left] + expr.comparators

    # If each AST value is a wrapper for True / False / None, assign it to the
    # value it's wrapping
    values = [v.value if isinstance(v, ast.NameConstant) else v for v in values]
    operations = expr.ops
    for oper in reversed(operations):
        val = values.pop()
        if isinstance(oper, ast.NotEq) and val is False:  # "val != False"
            return True
    return False
