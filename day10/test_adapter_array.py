from adapter_array import list_jumps, diffs


def test_no_jumps():
    input = [1, 2, 3, 4, 5]
    assert [1, 1, 1, 1, 1, 3] == list_jumps(input)


def test_1_jump_of_2():
    input = [1, 2, 3, 4, 6]
    assert [1, 1, 1, 1, 2, 3] == list_jumps(input)


def test_1_jump_of_2_unordered():
    input = [1, 6, 3, 4, 2]
    assert [1, 1, 1, 1, 2, 3] == list_jumps(input)


def test_return_number_of_differences():
    input = [1, 1, 2, 1, 3]
    assert {'one': 3, 'two': 1, 'three': 1} == diffs(input)


def test_given_example_1():
    adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    differences = diffs(list_jumps(adapters))
    assert 7 == differences['one']
    assert 5 == differences['three']


def test_given_example_2():
    adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
    differences = diffs(list_jumps(adapters))
    assert 22 == differences['one']
    assert 10 == differences['three']
