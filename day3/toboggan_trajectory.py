def thing_at_position(landscape, position):
    landscape_list = landscape.splitlines()
    row, column = position
    column = column % len(landscape_list[0])
    if landscape_list[row][column] == "#":
        return "tree"
    else:
        return "snow"


def slide(landscape, slope):
    horizontal_movement, vertical_movement = slope
    encountered_landscape = []
    for step in range(1, len(landscape.splitlines())):
        print("step")
        position = (0 + (step * vertical_movement), 0 + (step *horizontal_movement))
        print(landscape)
        print(position)
        print(thing_at_position(landscape, position))
        encountered_landscape.append(thing_at_position(landscape, position))
    return encountered_landscape
