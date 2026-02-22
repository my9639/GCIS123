
import pick

def test_check_guess_correct(): 
    assert pick.check_guess(5,5) == 0
    assert pick.check_guess (4,5) == 1
    assert pick.check_guess(10,5) == 5

def test_check_guess_too_high():
    assert pick.check_guess (5,4)
    
def test_check_guess_too_low():
    assert pick.check_guess(4,5)
