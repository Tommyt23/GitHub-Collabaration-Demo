import sys

sys.path.append("./Challenges/Basic_Programs/Python_Program_for_Program_to_find_area_of_a_circle/")

from Python_Program_for_Program_to_find_area_of_a_circle import find_area

def test_find_area():
    assert find_area(1) == 3.142
    assert find_area(0) == 0
    assert find_area(5) == 78.550000
    