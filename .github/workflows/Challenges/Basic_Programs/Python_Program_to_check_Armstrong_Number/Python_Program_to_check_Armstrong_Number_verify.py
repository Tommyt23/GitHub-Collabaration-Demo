import sys

sys.path.append("./Challenges/Basic_Programs/Python_Program_to_check_Armstrong_Number/")

from Python_Program_to_check_Armstrong_Number import armstrong

def test_armstrong():
    assert armstrong(153) == True
    assert armstrong(0) == True
    assert armstrong(1) == True
    assert armstrong(100) == False
    assert armstrong(1634) == True
    assert armstrong(1253) == False