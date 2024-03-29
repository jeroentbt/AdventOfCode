from solution import *
import pytest

def test_parse_section():
    sectionstring = "2-4,6-8"
    assert ((2, 4), (6, 8)) == parse_section(sectionstring)


def test_one_does_not_contain_two():
    sections = "2-4,6-8"
    assert False == complete_overlap(sections)


def test_one_does_contain_two():
    sections = "2-8,3-7"
    assert True == complete_overlap(sections)


part1 = [
    ("2-4,6-8", False),
    ("2-3,4-5", False),
    ("5-7,7-9", False),
    ("2-8,3-7", True),
    ("6-6,4-6", True),
    ("2-6,4-8", False)
]


@pytest.mark.parametrize("string,result", part1)
def test_example_part1(string, result):
    assert result == complete_overlap(string)


part2 = [
    ("2-4,6-8", False),
    ("2-3,4-5", False),
    ("5-7,7-9", True),
    ("2-8,3-7", True),
    ("6-6,4-6", True),
    ("2-6,4-8", True)
]


@pytest.mark.parametrize("string,result", part2)
def test_example_part2(string, result):
    assert result == any_overlap(string)
