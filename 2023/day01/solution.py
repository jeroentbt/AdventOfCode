import regex as re
from icecream import ic


def first_n_last_n(input_string, words=False):
    word_to_digit = {
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
    first = ""
    last = ""

    if words:
        ic()
        pattern = r'(\d|' + '|'.join(word_to_digit.keys()) + \
                  r'|' + '|'.join(word_to_digit.values()) + r')'

        extremities = [None] * len(input_string)

        for m in re.finditer(pattern, input_string, overlapped=True):
            index = int(m.start())
            extremities[index] = m.group()

        extremities = [x for x in extremities if x]
        f = extremities[0]
        first = f if f.isdigit() else word_to_digit.get(f)
        l = extremities[-1]
        last = l if l.isdigit() else word_to_digit.get(l)
        ic(f,l)
        ic(first, last)


    else:
        for char in input_string:
            if char.isdigit():
                last = char
                if first == "":
                    first = char
    ic(first, last)


    return first, last


def sum_of_values(input_file, words=False):
    output_sum = 0
    with open(input_file) as the_input:
        for line in the_input.readlines():
            output_sum += int("".join(first_n_last_n(line, words)))
    return output_sum
