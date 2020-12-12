from seating_system import read_grid, adjacent_occupied_seats_for


def test_read_grid_all_floor():
    input = ("...\n"
             "...\n"
             "...")
    grid = read_grid(input)
    assert "." == grid[0][0]


def test_read_grid_one_seat():
    input = ("...\n"
             ".L.\n"
             "...")
    grid = read_grid(input)
    assert "." == grid[0][0]
    assert "L" == grid[1][1]


def test_number_of_adjacent_occupied_seats():
    input = ("...\n"
             ".L.\n"
             "...")
    grid = read_grid(input)
    assert 0 == adjacent_occupied_seats_for(1, 1, grid)
