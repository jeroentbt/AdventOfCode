def read_coordinates(input):
    return [tuple([tuple([int(x) for x in x_comma_y.split(',')])
                   for x_comma_y in line.split(' -> ')])
            for line in input.splitlines()]


def line_for_coordinates(c):
    a, b = c
    line = []
    if a[1] == b[1]:
        y = a[1]
        for x in range(a[0], b[0] + 1):
            line.append((x, y))
    if a[0] == b[0]:
        x = a[0]
        for y in range(a[1], b[1] + 1):
            line.append((x, y))
    return line


if __name__ == "__main__":
    with open("../input.txt") as input:
        input = input.read()
