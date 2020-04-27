from fibonacci import fib
import pytest 

# write one or more pytest functions below, they need to start with test_
def test_test_first_3():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1

def test_fib():
    #0 1 1 2 3 5 8 13 
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
