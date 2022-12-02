from solution import *
import pytest

testdata_1 = [
    ("A Y", 8),
    ("B X", 1),
    ("C Z", 6)
]

@pytest.mark.parametrize("round,score", testdata_1)
def test_score_rounds(round, score):
    assert score == score_round(round)


testdata_2 = [
    ("A Y", 4),
    ("B X", 1),
    ("C Z", 7)
]

@pytest.mark.parametrize("round,score", testdata_2)
def test_score_rounds_2(round, score):
    assert score == score_strategized_round(round)
