def read_prog(input):
    program = []
    for line in input.splitlines():
        operation, argument = line.split()
        program.append((operation, int(argument)))
    return program


def run_program(program):
    result = 0
    for operation_, argument in program:
        result += argument
    return result
