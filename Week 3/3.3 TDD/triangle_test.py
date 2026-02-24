def triangle_area(base,height):
    if base < 0 or height < 0:
        return None
    
    return 0.5 * base * height

def test_triangle_area_0_0():
    assert triangle_area(0,0) == 0

def test_triangle_area_3_4():
    assert triangle_area(3,4) == 6

def test_triangle_area_negativebase():
    assert triangle_area(-3,4) is None