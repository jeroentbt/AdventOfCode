from handheld_halting import read_prog


def test_read_program():
    input = ("nop +0\n"
             "acc +1")
    assert [('nop', 0), ('acc', 1)] == read_prog(input)
