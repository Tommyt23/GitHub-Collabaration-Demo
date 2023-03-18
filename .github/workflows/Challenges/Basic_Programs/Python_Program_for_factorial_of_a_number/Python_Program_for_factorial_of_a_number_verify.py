import sys

sys.path.append("./Challenges/Basic_Programs/Python_Program_for_factorial_of_a_number/")

from Python_Program_for_factorial_of_a_number import factorial

def test_factorial():
    assert factorial(7) == 5040
    assert factorial(1) == 1
    assert factorial(13) == 6227020800
    assert factorial(0) == 0