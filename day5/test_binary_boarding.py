from binary_boarding import Seat

def test_row_seat():
    input = "BFFFBBFRRR"
    seat = Seat(input)
    assert 70 == seat.row
    assert 7 == seat.column
    assert 567 == seat.ID
