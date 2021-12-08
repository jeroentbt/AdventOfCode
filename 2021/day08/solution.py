def split_signal_and_output(line):
    signal, output = line.split('|')
    return signal.split(), output.split()


def known_digits(input):
    known_digits = []
    for digit in input:
        if len(digit) == 2:
            known_digits. append({1, digit})
        if len(digit) == 3:
            known_digits. append({7, digit})
        if len(digit) == 4:
            known_digits. append({4, digit})
        if len(digit) == 7:
            known_digits. append({8, digit})
    return known_digits


def count_known_digits(input):
    count = 0
    for line in input.splitlines():
        signal, output = split_signal_and_output(line)
        count += len(known_digits(output))
    return count


if __name__ == "__main__":
    with open("input.txt") as input:
        input = input.read()
        print("part1:", part1(input))
