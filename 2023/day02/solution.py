from collections import namedtuple
from typing import Dict, List
import regex as re
from icecream import ic

Rgb = namedtuple('Rgb', ['R', 'G', 'B'])


def parse_game(game: str) -> Dict[int, List[Rgb]]:
    pattern = r'^Game (?P<game_nr>\d+):(?P<sets>.*)'
    match = re.search(pattern, game)

    if match:
        game_nr = int(match.group("game_nr"))
        sets = [read_set(s) for s in match.group("sets").split(';')]

    else:
        return {}

    parsed_game = {game_nr: sets}
    return parsed_game


def read_set(setstring: str) -> Rgb:
    ic(setstring)
    red = 0
    green = 0
    blue = 0

    for count in setstring.split(','):
        pattern = r'(?P<nr>\d+) (?P<color>red|green|blue)'
        match = re.search(pattern, count)

        if match:
            red = int(match.group("nr")) if match.group("color") == "red" else red
            green = int(match.group("nr")) if match.group("color") == "green" else green
            blue = int(match.group("nr")) if match.group("color") == "blue" else blue

    parsed_set = Rgb(R=red, G=green, B=blue)
    return parsed_set
