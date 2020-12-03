def thing_at_position(landscape, position):
    landscape_list = landscape.splitlines()
    row, column = position
    column = column % len(landscape_list[0])
    if row >= len(landscape_list):
        return "done"
    elif landscape_list[row][column] == "#":
        return "tree"
    else:
        return "snow"


def slide(landscape, slope):
    horizontal_movement, vertical_movement = slope
    encountered_landscape = []
    for step in range(1, len(landscape.splitlines())):
        position = (0 + (step * vertical_movement), 0 + (step * horizontal_movement))
        encountered_landscape.append(thing_at_position(landscape, position))
    return encountered_landscape


def count_trees(landscape, slope):
    return slide(landscape, slope).count("tree")


def multiply_options(landscape, slopes):
    result = 1
    for slope in slopes:
        print(count_trees(landscape, slope))
        result *= count_trees(landscape, slope)
    return result


if __name__ == "__main__":
    with open("input.txt") as landscape_file:
        landscape = landscape_file.read()
        slope = (3, 1)
        # should be 292
        print(count_trees(landscape, slope))
        slopes = [(1, 1),
                  (3, 1),
                  (5, 1),
                  (7, 1),
                  (1, 2)]
        # should be 9354744432
        print(multiply_options(landscape, slopes))
