from binary_boarding import number_from_seatstring, Seat

def test_row_number_from_string():
    input = "BFFFBBF"
    assert 70 == number_from_seatstring(input)


def test_row_number_from_string_2():
    input = 'FFFBBBF'
    assert 14 == number_from_seatstring(input)


def test_column_number_from_string():
    input = 'RRR'
    assert 7 == number_from_seatstring(input)


def test_column_number_from_string_2():
    input = 'RLL'
    assert 4 == number_from_seatstring(input)


def test_row_seat():
    input = "BFFFBBFRRR"
    seat = Seat(input)
    assert 70 == seat.row
    assert 7 == seat.column
    assert 567 == seat.ID
