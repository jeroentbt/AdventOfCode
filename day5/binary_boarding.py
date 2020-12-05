def return_row(rowstring):
    return number_from_seatstring(rowstring)


def return_column(columnstring):
    return number_from_seatstring(columnstring)


def number_from_seatstring(string):
    binary_string = string.replace('B', '1') \
                          .replace('F', '0') \
                          .replace('R', '1') \
                          .replace('L', '0')
    return int(binary_string, 2)
