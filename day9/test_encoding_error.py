from encoding_error import is_sum_of_2_in


def test_is_sum_of_2():
    the_sum = 10
    the_numbers = [2, 8]
    assert True == is_sum_of_2_in(the_sum, the_numbers)
