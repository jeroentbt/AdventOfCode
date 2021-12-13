from transparent_origami import Paper

example_input = \
    "6,10\n" \
    "0,14\n" \
    "9,10\n" \
    "0,3\n" \
    "10,4\n" \
    "4,11\n" \
    "6,0\n" \
    "6,12\n" \
    "4,1\n" \
    "0,13\n" \
    "10,12\n" \
    "3,4\n" \
    "3,0\n" \
    "8,4\n" \
    "1,10\n" \
    "2,14\n" \
    "8,10\n" \
    "9,0\n" \
    "\n" \
    "fold along y=7\n" \
    "fold along x=5"


def test_printed_grid_is_same_as_example():
    printed_grid = \
        "...#..#..#.\n" \
        "....#......\n" \
        "...........\n" \
        "#..........\n" \
        "...#....#.#\n" \
        "...........\n" \
        "...........\n" \
        "...........\n" \
        "...........\n" \
        "...........\n" \
        ".#....#.##.\n" \
        "....#......\n" \
        "......#...#\n" \
        "#..........\n" \
        "#.#........"
    paper = Paper(example_input)
    assert printed_grid == paper.print()


def test_reading_folds():
    paper = Paper(example_input)
    assert [('y', 7), ('x', 5)] == paper.folds
