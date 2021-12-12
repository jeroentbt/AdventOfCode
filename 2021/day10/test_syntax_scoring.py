from syntax_scoring import is_corrupted, part1


def test_simple_chunk_is_legal():
    assert False is is_corrupted('()')


def test_simple_chunk_is_corrupted():
    assert False is not is_corrupted('(]')


def test_nested_chunk_is_legal():
    assert False is is_corrupted('([])')


def test_loose_legal_examples():
    assert False is is_corrupted('([])')
    assert False is is_corrupted('{()()()}')
    assert False is is_corrupted('<([{}])>')
    assert False is is_corrupted('[<>({}){}[([])<>]]')
    assert False is is_corrupted('(((((((((()))))))))).')


def test_loose_corrupted_examples():
    assert False is not is_corrupted('(]')
    assert False is not is_corrupted('{()()()>')
    assert False is not is_corrupted('(((()))}')
    assert False is not is_corrupted('<([]){()}[{}])')


example_input = \
    '[({(<(())[]>[[{[]{<()<>>\n' \
    '[(()[<>])]({[<{<<[]>>(\n' \
    '{([(<{}[<>[]}>{[]{[(<()>\n' \
    '(((({<>}<{<{<>}{[]{[]{}\n' \
    '[[<[([]))<([[{}[[()]]]\n' \
    '[{[{({}]{}}([{[{{{}}([]\n' \
    '{<[[]]>}<{[{[{[]{()[[[]\n' \
    '[<(<(<(<{}))><([]([]()\n' \
    '<{([([[(<>()){}]>(<<{{\n' \
    '<{([{{}}[<[[[<>{}]]]>[]]'


def test_example_count_illegals():
    assert 26397 == part1(example_input)


def test_part1_solution():
    with open("input.txt") as input:
        input = input.read()
    assert 392097 == part1(input)
