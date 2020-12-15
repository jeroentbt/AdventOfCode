from memorygame import play_turns


def test_turn_based_just_the_starting_numbers():
    input = [0, 3, 6]
    assert 0 == play_turns(1, input)
    assert 3 == play_turns(2, input)
    assert 6 == play_turns(3, input)


def test_play_4th_turn():
    input = [0, 3, 6]
    assert 0 == play_turns(4, input)


def test_play_5th_turn():
    input = [0, 3, 6]
    assert 3 == play_turns(5, input)
