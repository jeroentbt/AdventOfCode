from binary_boarding import Seat, highest_seat_id
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


def test_highest_seat_id():
    boardingpasses = ['BFFFBBFRRR', 'BBFFBBFRLL', 'FFFBBBFRRR']
    assert 820 == highest_seat_id(boardingpasses)
