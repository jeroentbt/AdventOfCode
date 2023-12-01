import pytest
from solution import *


example = [("1abc2", "1"),
           ("pqr3stu8vwx", "3"),
           ("a1b2c3d4e5f", "1"),
           ("treb7uchet", "7")]
@pytest.mark.parametrize("data,first", example)
def test_get_first_digit(data, first):
    data_in = data
    assert first_digit_of(data_in) == first



