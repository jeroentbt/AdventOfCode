from smoke_basin import low_points


def test_find_two_lowest_points_on_horizontal():
    heightmap = "9190"
    assert 2 == len(low_points(heightmap))


def test_find_two_lowest_points_on_two_row_grid():
    heightmap = \
        "9990\n" \
        "0998"
    assert 2 == len(low_points(heightmap))


def test_find_four_lowest_points_on_two_row_grid():
    heightmap = \
        "2199943210\n" \
        "3987894921\n" \
        "9856789892\n" \
        "8767896789\n" \
        "9899965678"
    assert 4 == len(low_points(heightmap))
