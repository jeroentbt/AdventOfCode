from solution import read_input, parse_state, execute_move


input = ("    [D]    \n"
         "[N] [C]    \n"
         "[Z] [M] [P]\n"
         " 1   2   3\n"
         "\n"
         "move 1 from 2 to 1\n"
         "move 3 from 1 to 3\n"
         "move 2 from 2 to 1\n"
         "move 1 from 1 to 2")


def test_split_state():
    state = read_input(input)
    assert ("    [D]    \n"
            "[N] [C]    \n"
            "[Z] [M] [P]\n"
            " 1   2   3") == state["state"]


def test_parse_state():
    state = ("    [D]    \n"
             "[N] [C]    \n"
             "[Z] [M] [P]\n"
             " 1   2   3")
    assert ["",
            ["Z", "N"],
            ["M", "C", "D"],
            ["P"]] == parse_state(state)


def test_split_procedure():
    state = read_input(input)
    assert ["move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2"] == state["procedure"]


def test_first_move():
    stacks = [False,
              ["Z", "N"],
              ["M", "C", "D"],
              ["P"]]
    procedure = ["move 1 from 2 to 1"]
    assert [False,
            ["Z","N","D"],
            ["M","C"],
            ["P"]] == execute_move(procedure, stacks)


def test_second_move():
    stacks = [False,
            ["Z","N","D"],
            ["M","C"],
            ["P"]]
    procedure = ["move 3 from 1 to 3"]
    assert [False,
            [],
            ["M","C"],
            ["P","D","N","Z"]] == execute_move(procedure, stacks)
