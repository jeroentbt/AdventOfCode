def read_grid(input_txt):
    rows = input_txt.splitlines()
    grid = [[position for position in row] for row in rows]
    return grid


def adjacent_occupied_seats_for(row, column, grid):
    number_of_occupied_seats = 0

    if seat_in_direction_occupied(row, column, -1, -1, grid):
        number_of_occupied_seats += 1
    if seat_in_direction_occupied(row, column, -1, 0, grid):
        number_of_occupied_seats += 1
    if seat_in_direction_occupied(row, column, -1, 1, grid):
        number_of_occupied_seats += 1

    if seat_in_direction_occupied(row, column, 0, -1, grid):
        number_of_occupied_seats += 1
    if seat_in_direction_occupied(row, column, 0, 1, grid):
        number_of_occupied_seats += 1

    if seat_in_direction_occupied(row, column, 1, -1, grid):
        number_of_occupied_seats += 1
    if seat_in_direction_occupied(row, column, 1, 0, grid):
        number_of_occupied_seats += 1
    if seat_in_direction_occupied(row, column, 1, 1, grid):
        number_of_occupied_seats += 1
    return number_of_occupied_seats


def seat_in_direction_occupied(row, column, horizontal, vertical, grid):
    occupied = "#"
    empty = "L"

    nmb_of_rows = len(grid)
    nmb_of_cols = len(grid[0])

    row += vertical
    column += horizontal

    if 0 <= row < nmb_of_rows and \
       0 <= column < nmb_of_cols:
        position = grid[row][column]
        if position == occupied:
            return True
        if position == empty:
            return False
    else:
        return False

    return seat_in_direction_occupied(row, column, horizontal, vertical, grid)


def evolve(grid):
    evolved_grid = []
    for row_num, row in enumerate(grid):
        evolved_grid.append([])
        for col_num, position in enumerate(row):
            evolved_grid[row_num].append("")
            if position == "L" and \
               adjacent_occupied_seats_for(row_num, col_num, grid) == 0:
                evolved_grid[row_num][col_num] = "#"
            elif position == "#" and \
                 adjacent_occupied_seats_for(row_num, col_num, grid) >= 5:
                evolved_grid[row_num][col_num] = "L"
            else:
                evolved_grid[row_num][col_num] = grid[row_num][col_num]
    return evolved_grid


def evolve_to_stable(grid):
    new_grid = evolve(grid)
    if new_grid == grid:
        return grid
    else:
        return evolve_to_stable(new_grid)


def count_occupied_seats(grid):
    seats = 0
    for row in grid:
        seats += ''.join(row).count('#')
    return seats


if __name__ == "__main__":
    with open("input.txt") as input_txt:
        grid_as_text = input_txt.read()
        print((count_occupied_seats(evolve_to_stable(read_grid(grid_as_text)))))
