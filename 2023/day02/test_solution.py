import pytest
from solution import *

test_input_part1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

games_parsed = [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
     {'n': 1, 'sets': [Rgb(R=4, G=0, B=3), Rgb(R=1, G=2, B=6), Rgb(R=0, G=2, B=0)]},
     True),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
     {'n': 2, 'sets': [Rgb(R=0, G=2, B=1), Rgb(R=1, G=3, B=4), Rgb(R=0, G=1, B=1)]},
     True),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
     {'n': 3, 'sets': [Rgb(R=20, G=8, B=6), Rgb(R=4, G=13, B=5), Rgb(R=1, G=5, B=0)]},
     False),
    ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
     {'n': 4, 'sets': [Rgb(R=3, G=1, B=6), Rgb(R=6, G=3, B=0), Rgb(R=14, G=3, B=15)]},
     False)
]


# only 12 red cubes, 13 green cubes, and 14 blue cubes

@pytest.mark.parametrize("line,parsed,valid", games_parsed)
def test_parse_game(line, parsed, valid):
    assert parse_game(line) == parsed


@pytest.mark.parametrize("line,parsed,valid", games_parsed)
def test_game_is_valid(line, parsed, valid):
    assert game_is_valid(parsed) == valid
