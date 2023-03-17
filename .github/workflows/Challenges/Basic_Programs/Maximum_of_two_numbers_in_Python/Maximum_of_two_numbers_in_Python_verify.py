import sys

sys.path.append("./Challenges/Basic_Programs/Maximum_of_two_numbers_in_Python/")

from Maximum_of_two_numbers_in_Python import maximum

def test_maximum():
    assert maximum(7, 8) == 8
    assert maximum(1, 2) == 2
    assert maximum(1324154, 123) == 1324154
    assert maximum(0, 0) == 0