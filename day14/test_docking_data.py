from docking_data import apply_bitmasks


def test_read_one_block_one_number():
    input = ("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n"
             "mem[8] = 11\n")
    mem = apply_bitmasks(input)
    assert 73 == mem[8]
