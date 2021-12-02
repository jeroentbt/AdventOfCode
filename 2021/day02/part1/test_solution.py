from solution import position_after_navigation


def test_navigate_0_forward():
    input = "forward 0"
    position = position_after_navigation(input)
    assert position['x'] == 0
    assert position['y'] == 0


def test_navigate_1_forward():
    input = "forward 1"
    position = position_after_navigation(input)
    assert position['x'] == 1
    assert position['y'] == 0


def test_navigate_2_forward_in_1_step():
    input = "forward 2"
    position = position_after_navigation(input)
    assert position['x'] == 2
    assert position['y'] == 0


def test_navigate_2_forward_in_2_step():
    input = "forward 1\nforward 1"
    position = position_after_navigation(input)
    assert position['x'] == 2
    assert position['y'] == 0


def test_navigate_1_down():
    input = "down 1"
    position = position_after_navigation(input)
    assert position['x'] == 0
    assert position['y'] == -1


def test_navigate_2_down_1_up():
    input = "down 2\nup 1"
    position = position_after_navigation(input)
    assert position['x'] == 0
    assert position['y'] == -1


def test_planned_course_1():
    input = "forward 5\n" \
        "down 5\n" \
        "forward 8\n" \
        "up 3\n" \
        "down 8\n" \
        "forward 2"
    position = position_after_navigation(input)
    assert 150 == position['x'] * abs(position['y'])
