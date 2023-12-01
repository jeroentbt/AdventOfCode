import pytest
from solution import *


example = [("1abc2", 1, 2),
           ("pqr3stu8vwx", 3, 8),
           ("a1b2c3d4e5f", 1, 5),
           ("treb7uchet", 7, 7),
           ("one23", 2, 3)]
@pytest.mark.parametrize("data,first,last", example)
def test_get_first_and_last_digit(data, first, last):
    assert first_n_last_n(data, False) == (first, last)

def test_sum_of_example_values_1():
    assert sum_of_values("input_example.txt", False) == 142

def test_solution_1():
    assert sum_of_values("input.txt", False) == 53386

def test_digits_can_be_written_out():
    example = "two1nine"
    assert first_n_last_n(example) == (2, 9)

def test_words_can_overlap():
    example = "twone"
    assert first_n_last_n(example) == (2, 1)

def test_solution_2():
    assert sum_of_values("input.txt") == 53312
