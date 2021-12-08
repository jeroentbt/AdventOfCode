from solution import deltas_to, combined_deltas_to, smallest_combined_delta, \
    fuel_to, combined_fuel_to


def test_list_of_deltas_to_5():
    positions = [1, 2, 5, 16, 4]
    to = 5
    assert [4, 3, 0, 11, 1] == deltas_to(positions, to)


def test_combined_delta_to_5():
    positions = [1, 2, 5, 16, 4]
    to = 5
    assert 19 == combined_deltas_to(positions, to)


def test_example():
    positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert 37 == combined_deltas_to(positions, 2)
    assert 41 == combined_deltas_to(positions, 1)
    assert 39 == combined_deltas_to(positions, 3)
    assert 71 == combined_deltas_to(positions, 10)


def test_cheapest_part1():
    positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert 37 == smallest_combined_delta(positions)


def test_list_of_fuel_to_5():
    deltas = [4, 3, 0, 11, 1]
    assert [10, 6, 0, 66, 1] == fuel_to(deltas)


def test_example_part2():
    positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert 206 == combined_fuel_to(positions, 2)
    assert 168 == combined_fuel_to(positions, 5)
