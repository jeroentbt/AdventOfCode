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
    assert -10 == b.facing


def test_move_forward_starting_direction():
    b = Boat()
    b.move(("F", 10))
    assert 10 == b.longtitude
