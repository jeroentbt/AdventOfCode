def split_signal_and_output(line):
    signal, output = line.split('|')
    return signal.split(), output.split()


def known_digits(input):
    known_digits = {}
    for digit in input:
        digit = set(digit)
        if len(digit) == 2:
            known_digits[1] = digit
        if len(digit) == 3:
            known_digits[7] = digit
        if len(digit) == 4:
            known_digits[4] = digit
        if len(digit) == 7:
            known_digits[8] = digit
    return known_digits


def count_known_digits(input):
    count = 0
    for line in input.splitlines():
        signal, output = split_signal_and_output(line)
        for digit in output:
            count += 1 if len(digit) in (2, 3, 4, 7) else 0
    return count


def read_display(input):
    for line in input.splitlines():
        signal, output = split_signal_and_output(line)
        known = known_digits(signal)
        known[9] = find_9(signal, known)
    return 0


def find_9(signal, known):
    # 3 digits have 6 segments: 0, 6, 9
    # 9 is the only one that has all segments of 4
    for digit in [set(x) for x in signal if len(x) == 6]:
        if known[4].issubset(digit):
            return digit


def find_0(signal, known):
    # 3 digits have 6 segments: 0, 6, 9
    # 0 is the only one that has all segments of 1
    for digit in [set(x) for x in signal if len(x) == 6]:
        if known[1].issubset(digit) and \
           known[9] != digit:
            return digit


if __name__ == "__main__":
    with open("input.txt") as input:
        input = input.read()
        print("part1:", count_known_digits(input))
