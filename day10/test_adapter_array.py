from adapter_array import list_jumps, diffs


def test_no_jumps():
    input = [1, 2, 3, 4, 5]
    assert [1, 1, 1, 1, 3] == list_jumps(input)


def test_1_jump_of_2():
    input = [1, 2, 3, 4, 6]
    assert [1, 1, 1, 2, 3] == list_jumps(input)


def test_1_jump_of_2_unordered():
    input = [1, 6, 3, 4, 2]
    assert [1, 1, 1, 2, 3] == list_jumps(input)


def test_return_number_of_differences():
    input = [1, 1, 2, 1, 3]
    assert {'one': 3, 'two': 1, 'three': 1} == diffs(input)
