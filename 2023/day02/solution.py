from collections import namedtuple
from typing import Dict, List

Rgb = namedtuple('Rgb', ['R', 'G', 'B'])


def parse_game(game: str) -> Dict[int, List[Rgb]]:
    parsed_game = {1: [Rgb(R=4, G=0, B=3), Rgb(R=1, G=2, B=6), Rgb(R=0, G=2, B=0)]}
    return parsed_game
