import pytest
def no_zero(number):
    if number < 0:
        raise ValueError
    return number
def test_no_zero():

    assert no_zero(5) == 5

    with pytest.raises(ValueError)
        no_zero(-1)
test_no_zero()