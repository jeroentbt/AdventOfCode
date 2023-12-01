import re


def first_and_last_digit_of(input_string):
    digits = re.findall(r'\d', input_string)
    return digits[0], digits[-1]
