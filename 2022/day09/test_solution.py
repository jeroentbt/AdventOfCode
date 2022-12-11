from solution import Rope
import pytest


stretched_one_step_moves = [((1, 0), (0, 0), "R 1", (1, 0)),
                            ((1, 0), (2, 0), "L 1", (1, 0)),
                            ((0, 1), (0, 0), "U 1", (0, 1)),
                            ((0, 1), (0, 2), "D 1", (0, 1)),
                            ((1, 0), (0, 0), "L 1", (0, 0))]


@pytest.mark.parametrize("head,tail,motion,tailresult",
                         stretched_one_step_moves)
def test_straight_one_inline_move(head, tail, motion, tailresult):
    r = Rope(head, tail)
    r.move_head(motion)
    assert tailresult == r.get_tail_position()


def test_straight_two_inline_moves():
    r = Rope((1, 0),
             (0, 0))
    r.move_head("R 2")
    assert (2, 0) == r.get_tail_position()


def test_bundled_one_move():
    r = Rope((0, 0),
             (0, 0))
    r.move_head("R 1")
    assert (0, 0) == r.get_tail_position()


def test_straight_one_sidemove():
    r = Rope((0, 1),
             (0, 0))
    r.move_head("R 1")
    assert (0, 0) == r.get_tail_position()


def test_diagonal_one_away_move():
    r = Rope((1, 1),
             (0, 0))
    r.move_head("R 1")
    assert (1, 1) == r.get_tail_position()


def test_example_1():
    r = Rope()
    moves = ["R 4",
             "U 4",
             "L 3",
             "D 1",
             "R 4",
             "D 1",
             "L 5",
             "R 2"]
    for m in moves:
        r.move_head(m)
    assert 13 == r.unique_tail_positions()


def test_solution_1():
    with open("input.txt") as input:
        motions = input.readlines()
    r = Rope()
    for m in motions:
        r.move_head(m)
    assert 6284 == r.unique_tail_positions()
