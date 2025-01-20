import pytest

def my_funktion(a, b):
    sum = a + b
    dele = a - b
    dobytok = a * b
    dilenya = a / b
    return sum, dele, dobytok, dilenya
my_funktion(3, 3)

def test_my_funktion(sum_result = 6, dele_result = 0, dobytok_result = 9, dilenya_result = 1):

    assert sum_result == 6
    assert dele_result == 0
    assert dobytok_result == 9
    assert dilenya_result == 1
test_my_funktion()


