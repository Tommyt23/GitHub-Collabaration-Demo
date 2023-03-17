import sys

print(sys.path) 

def test_add():
    assert add(7, 8) == 15
    assert add(1, 2) == 3
    assert add(1324154, 123) == 1324277
    assert add(0, 0) == 0