def read_grid(input_txt):
    rows = input_txt.splitlines()
    grid = [[position for position in row] for row in rows]
    return grid


def adjacent_occupied_seats_for(row, column, grid):
    occupied = "#"
    number_of_occupied_seats = 0

    nmb_of_rows = len(grid) - 1
    nmb_of_cols = len(grid[0]) - 1

    if row > 0 and column > 0 and \
       grid[row-1][column-1] == occupied:
        number_of_occupied_seats += 1
    if row > 0 and \
       grid[row-1][column] == occupied:
        number_of_occupied_seats += 1
    if row > 0 and column < nmb_of_cols and \
       grid[row-1][column+1] == occupied:
        number_of_occupied_seats += 1

    if column > 0 and \
       grid[row][column-1] == occupied:
        number_of_occupied_seats += 1
    if column < nmb_of_cols and \
       grid[row][column+1] == occupied:
        number_of_occupied_seats += 1

    if row < nmb_of_rows and column > 0 and \
       grid[row+1][column-1] == occupied:
        number_of_occupied_seats += 1
    if row < nmb_of_rows and \
       grid[row+1][column] == occupied:
        number_of_occupied_seats += 1
    if row < nmb_of_rows and column < nmb_of_cols and \
       grid[row+1][column+1] == occupied:
        number_of_occupied_seats += 1
    return number_of_occupied_seats


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
                 adjacent_occupied_seats_for(row_num, col_num, grid) >= 4:
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
