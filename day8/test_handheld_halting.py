from handheld_halting import read_prog, run_program


def test_read_program():
    input = ("nop +0\n"
             "acc +1")
    assert [('nop', 0, 0), ('acc', 1, 0)] == read_prog(input)


def test_only_accumulators():
    input = [('acc', 1, 0),
             ('acc', 9, 0)]
    assert 10 == run_program(input)


def test_only_accumulators_to_negative():
    input = [('acc', 1, 0),
             ('acc', -11, 0)]
    assert -10 == run_program(input)


def test_nop_does_nothing():
    input = [('acc', 1, 0),
             ('nop', 100, 0),
             ('acc', -11, 0)]
    assert -10 == run_program(input)


def test_first_jump_forward():
    input = [('acc', 1, 0),
             ('jmp', 2, 0),
             ('acc', -100, 0),
             ('acc', 1, 0)]
    assert 2 == run_program(input)


def test_loop_it_should_not():
    input = [('acc', 1, 0),
             ('acc', 1, 0),
             ('jmp', -2, 0)]
    assert 2 == run_program(input)
