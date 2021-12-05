def read_coordinates(input):
    return [tuple([tuple([int(x) for x in x_comma_y.split(',')])
                   for x_comma_y in line.split(' -> ')])
            for line in input.splitlines()]


def line_for_coordinates(c):
    a, b = c
    line = []
    for x in range(a[0], b[0] + 1):
        line.append((x, a[1]))
    return line


if __name__ == "__main__":
    with open("../input.txt") as input:
        input = input.read()
