from seating_system_2 import read_grid, adjacent_occupied_seats_for, \
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


def test_looking_far():
    input = (".......#.\n"
             "...#.....\n"
             ".#.......\n"
             ".........\n"
             "..#L....#\n"
             "....#....\n"
             ".........\n"
             "#........\n"
             "...#.....")
    grid = read_grid(input)
    assert 8 == adjacent_occupied_seats_for(4, 3, grid)


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


# def test_seats_with_4_or_more_neighbours_are_vacated():
#     grid_in = read_grid("#.##.##.##\n"
#                         "#######.##\n"
#                         "#.#.#..#..\n"
#                         "####.##.##\n"
#                         "#.##.##.##\n"
#                         "#.#####.##\n"
#                         "..#.#.....\n"
#                         "##########\n"
#                         "#.######.#\n"
#                         "#.#####.##")
#     grid_out = read_grid("#.LL.L#.##\n"
#                          "#LLLLLL.L#\n"
#                          "L.L.L..L..\n"
#                          "#LLL.LL.L#\n"
#                          "#.LL.LL.LL\n"
#                          "#.LLLL#.##\n"
#                          "..L.L.....\n"
#                          "#LLLLLLLL#\n"
#                          "#.LLLLLL.L\n"
#                          "#.#LLLL.##")
#     assert grid_out == evolve(grid_in)


# def test_untill_stable():
#     grid_in = read_grid("L.LL.LL.LL\n"
#                         "LLLLLLL.LL\n"
#                         "L.L.L..L..\n"
#                         "LLLL.LL.LL\n"
#                         "L.LL.LL.LL\n"
#                         "L.LLLLL.LL\n"
#                         "..L.L.....\n"
#                         "LLLLLLLLLL\n"
#                         "L.LLLLLL.L\n"
#                         "L.LLLLL.LL")
#     grid_out = read_grid("#.#L.L#.##\n"
#                          "#LLL#LL.L#\n"
#                          "L.#.L..#..\n"
#                          "#L##.##.L#\n"
#                          "#.#L.LL.LL\n"
#                          "#.#L#L#.##\n"
#                          "..L.L.....\n"
#                          "#L#L##L#L#\n"
#                          "#.LLLLLL.L\n"
#                          "#.#L#L#.##")
#     assert grid_out == evolve_to_stable(grid_in)


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
