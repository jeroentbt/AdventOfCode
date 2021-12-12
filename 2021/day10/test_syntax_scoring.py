from syntax_scoring import is_invalid


def test_simple_chunk_is_valid():
    assert False is is_invalid('()')


def test_part1_solution():
    with open("input.txt") as input:
        input = input.read()
    assert True
