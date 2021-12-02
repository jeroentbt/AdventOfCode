from solution import position_after_navigation


def test_planned_course_1():
    input = "forward 5\n" \
        "down 5\n" \
        "forward 8\n" \
        "up 3\n" \
        "down 8\n" \
        "forward 2"
    position = position_after_navigation(input)
    assert 900 == position['x'] * abs(position['y'])
