from encoding_error import is_sum_of_2_in


def test_is_sum_of_2():
    the_sum = 10
    the_numbers = [2, 8]
    assert True == is_sum_of_2_in(the_sum, the_numbers)


def test_is_not_sum_of_2():
    the_sum = 10
    the_numbers = [1, 8]
    assert False == is_sum_of_2_in(the_sum, the_numbers)


def test_is_sum_of_2_in_3():
    the_sum = 10
    the_numbers = [2, 8, 1]
    assert True == is_sum_of_2_in(the_sum, the_numbers)


def test_is_not_sum_of_2_in_3():
    the_sum = 10
    the_numbers = [5, 8, 1]
    assert False == is_sum_of_2_in(the_sum, the_numbers)


def test_is_sum_of_2_of_the_same_in_3():
    the_sum = 10
    the_numbers = [5, 8, 5]
    assert True == is_sum_of_2_in(the_sum, the_numbers)
