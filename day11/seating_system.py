def read_grid(input_txt):
    rows = input_txt.splitlines()
    grid = [[position for position in row] for row in rows]
    return grid


def adjacent_occupied_seats_for(row, column, grid):
    return 0
