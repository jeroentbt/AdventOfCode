def thing_at_position(landscape, position):
    landscape_list = landscape.splitlines()
    row, column = position
    column = column % len(landscape_list[0])
    if landscape_list[row][column] == "#":
        return "tree"
    else:
        return "snow"
