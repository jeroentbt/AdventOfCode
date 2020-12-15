from docking_data_2 import apply_bitmasks, sum_of_masked


def test_read_one_block_one_number():
    input = ("mask = 000000000000000000000000000000X1001X\n"
             "mem[42] = 100\n"
             "mem[4113] = 1\n")
    mem = apply_bitmasks(input)

    assert 100 == mem[26]
    assert 100 == mem[27]
    assert 100 == mem[58]
    assert 100 == mem[59]


def test_return_sum():
    mem = {7: 101,
           8: 64}
    assert 165 == sum_of_masked(mem)
