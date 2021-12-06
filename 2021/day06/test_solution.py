from solution import fish_after_days, input_to_dict, one_day_later


def test_input_to_dict_one_of_1():
    input = "1"
    assert 1 == input_to_dict(input)[1]


def test_input_to_dict_one_of_each():
    school = input_to_dict("0,1,2,3,4,5,6,7,8")
    assert 1 == school[0]
    assert 1 == school[1]
    assert 1 == school[2]
    assert 1 == school[3]
    assert 1 == school[4]
    assert 1 == school[5]
    assert 1 == school[6]
    assert 1 == school[7]
    assert 1 == school[8]


def test_input_to_dict_two_of_1():
    input = "1,1"
    assert 2 == input_to_dict(input)[1]


def test_age_singles_with_no_spawn():
    input = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}
    expected = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 0}
    assert expected == one_day_later(input)


def test_age_couples_with_no_spawn():
    input = {0: 0, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2}
    expected = {0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 0}
    assert expected == one_day_later(input)


def test_spawning_resets_t_to_6_and_spawns_at_8():
    input = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    assert 1 == one_day_later(input)[6]
    assert 1 == one_day_later(input)[8]


def test_example_18_days():
    input = "3,4,3,1,2"
    assert 26 == fish_after_days(input, 18)


def test_example_80_days():
    input = "3,4,3,1,2"
    assert 5934 == fish_after_days(input, 80)


def test_example_256_days():
    input = "3,4,3,1,2"
    assert 26984457539 == fish_after_days(input, 256)
