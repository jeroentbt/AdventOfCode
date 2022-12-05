def read_input(input):
    i = input.split("\n\n")
    return {"state": i[0],
            "procedure": i[1].rstrip().split('\n')}


def parse_state(state_string):
    stack_rows = state_string.split('\n')
    stacks = [[""]]
    column_identifiers = stack_rows.pop()
    stack_rows.reverse()

    for n in range(len(column_identifiers)):
        if column_identifiers[n] != " ":
            stack = ""
            for row in stack_rows:
                stack += row[n]
            stacks.append(list(stack.rstrip()))
    return stacks


def execute_move(procedure, stacks):
    p = procedure[0].split(" ")

    move_ = int(p[1])
    from_ = int(p[3])
    to_ = int(p[5])

    pick_up = stacks[from_][-move_:]
    stacks[from_] = stacks[from_][:-move_]
    pick_up.reverse() # remove for part 2
    stacks[to_] = stacks[to_] + pick_up

    procedure = procedure[1:]

    if len(procedure) > 0:
        stacks = execute_move(procedure, stacks)

    return stacks


if __name__ == "__main__":
    with open("input.txt") as cargo:
        lines = cargo.read()

    print("part 1:")
    input = read_input(lines)
    stacks = parse_state(input["state"])
    stacks = execute_move(input["procedure"], stacks)
    output = ""

    for s in stacks:
        if s[-1]:
            output += s[-1]
    print(output)
