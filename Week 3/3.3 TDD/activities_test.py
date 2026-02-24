def square_area(sidelength):
    
    if sidelength < 0:
        return None
    
    return sidelength * sidelength
    
    

def test_square_area_8():
    assert square_area(8) == 64



def test_square_area_6():
    assert square_area(6) == 36



def test_square_area_negativesidelength():
    assert square_area(-5) == None