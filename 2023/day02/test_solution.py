import pytest
from solution import *

test_input_part1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

games_parsed = [("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                 {1: [Rgb(R=4, G=0, B=3), Rgb(R=1, G=2, B=6), Rgb(R=0, G=2, B=0)]}),
                ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                 {2: [Rgb(R=0, G=2, B=1), Rgb(R=1, G=3, B=4), Rgb(R=0, G=1, B=1)]})
                ]


@pytest.mark.parametrize("game,expected", games_parsed)
def test_parse_game(game, expected):
    assert parse_game(game) == expected
