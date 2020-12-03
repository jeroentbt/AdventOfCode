from toboggan_trajectory import thing_at_position, slide, count_trees, multiply_options


def test_report_tree_at_position():
    landscape = "...#"
    position = (0, 3)
    assert "tree" == thing_at_position(landscape, position)


def test_report_snow_at_position():
    landscape = "...#"
    position = (0, 2)
    assert "snow" == thing_at_position(landscape, position)


def test_report_snow_at_position_out_of_bounds():
    landscape = "...#"
    position = (0, 4)
    assert "snow" == thing_at_position(landscape, position)


def test_report_snow_on_second_row():
    landscape = ("####\n"
                 "##.#")
    position = (1, 2)
    assert "snow" == thing_at_position(landscape, position)


def test_moving_vertically():
    landscape = ("####\n"
                 "####")
    slope = (0, 1)
    assert ["tree"] == slide(landscape, slope)


def test_moving_vertically_2():
    landscape = ("####\n"
                 ".###")
    slope = (0, 1)
    assert ["snow"] == slide(landscape, slope)


def test_moving_too_far_vertically():
    landscape = ("####\n"
                 ".###")
    slope = (0, 2)
    assert ["done"] == slide(landscape, slope)


def test_moving_on_a_slope():
    landscape = ("...#.\n"
                 "..#..\n"
                 "#....")
    slope = (2, 1)
    assert ["tree", "snow"] == slide(landscape, slope)


def test_count_trees():
    landscape = ("..##.......\n"
                 "#...#...#..\n"
                 ".#....#..#.\n"
                 "..#.#...#.#\n"
                 ".#...##..#.\n"
                 "..#.##.....\n"
                 ".#.#.#....#\n"
                 ".#........#\n"
                 "#.##...#...\n"
                 "#...##....#\n"
                 ".#..#...#.#")
    slope = (3, 1)
    assert 7 == count_trees(landscape, slope)


def test_multiply_options():
    landscape = ("..##.......\n"
                 "#...#...#..\n"
                 ".#....#..#.\n"
                 "..#.#...#.#\n"
                 ".#...##..#.\n"
                 "..#.##.....\n"
                 ".#.#.#....#\n"
                 ".#........#\n"
                 "#.##...#...\n"
                 "#...##....#\n"
                 ".#..#...#.#")
    slopes = [(1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2)]
    assert 336 == multiply_options(landscape, slopes)
