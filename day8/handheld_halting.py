def read_prog(input):
    program = []
    for line in input.splitlines():
        operation, argument = line.split()
        program.append((operation, int(argument)))
    return program


def run_program(program):
    return 10
