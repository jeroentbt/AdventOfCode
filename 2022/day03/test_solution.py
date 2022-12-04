from solution import *
import pytest


def test_compartmentalize():
    input = "ABCDEFGHIJ"
    assert ("ABCDE", "FGHIJ") == compartmentalize(input)


examples = [
    (("vJrwpWtwJgWr", "hcsFMMfFFhFp"), "p"),
    (("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"), "L"),
    (("PmmdzqPrV", "vPwwTWBwg"), "P"),
    (("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"), "v"),
    (("ttgJtRGJ", "QctTZtZT"), "t"),
    (("CrZsJsPPZsGz", "wwsLwLmpwMDw"), "s")
]


@pytest.mark.parametrize("compartments,item", examples)
def test_item_all(compartments, item):
    assert item == item_in_all(compartments)


example_scores = [
    ("p", 16),
    ("L", 38),
    ("P", 42),
    ("v", 22),
    ("t", 20),
    ("s", 19)
]


@pytest.mark.parametrize("item,score", example_scores)
def test_score_items(item, score):
    assert score == score_item(item)


def test_split_list_by_three():
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert [[1, 2, 3],  [4, 5, 6], [7, 8, 9]] == group_by_three(input)
