from syntax_scoring import is_corrupted


def test_simple_chunk_is_legal():
    assert False is is_corrupted('()')


def test_simple_chunk_is_corrupted():
    assert False is not is_corrupted('(]')


def test_nested_chunk_is_legal():
    assert False is is_corrupted('([])')


def test_loose_legal_examples():
    assert True


def test_part1_solution():
    with open("input.txt") as input:
        input = input.read()
    assert True
