from binary_boarding import return_row, return_column

def test_row_number_from_string():
    input = "BFFFBBF"
    assert 70 == return_row(input)


def test_row_number_from_string_2():
    input = 'FFFBBBF'
    assert 14 == return_row(input)


def test_column_number_from_string():
    input = 'RRR'
    assert 7 == return_column(input)


def test_column_number_from_string_2():
    input = 'RLL'
    assert 4 == return_column(input)
