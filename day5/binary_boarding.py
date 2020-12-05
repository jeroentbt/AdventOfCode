def number_from_seatstring(string):
    binary_string = string.replace('B', '1') \
                          .replace('F', '0') \
                          .replace('R', '1') \
                          .replace('L', '0')
    return int(binary_string, 2)

class Seat():
    def __init__(self, seatstring):
        self.row = number_from_seatstring(seatstring[:7])
        self.column = number_from_seatstring(seatstring[7:])
