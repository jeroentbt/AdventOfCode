def known_digits_in(line):
    return sum([1 for x in line.split('|')[1].split()
                if len(x) in (2, 3, 4, 7)])


def part1(input):
    return sum(list(map(known_digits_in, input.splitlines())))


if __name__ == "__main__":
    with open("input.txt") as input:
        input = input.read()
        print("part1:", part1(input))
