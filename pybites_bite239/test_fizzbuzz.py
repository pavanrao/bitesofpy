from fizzbuzz import fizzbuzz
import pytest
# write one or more pytest functions below, they need to start with test_

@pytest.mark.parametrize("test_input, expected",[
    (3,"Fizz"),
    (5, "Buzz"),
    (15, "Fizz Buzz"),
    (2, 2),
    (10, "Buzz"),
    (9, "Fizz"),
    (30, "Fizz Buzz"),
    (37, 37)
])
def test_fizzbuzz(test_input, expected):
    assert fizzbuzz(test_input) == expected
