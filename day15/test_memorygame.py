from memorygame import play_turns


def test_turn_based_just_the_starting_numbers():
    input = [0, 3, 6]
    assert 0 == play_turns(1, input)
