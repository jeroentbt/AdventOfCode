from seating_system import read_grid, adjacent_occupied_seats_for, \
    evolve, evolve_to_stable, count_occupied_seats


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


def test_number_of_adjacent_occupied_seats_on_empty_floor():
    input = ("...\n"
             ".L.\n"
             "...")
    grid = read_grid(input)
    assert 0 == adjacent_occupied_seats_for(1, 1, grid)


def test_one_seat_taken():
    input = (".#.\n"
             ".L.\n"
             "...")
    grid = read_grid(input)
    assert 1 == adjacent_occupied_seats_for(1, 1, grid)


def test_corners():
    input = (".#.\n"
             ".L.\n"
             "...")
    grid = read_grid(input)
    assert 1 == adjacent_occupied_seats_for(0, 0, grid)
    assert 1 == adjacent_occupied_seats_for(0, 2, grid)
    assert 0 == adjacent_occupied_seats_for(2, 0, grid)
    assert 0 == adjacent_occupied_seats_for(2, 2, grid)


def test_empty_seats_with_no_neighbours_get_occupied():
    grid_in = read_grid("L.LL.LL.LL\n"
                        "LLLLLLL.LL\n"
                        "L.L.L..L..\n"
                        "LLLL.LL.LL\n"
                        "L.LL.LL.LL\n"
                        "L.LLLLL.LL\n"
                        "..L.L.....\n"
                        "LLLLLLLLLL\n"
                        "L.LLLLLL.L\n"
                        "L.LLLLL.LL")
    grid_out = read_grid("#.##.##.##\n"
                         "#######.##\n"
                         "#.#.#..#..\n"
                         "####.##.##\n"
                         "#.##.##.##\n"
                         "#.#####.##\n"
                         "..#.#.....\n"
                         "##########\n"
                         "#.######.#\n"
                         "#.#####.##")
    assert grid_out == evolve(grid_in)


def test_seats_with_4_or_more_neighbours_are_vacated():
    grid_in = read_grid("#.##.##.##\n"
                        "#######.##\n"
                        "#.#.#..#..\n"
                        "####.##.##\n"
                        "#.##.##.##\n"
                        "#.#####.##\n"
                        "..#.#.....\n"
                        "##########\n"
                        "#.######.#\n"
                        "#.#####.##")
    grid_out = read_grid("#.LL.L#.##\n"
                         "#LLLLLL.L#\n"
                         "L.L.L..L..\n"
                         "#LLL.LL.L#\n"
                         "#.LL.LL.LL\n"
                         "#.LLLL#.##\n"
                         "..L.L.....\n"
                         "#LLLLLLLL#\n"
                         "#.LLLLLL.L\n"
                         "#.#LLLL.##")
    assert grid_out == evolve(grid_in)


def test_untill_stable():
    grid_in = read_grid("L.LL.LL.LL\n"
                        "LLLLLLL.LL\n"
                        "L.L.L..L..\n"
                        "LLLL.LL.LL\n"
                        "L.LL.LL.LL\n"
                        "L.LLLLL.LL\n"
                        "..L.L.....\n"
                        "LLLLLLLLLL\n"
                        "L.LLLLLL.L\n"
                        "L.LLLLL.LL")
    grid_out = read_grid("#.#L.L#.##\n"
                         "#LLL#LL.L#\n"
                         "L.#.L..#..\n"
                         "#L##.##.L#\n"
                         "#.#L.LL.LL\n"
                         "#.#L#L#.##\n"
                         "..L.L.....\n"
                         "#L#L##L#L#\n"
                         "#.LLLLLL.L\n"
                         "#.#L#L#.##")
    assert grid_out == evolve_to_stable(grid_in)


def test_count_occupied_seats():
    grid_in = read_grid("#.#L.L#.##\n"
                        "#LLL#LL.L#\n"
                        "L.#.L..#..\n"
                        "#L##.##.L#\n"
                        "#.#L.LL.LL\n"
                        "#.#L#L#.##\n"
                        "..L.L.....\n"
                        "#L#L##L#L#\n"
                        "#.LLLLLL.L\n"
                        "#.#L#L#.##")
    assert 37 == count_occupied_seats(grid_in)
