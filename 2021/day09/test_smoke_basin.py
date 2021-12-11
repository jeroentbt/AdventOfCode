from smoke_basin import low_points


def test_find_one_lowest_point():
    heightmap = \
        "91\n" \
        "99"
    assert 1 == len(low_points(heightmap))


def test_find_two_lowest_point():
    heightmap = \
        "91\n" \
        "19"
    assert 2 == len(low_points(heightmap))
