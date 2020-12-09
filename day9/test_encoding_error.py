from encoding_error import is_sum_of_2_in, \
    first_number_that_is_not_sum_of_two_in_preamble


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


def test_find_first_number_that_fails_test_1():
    the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 100]
    preamble = 25
    assert 100 == first_number_that_is_not_sum_of_two_in_preamble(preamble, the_list)


def test_find_first_number_that_fails_test_2():
    the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 3, 100]
    preamble = 25
    assert 100 == first_number_that_is_not_sum_of_two_in_preamble(preamble, the_list)


def test_find_first_number_that_fails_test_3():
    the_list = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102,
                117, 150, 182, 127, 219, 299, 277, 309, 576]
    preamble = 5
    assert 127 == first_number_that_is_not_sum_of_two_in_preamble(preamble, the_list)
