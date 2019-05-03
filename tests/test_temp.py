"""Collection of tests for our checks"""
from pytest_encourage import checks
import pytest
import ast


def test_temp():
    if True:
        assert True != False


if __name__ == "__main__":
    powers = []
    for i in range(1, 10):
        powers.append(2 ** i)


def test_none():
    """Tests not none check"""

    node = ast.parse("purse = ['h']; assert purse is not None")
    assertion = node.body[1]
    compareA = assertion.test
    assertlist = checks.run_compare_checks(compareA)
    assert assertlist == [checks.is_none_compare.__doc__]
    print(node)


def test_comparechecks_fail():
    """Tests check for failing Comparisons"""
    cat = " "
    dog = "a"
    assert cat == dog


def test_too_many_and():
    """Tests check for too many ands"""
    node = ast.parse(
        "pig = '2'; cow = '2'; tiger = '2'; assert pig == cow and cow == tiger and pig == tiger"
    )
    assertion = node.body[3]
    compareTooMany = assertion.test
    assert checks.has_too_many_ands(compareTooMany)


def test_is_len_checks():
    """tests the len check"""
    book = ["A", "B", "C", "D"]
    assert len(book) == 4


def test_bool_checks():
    """Tests boolean checks"""


def test_false_checks():
    """Tests false checks"""
    node = ast.parse("assert True")
    assertion = node.body[0]
    falcheck = assertion.test
    assert checks.is_true(falcheck)


def test_true_checks():
    """Tests true checks"""
    node = ast.parse("assert True")
    assertion = node.body[0]
    trucheck = assertion.test
    assert checks.is_false(trucheck)
