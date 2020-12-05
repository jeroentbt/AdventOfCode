from binary_boarding import Seat
import pytest

@pytest.mark.parametrize("boardingpass, row, column, ID",
                         [('BFFFBBFRRR', 70, 7, 567),
                          ('FFFBBBFRRR', 14, 7, 119),
                          ('BBFFBBFRLL', 102, 4, 820)])


def test_row_seat(boardingpass, row, column, ID):
    seat = Seat(boardingpass)
    assert row == seat.row
    assert column == seat.column
    assert ID == seat.ID
