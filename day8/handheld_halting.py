def read_prog(input):
    program = []
    for line in input.splitlines():
        operation, argument = line.split()
        program.append((operation, int(argument), 0))
    return program


def run_program(program, result=0, next_step=0):
    operation, argument, runs = program[next_step]
    if runs == 0:
        program[next_step] = (operation, argument, 1)
        if operation == 'acc':
            result += argument
        next_step += argument if operation == 'jmp' else 1
        if next_step < len(program):
            result = run_program(program, result, next_step)
    return result
