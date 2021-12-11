from smoke_basin import low_points


def test_find_two_lowest_points_on_horizontal():
    heightmap = "9190"
    assert 2 == len(low_points(heightmap))


def test_find_two_lowest_points_on_grid():
    heightmap = \
        "9990\n" \
        "0998"
    assert 2 == len(low_points(heightmap))
