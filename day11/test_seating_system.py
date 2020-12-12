from seating_system import read_grid


def test_read_grid_all_floor():
    input = ("..."
             "..."
             "...")
    grid = read_grid(input)
    assert "." == grid[1][1]
