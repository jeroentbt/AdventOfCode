from solution import is_marker, find_marker
import pytest


def test_is_a_marker():
    input = "abcd"
    assert True == is_marker(input)


def test_is_not_a_marker():
    input = "abca"
    assert False == is_marker(input)


example = [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
           ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
           ("nppdvjthqldpwncqszvftbrmjlhg", 6),
           ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
           ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)]


@pytest.mark.parametrize("data,solution", example)
def test_find_end_of_marker(data, solution):
    assert solution == find_marker(data)


example = [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
           ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
           ("nppdvjthqldpwncqszvftbrmjlhg", 23),
           ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
           ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)]


@pytest.mark.parametrize("data,solution", example)
def test_find_end_of_marker(data, solution):
    assert solution == find_marker(data, 14)
