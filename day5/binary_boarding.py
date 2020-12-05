class Seat():
    def __init__(self, boardingpass):
        self.row = self.to_number(boardingpass[:7])
        self.column = self.to_number(boardingpass[7:])
        self.ID = (self.row * 8) + self.column


    def to_number(self, string):
        binary_string = string.replace('B', '1') \
                              .replace('F', '0') \
                              .replace('R', '1') \
                              .replace('L', '0')
        return int(binary_string, 2)


def list_seat_ids(boardingpasses):
    list = []
    for boardingpass in boardingpasses:
        seat = Seat(boardingpass)
        list.append(seat.ID)
    return list

def highest_seat_id(boardingpasses):
    highest = 0
    for ID in list_seat_ids(boardingpasses):
        if ID > highest:
            highest = ID
    return highest

if __name__ == "__main__":
    with open("input.txt") as boardingpasses_list:
        boardingpasses = boardingpasses_list.read().splitlines()
        print(highest_seat_id(boardingpasses))
