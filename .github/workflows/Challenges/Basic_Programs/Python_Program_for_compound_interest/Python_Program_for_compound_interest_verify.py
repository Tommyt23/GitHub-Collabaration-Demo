import sys

sys.path.append("./Challenges/Basic_Programs/Python_Program_for_compound_interest/")

from Python_Program_for_compound_interest import compound_interest

def test_compound_interest():
    assert compound_interest(10000, 10.25, 5) == 16288.946267774416
    assert compound_interest(0, 0, 0) == 0
    assert compound_interest(100, 2, 5) == 110.25
    assert compound_interest(100, 2, 0) == 100
    assert compound_interest(1200, 2, 5.4) == 100
    assert compound_interest(100, 0, 0) == 100