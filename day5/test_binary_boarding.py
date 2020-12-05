from binary_boarding import return_row, return_column, number_from_seatstring

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
