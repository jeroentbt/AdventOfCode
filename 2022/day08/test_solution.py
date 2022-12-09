from solution import *


def test_border_is_visible():
    input = ("111\n"
             "101\n"
             "111")
    assert 8 == visible_trees(input)


def test_all_are_visible():
    input = ("111\n"
             "121\n"
             "111")
    assert 9 == visible_trees(input)


def test_example_part_1():
    input = ("30373\n"
             "25512\n"
             "65332\n"
             "33549\n"
             "35390")
    assert 21 == visible_trees(input)


def test_solution_part_1():
    with open("input.txt") as txt:
        input = txt.read().rstrip()
    assert 1679 == visible_trees(input)


def test_example_part_2():
    input = ("30373\n"
             "25512\n"
             "65332\n"
             "33549\n"
             "35390")
    assert 8 == best_trees_scenic_score(input)


def test_solution_part_2():
    with open("input.txt") as txt:
        input = txt.read().rstrip()
    assert 536625 == best_trees_scenic_score(input)
