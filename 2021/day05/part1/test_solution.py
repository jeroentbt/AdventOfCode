from solution import read_coordinates, \
    line_for_coordinates


def test_read_coordinates_for_2_lines():
    input = "0,0 -> 1,0\n" \
        "3,0 -> 4,0\n"
    expected = [((0, 0), (1, 0)),
                ((3, 0), (4, 0))]
    assert expected == read_coordinates(input)


def test_set_points_of_horizontal_line():
    input = ((0, 0), (4, 0))
    expected = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    assert expected == line_for_coordinates(input)


# def test_example():
#     input = "0,9 -> 5,9\n" \
#         "8,0 -> 0,8\n" \
#         "9,4 -> 3,4\n" \
#         "2,2 -> 2,1\n" \
#         "7,0 -> 7,4\n" \
#         "6,4 -> 2,0\n" \
#         "0,9 -> 2,9\n" \
#         "3,4 -> 1,4\n" \
#         "0,0 -> 8,8\n" \
#         "5,5 -> 8,2\n"
#     assert 5 == number_of_overlapping_vents(input)
