def read_prog(input):
    program = []
    for line in input.splitlines():
        operation, argument = line.split()
        program.append((operation, int(argument)))
    return program


def run_program(program, result=0, next_step=0):
    operation, argument = program[next_step]
    if operation == 'acc':
        result += argument
        next_step += 1
    if operation == 'nop':
        next_step += 1
    if operation == 'jmp':
        next_step += argument
    if next_step < len(program):
        result = run_program(program, result, next_step)
    return result
