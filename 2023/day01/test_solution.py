import pytest
from solution import *


example = [("1abc2", "1", "2"),
           ("pqr3stu8vwx", "3", "8"),
           ("a1b2c3d4e5f", "1", "5"),
           ("treb7uchet", "7", "7")]
@pytest.mark.parametrize("data,first,last", example)
def test_get_first_and_last_digit(data, first, last):
    data_in = data
    assert first_and_last_digit_of(data_in) == (first, last)




