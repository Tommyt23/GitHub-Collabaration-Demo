import sys

sys.path.append("./Challenges/Basic_Programs/Python_Program_for_simple_interest/")

from Python_Program_for_simple_interest import simple_interest

def test_simple_interest():
    assert simple_interest(8, 6, 8) == 3.84
    assert simple_interest(1, 2, 3) == 0.06
    assert simple_interest(0, 0, 0) == 0
    assert simple_interest(100, 2, 5) == 10