from solution import *
import pytest

testdata = [
    ("A Y", 8),
    ("B X", 1),
    ("C Z", 6)
]

@pytest.mark.parametrize("round,score", testdata)
def test_score_rounds(round, score):
    assert score == score_round(round)
