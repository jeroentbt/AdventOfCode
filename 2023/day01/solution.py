import regex as re
from icecream import ic


def first_n_last_n(input_string, words=True):
    word_to_digit = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    pattern = r'(\d|' + '|'.join(word_to_digit.keys()) + r')'

    digits = [None] * len(input_string)

    for m in re.finditer(pattern, input_string, overlapped=True):
        index = int(m.start())
        digits[index] = m.group()


    digits = [x for x in digits if x]
    f = digits[0]
    first = int(f) if f not in word_to_digit.keys() else word_to_digit.get(f)
    l = digits[-1]
    last = int(l) if l not in word_to_digit.keys() else word_to_digit.get(l)

    return first, last


def sum_of_values(input_file, words=False):
    output_sum = 0
    with open(input_file) as the_input:
        for line in the_input.readlines():
            a, b = first_n_last_n(line, words)
            output_sum += ((10 * a) + b)
    return output_sum
