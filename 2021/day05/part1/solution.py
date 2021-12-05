from collections import Counter


def read_coordinates(input):
    return [tuple([tuple([int(x) for x in x_comma_y.split(',')])
                   for x_comma_y in line.split(' -> ')])
            for line in input.splitlines()]


def line_for_coordinates(c):
    a, b = c
    line = []
    if a[1] == b[1]:
        y = a[1]
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            line.append((x, y))
    if a[0] == b[0]:
        x = a[0]
        for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
            line.append((x, y))
    return line


def list_overlaps(coordinates):
    return [point for point, count in Counter(coordinates).items() if count > 1]


def number_of_overlapping_vents(input):
    points = []
    for c in read_coordinates(input):
        points += line_for_coordinates(c)
    return(len(list_overlaps(points)))


if __name__ == "__main__":
    with open("../input.txt") as input:
        input = input.read()
