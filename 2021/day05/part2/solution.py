from collections import Counter


def read_coordinates(input):
    return [tuple([tuple([int(x) for x in x_comma_y.split(',')])
                   for x_comma_y in line.split(' -> ')])
            for line in input.splitlines()]


def line_for_coordinates(c):
    point_a, point_b = c

    x_direction = 1 if point_b[0] >= point_a[0] else -1
    y_direction = 1 if point_b[1] >= point_a[1] else -1

    list_of_x = [*range(point_a[0], point_b[0] + x_direction, x_direction)]
    list_of_y = [*range(point_a[1], point_b[1] + y_direction, y_direction)]

    if len(list_of_y) == 1:
        list_of_y = list_of_y * len(list_of_x)
    if len(list_of_x) == 1:
        list_of_x = list_of_x * len(list_of_y)

    return list(zip(list_of_x, list_of_y))


def list_overlaps(coordinates):
    return [point for point, count in Counter(coordinates).items() if count > 1]


def number_of_overlapping_vents(input):
    points = []
    for c in read_coordinates(input):
        points += line_for_coordinates(c)
    return(len(list_overlaps(points)))


if __name__ == "__main__":
    with open("../input.txt") as input:
        print(number_of_overlapping_vents(input.read()))
