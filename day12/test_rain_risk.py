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
    assert 11 == b.waypoint_latitude


def test_move_south():
    b = Boat()
    b.waypoint_latitude = 10
    b.move(("S", 5))
    assert 5 == b.waypoint_latitude


def test_move_east():
    b = Boat()
    b.move(("E", 10))
    assert 20 == b.waypoint_longtitude


def test_move_west():
    b = Boat()
    b.waypoint_longtitude = 10
    b.move(("W", 5))
    assert 5 == b.waypoint_longtitude


def test_turn_right():
    b = Boat()
    b.move(("R", 90))
    assert -10 == b.waypoint_latitude
    assert 1 == b.waypoint_longtitude


def test_turn_left():
    b = Boat()
    b.move(("L", 90))
    assert 10 == b.waypoint_latitude
    assert -1 == b.waypoint_longtitude


def test_move_forward_starting_direction():
    b = Boat()
    b.move(("F", 10))
    assert 100 == b.longtitude
    assert 10 == b.latitude


def test_navigating():
    input = ("F10\n"
             "N3\n"
             "F7\n"
             "R90\n"
             "F11")
    b = Boat()
    b.navigate(read_nav(input))
    assert 214 == abs(b.longtitude)
    assert 72 == abs(b.latitude)


def test_manhattan_distamce():
    input = ("F10\n"
             "N3\n"
             "F7\n"
             "R90\n"
             "F11")
    b = Boat()
    b.navigate(read_nav(input))
    assert 286 == b.manhattan()


def test_navigating_2():
    input = ("F10\n"
             "N3\n"
             "F7\n"
             "L270\n"
             "F11")
    b = Boat()
    b.navigate(read_nav(input))
    assert 214 == abs(b.longtitude)
    assert 72 == abs(b.latitude)


def test_navigating_real_left():
    input = ("F10\n"
             "N3\n"
             "F7\n"
             "L90\n"
             "F11")
    b = Boat()
    b.navigate(read_nav(input))
    assert 126 == abs(b.longtitude)
    assert 148 == abs(b.latitude)


def test_navigating_overturned_left():
    input = ("F10\n"
             "N3\n"
             "F7\n"
             "R270\n"
             "F11")
    b = Boat()
    b.navigate(read_nav(input))
    assert 126 == abs(b.longtitude)
    assert 148 == abs(b.latitude)


def test_navigating_back():
    input = ("F10\n"
             "N3\n"
             "F7\n"
             "R180\n"
             "F11")
    b = Boat()
    b.navigate(read_nav(input))
    assert 60 == abs(b.longtitude)
    assert 6 == abs(b.latitude)
