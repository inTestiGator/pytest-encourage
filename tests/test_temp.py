"""Collection of tests for our checks"""
from pytest_encourage import checks

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
    assert purse is not none

def test_comparechecks_fail():
   """Tests check for failing Comparisons"""
   cat = " "
   dog = "a"
   checks.run_compare_checks()
   assert cat == dog
