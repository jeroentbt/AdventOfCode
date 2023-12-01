import re
from icecream import ic


def first_and_last_digit_of(input_string, also_recognise_words=False):
    word_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    if also_recognise_words:
        pattern = r'\d|' + '|'.join(word_to_digit.keys())
    else:
        pattern = r'\d'
    digits = re.findall(pattern, input_string)
    # ic(digits)
    first = word_to_digit.get(digits[0], digits[0])
    last = word_to_digit.get(digits[-1], digits[-1])
    return first, last


def sum_of_values(input_file):
    output_sum = 0
    with open(input_file) as the_input:
        for line in the_input.readlines():
            output_sum += int("".join(first_and_last_digit_of(line)))
    return output_sum
