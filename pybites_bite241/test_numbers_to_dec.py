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
    assert list_to_decimal([1,2,3,4,5,6,7,8,9,0]) == 1234567890
    

def test_negative():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])
        

def test_empty():
    with pytest.raises(ValueError):
        list_to_decimal([])
        
def test_bool():
    with pytest.raises(TypeError):
        list_to_decimal([False, True, 0, -1])

def test_str():
    with pytest.raises(TypeError):
        list_to_decimal(['4', 5, 3, 1])


def test_range():
    with pytest.raises(ValueError):
        list_to_decimal([11,99])


def test_endpoint():
    """
    This test was added so that a mutation would fail the code.
    Pybites uses mut.py to test the tests.
    Cehck this link for more details:
    https://pybit.es/guest-mutpy-exploration.html
    """
    with pytest.raises(ValueError):
        list_to_decimal([10,0])

@pytest.mark.xfail
def test_mutaion():
    """
    This did not help with testing mutation. 
    """
    if(list_to_decimal([10]) == 10):
        pytest.xfail("Extra test case to pass mutation test")

