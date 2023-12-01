import regex as re
from icecream import ic


def first_n_last_n(input_string, words=True):
    word_to_digit = {
        'one': "1",
        'two': "2",
        'three': "3",
        'four': "4",
        'five': "5",
        'six': "6",
        'seven': "7",
        'eight': "8",
        'nine': "9"
    }

    pattern = r'(\d|' + '|'.join(word_to_digit.keys()) + r')'
    digits = [None] * len(input_string)

    for m in re.finditer(pattern, input_string, overlapped=True):
        i = int(m.start())
        match = m.group()
        if match.isdigit():
            digits[i] = match
        if words and match in word_to_digit.keys():
            digits[i] = word_to_digit.get(match)

    digits = [x for x in digits if x]

    first = int(digits[0])
    last = int(digits[-1])

    return first, last


def sum_of_values(input_file, words=True):
    output_sum = 0
    with open(input_file) as the_input:
        for line in the_input.readlines():
            a, b = first_n_last_n(line, words)
            output_sum += ((10 * a) + b)
    return output_sum
