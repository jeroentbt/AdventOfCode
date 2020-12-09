def is_sum_of_2_in(the_sum, the_numbers):
    for n in the_numbers:
        rest = the_sum - n
        print(rest, the_numbers.count(rest))
        if rest in the_numbers and rest != n:
            return True
    return False
