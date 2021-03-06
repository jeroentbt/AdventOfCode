from binary_boarding import Seat, highest_seat_id, missing_seats
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


def test_missing_seats():
    ids = [1, 2, 3, 4, 6]
    assert [5] == missing_seats(ids)


def test_missing_seats_2():
    ids = [1, 2, 3, 5, 6]
    assert [4] == missing_seats(ids)
