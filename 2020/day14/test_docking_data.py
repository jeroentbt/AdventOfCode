from docking_data import apply_bitmasks, sum_of_masked


def test_read_one_block_one_number():
    input = ("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n"
             "mem[8] = 11\n")
    mem = apply_bitmasks(input)
    assert 73 == mem[8]


def test_read_one_block_one_other_number():
    input = ("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n"
             "mem[7] = 101\n")
    mem = apply_bitmasks(input)
    assert 101 == mem[7]


def test_read_one_block():
    input = ("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n"
             "mem[8] = 11\n"
             "mem[7] = 101\n"
             "mem[8] = 0\n")
    mem = apply_bitmasks(input)
    assert 101 == mem[7]
    assert 64 == mem[8]


def test_return_sum():
    mem = {7: 101,
             8: 64}
    assert 165 == sum_of_masked(mem)
