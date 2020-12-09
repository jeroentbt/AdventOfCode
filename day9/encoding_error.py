def is_sum_of_2_in(the_sum, the_numbers):
    for n in the_numbers:
        rest = the_sum - n
        if rest in the_numbers and (rest != n or the_numbers.count(n) > 1):
            return True
    return False


def first_number_that_is_not_sum_of_two_in_preamble(preamble, the_list):
    for i, n in enumerate(the_list[preamble:]):
        start_of_preamble = i
        end_of_preamble = i + preamble
        if not is_sum_of_2_in(n, the_list[start_of_preamble:end_of_preamble]):
            return n


if __name__ == "__main__":
    with open("input.txt") as XMASdata:
        XMAS = [int(i) for i in XMASdata.readlines()]
        print(first_number_that_is_not_sum_of_two_in_preamble(25, XMAS))
