class Seat():
    def __init__(self, seatstring):
        self.row = self.to_number(seatstring[:7])
        self.column = self.to_number(seatstring[7:])
        self.ID = (self.row * 8) + self.column


    def to_number(self, string):
        binary_string = string.replace('B', '1') \
                              .replace('F', '0') \
                              .replace('R', '1') \
                              .replace('L', '0')
        return int(binary_string, 2)
