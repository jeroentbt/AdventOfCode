from binary_boarding import return_row

def test_row_number_from_string():
    input = "BFFFBBF"
    assert 70 == return_row(input)


def test_row_number_from_string_2():
    input = 'FFFBBBF'
    assert 14 == return_row(input)
