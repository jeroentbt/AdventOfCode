import re


def first_and_last_digit_of(input_string):
    digits = re.findall(r'\d', input_string)
    return digits[0], digits[-1]

def sum_of_values(input_file):
    sum = 0
    with open(input_file) as the_input:
        for line in the_input.readlines():
            sum += int("".join(first_and_last_digit_of(line)))
    return sum

