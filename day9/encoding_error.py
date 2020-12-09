def is_sum_of_2_in(the_sum, the_numbers):
    for n in the_numbers:
        rest = the_sum - n
        if rest in the_numbers and (rest != n or the_numbers.count(n) > 1):
            return True
    return False
