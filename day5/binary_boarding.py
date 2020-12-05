def number_from_seatstring(string):
    binary_string = string.replace('B', '1') \
                          .replace('F', '0') \
                          .replace('R', '1') \
                          .replace('L', '0')
    return int(binary_string, 2)
