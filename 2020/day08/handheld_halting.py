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
        else:
            print('program terminated succesfully')
    return result


def fix_program(program):
    for i, instruction in enumerate(program):
        modified_program = program.copy()
        operation, argument, runs = instruction
        if operation == 'nop' or operation == 'jmp':
            switcheroo = {'nop': 'jmp',
                          'jmp': 'nop'}
            operation = switcheroo[operation]
            modified_program[i] = (operation, argument, runs)
            print(run_program(modified_program))


if __name__ == "__main__":
    with open("input.txt") as progfile:
        program = read_prog(progfile.read())
        second_run = program.copy()
    print('one run results in:')
    print(run_program(program))
    print('---')
    fix_program(second_run)
