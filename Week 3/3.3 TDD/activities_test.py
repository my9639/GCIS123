def square_area(sidelength):
    return sidelength * sidelength

def test_square_area_8():
    value = square_area(8)
    assert value == 64


def test_square_area_6():
    value = square_area(6)
    assert value == 36