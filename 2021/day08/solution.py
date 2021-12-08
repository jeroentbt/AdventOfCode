def split_signal_and_output(line):
    signal, output = line.split('|')
    return signal.split(), output.split()


def known_digits(line):
    signal, output = split_signal_and_output(line)
    return sum([1 for digit in output
                if len(digit) in (2, 3, 4, 7)])


def count_known_digits(input):
    return sum(list(map(known_digits, input.splitlines())))


if __name__ == "__main__":
    with open("input.txt") as input:
        input = input.read()
        print("part1:", part1(input))
