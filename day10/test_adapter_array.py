from adapter_array import list_jumps


def test_no_jumps():
    input = [1, 2, 3, 4, 5]
    assert [1, 1, 1, 1] == list_jumps(input)


def test_1_jump_of_2():
    input = [1, 2, 3, 4, 6]
    assert [1, 1, 1, 2] == list_jumps(input)
