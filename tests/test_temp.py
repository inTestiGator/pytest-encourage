"""Collection of tests for our checks"""
from pytest_encourage import checks
import pytest

def test_temp():
    if True:
        assert True != False

if __name__ == "__main__":
    powers = []
    for i in range(1,10):
        powers.append(2 ** i)

def test_none():
    """Tests not none check"""
    purse = []
    checks.is_none_compare(left, oper, right)
    ast.parse("assert purse is not none")

def test_comparechecks_fail():
   """Tests check for failing Comparisons"""
   cat = " "
   dog = "a"
   assert cat == dog

def test_too_many_and():
    """Tests check for too many ands"""
    pig = "2"
    cow = "2"
    tiger = "2"
    assert pig == cow & cow == tiger & pig == tiger

def test_is_len_checks():
    """tests the len check"""
    book = ["A", "B", "C", "D"]
    assert len(book) == 4

def test_bool_checks():
    """Tests boolean checks"""

def test_false_checks():
    """Tests false checks"""
    assert False

def test_true_checks():
    """Tests true checks"""
    assert True
