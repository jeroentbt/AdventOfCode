from solution import prep_input, win_bingo, mark_number_on_board, board_wins, lose_bingo


def test_prep_input():
    input = "2,5,3,2,4,5,7,4,3\n" \
        "\n" \
        "11 12\n" \
        "13 14\n" \
        "\n" \
        "21 22\n" \
        "23 24\n"
    draws, grids = prep_input(input)
    assert [2,5,3,2,4,5,7,4,3] == draws
    assert [[[(11, 0), (12, 0)],
             [(13, 0), (14, 0)]],
            [[(21, 0), (22, 0)],
             [(23, 0), (24, 0)]]] == grids


def test_mark_board():
    board = [[(1, 0), (2, 0)],
             [(3, 0), (4, 0)]]
    assert [[(1, 1), (2, 0)],
            [(3, 0), (4, 0)]] == mark_number_on_board(1, board)


def test_check_for_win_should_fail():
    board = [[(1, 1), (2, 0)],
             [(3, 0), (4, 0)]]
    assert board_wins(board) is False


def test_check_for_win_should_succeed_on_line():
    board = [[(1, 1), (2, 1)],
             [(3, 0), (4, 0)]]
    assert board_wins(board) is True


def test_check_for_win_should_succeed_on_column():
    board = [[(1, 1), (2, 0)],
             [(3, 1), (4, 0)]]
    assert board_wins(board) is True


def test_check_for_win_should_succeed_on_second_column():
    board = [[(1, 0), (2, 1)],
             [(3, 1), (4, 1)]]
    assert board_wins(board) is True


def test_example():
    input = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n" \
        "\n" \
        "22 13 17 11  0\n" \
        " 8  2 23  4 24\n" \
        "21  9 14 16  7\n" \
        " 6 10  3 18  5\n" \
        " 1 12 20 15 19\n" \
        "\n" \
        " 3 15  0  2 22\n" \
        " 9 18 13 17  5\n" \
        "19  8  7 25 23\n" \
        "20 11 10 24  4\n" \
        "14 21 16 12  6\n" \
        "\n" \
        "14 21 17 24  4\n" \
        "10 16 15  9 19\n" \
        "18  8 23 26 20\n" \
        "22 11 13  6  5\n" \
        " 2  0 12  3  7\n"
    assert 4512 == win_bingo(input)


def test_example():
    input = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n" \
        "\n" \
        "22 13 17 11  0\n" \
        " 8  2 23  4 24\n" \
        "21  9 14 16  7\n" \
        " 6 10  3 18  5\n" \
        " 1 12 20 15 19\n" \
        "\n" \
        " 3 15  0  2 22\n" \
        " 9 18 13 17  5\n" \
        "19  8  7 25 23\n" \
        "20 11 10 24  4\n" \
        "14 21 16 12  6\n" \
        "\n" \
        "14 21 17 24  4\n" \
        "10 16 15  9 19\n" \
        "18  8 23 26 20\n" \
        "22 11 13  6  5\n" \
        " 2  0 12  3  7\n"
    assert 1924 == lose_bingo(input)
