import pytest

from numbers_to_dec import list_to_decimal


    # [0, 4, 2, 8] => 428
    # [1, 2] => 12
    # [3] => 3
    # [6, 2, True] => raises TypeError
    # [-3, 12] => raises ValueError
    # [3.6, 4, 1] => raises TypeError
    # ['4', 5, 3, 1] => raises TypeError

def test_success():
    assert list_to_decimal([0, 4, 2, 8]) == 428
    assert list_to_decimal([1, 2]) == 12
    assert list_to_decimal([3]) == 3

def test_ValueError():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])
        list_to_decimal([])

def test_TypeError():
    with pytest.raises(TypeError):
        list_to_decimal([6, 2, True])
        list_to_decimal([3.6, 4, 1])
        list_to_decimal(['4', 5, 3, 1])
  
