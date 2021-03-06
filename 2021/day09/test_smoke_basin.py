from smoke_basin import low_points, sum_of_risk, basins, solution_part_2


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


def test_part1_example_risk():
    heightmap = \
        "2199943210\n" \
        "3987894921\n" \
        "9856789892\n" \
        "8767896789\n" \
        "9899965678"
    assert 15 == sum_of_risk(heightmap)


def test_part1_solution():
    with open("input.txt") as input:
        input = input.read()
    assert 524 == sum_of_risk(input)


def test_find_1_basin_on_horizontal():
    heightmap = "98719"
    assert 1 == len(basins(heightmap))


def test_find_size_of_1_basin_on_horizontal():
    heightmap = "98719"
    assert 3 == len(basins(heightmap)[0])


def test_part2_example_basins():
    heightmap = \
        "2199943210\n" \
        "3987894921\n" \
        "9856789892\n" \
        "8767896789\n" \
        "9899965678"
    assert 4 == len(basins(heightmap))


def test_part2_example_solution():
    heightmap = \
        "2199943210\n" \
        "3987894921\n" \
        "9856789892\n" \
        "8767896789\n" \
        "9899965678"
    assert 1134 == solution_part_2(heightmap)


def test_part2_solution():
    with open("input.txt") as input:
        input = input.read()
    assert 1235430 == solution_part_2(input)
