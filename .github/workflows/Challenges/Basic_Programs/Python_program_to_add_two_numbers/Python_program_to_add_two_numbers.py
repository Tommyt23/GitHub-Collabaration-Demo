import sys

sys.path.append("../../../../Challenges/Basic_Programs/Python_program_to_add_two_numbers/")

from Python_program_to_add_two_numbers import add

def test_add():
    assert add(7, 8) == 15
    assert add(1, 2) == 3
    assert add(1324154, 123) == 1324277
    assert add(0, 0) == 0