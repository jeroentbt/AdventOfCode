from handheld_halting import read_prog, run_program


def test_read_program():
    input = ("nop +0\n"
             "acc +1")
    assert [('nop', 0), ('acc', 1)] == read_prog(input)


def test_only_accumulators():
    input = [('acc', 1),
             ('acc', 9)]
    assert 10 == run_program(input)
