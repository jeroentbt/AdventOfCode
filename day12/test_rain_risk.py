from rain_risk import Boat, read_nav


def test_read_nav():
    input = ("F10\n"
             "N3\n"
             "F7\n"
             "R90\n"
             "F11")
    assert [("F", 10),
            ("N", 3),
            ("F", 7),
            ("R", 90),
            ("F", 11)] == read_nav(input)


def test_move_north():
    b = Boat()
    b.move(("N", 10))
    assert 10 == b.latitude


def test_move_south():
    b = Boat()
    b.latitude = 10
    b.move(("S", 5))
    assert 5 == b.latitude


def test_move_east():
    b = Boat()
    b.move(("E", 10))
    assert 10 == b.longtitude


def test_move_west():
    b = Boat()
    b.longtitude = 10
    b.move(("W", 5))
    assert 5 == b.longtitude


def test_turn_right():
    b = Boat()
    b.move(("R", 90))
    assert 180 == b.facing


def test_turn_left():
    b = Boat()
    b.move(("L", 100))
    assert 350 == b.facing


def test_turn_beyond_360():
    b = Boat()
    b.move(("R", 280))
    assert 10 == b.facing


def test_turn_back_beyond_360():
    b = Boat()
    b.move(("L", 100))
    assert 350 == b.facing


def test_turn_back_beyond_360_2():
    b = Boat()
    b.move(("L", 100))
    b.move(("L", 90))
    assert 260 == b.facing


def test_move_forward_starting_direction():
    b = Boat()
    b.move(("F", 10))
    assert 10 == b.longtitude


def test_move_forward_after_turning_180():
    b = Boat()
    b.move(("L", 180))
    b.move(("F", 10))
    assert -10 == b.longtitude


def test_navigating():
    input = ("F10\n"
             "N3\n"
             "F7\n"
             "R90\n"
             "F11")
    b = Boat()
    b.navigate(read_nav(input))
    assert 17 == abs(b.longtitude)
    assert 8 == abs(b.latitude)


def test_manhattan_distamce():
    input = ("F10\n"
             "N3\n"
             "F7\n"
             "R90\n"
             "F11")
    b = Boat()
    b.navigate(read_nav(input))
    assert 25 == b.manhattan()
