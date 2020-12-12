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
