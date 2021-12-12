from syntax_scoring import is_corrupted, chunkify


def test_simple_chunk_is_valid():
    assert False is is_corrupted('()')


def test_simple_chunk_is_corrupted():
    assert True is is_corrupted('(]')


def test_chunkify_one_chunk():
    assert ['()'] == chunkify('()')


def test_part1_solution():
    with open("input.txt") as input:
        input = input.read()
    assert True
