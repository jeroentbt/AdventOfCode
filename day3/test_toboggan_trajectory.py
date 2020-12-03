from toboggan_trajectory import thing_at_position, slide


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
