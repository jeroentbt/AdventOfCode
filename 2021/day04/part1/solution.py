import numpy as np


def prep_input(input):
    input = input.splitlines()
    draws = [int(x) for x in input.pop(0).split(',')]

    boards = []
    current_board = []
    for line in input:
        line = line.split()
        if len(line) == 0 and len(current_board) != 0:
            boards.append(current_board)
            current_board = []
        if len(line) > 0:
            current_board.append([(int(x), 0) for x in line])
    boards.append(current_board)
    return draws, boards


def mark_board(n, board):
    for i in range(0, len(board)):
        board[i] = [(o, 1) if o == n else (o, m) for o, m in board[i]]
    return board


def board_wins(board):
    board = np.array([[m for x, m in line] for line in board])
    for line in board:
        if set(line) == {1}:
            return True
    for i in range(0, len(board[0])):
        if set(board[:, i]) == {1}:
            return True
    return False


def calculate_score(number, winning_board):
    unmarked = []
    for line in winning_board:
        unmarked += [o if m == 0 else 0 for o, m in line]
    return sum(unmarked) * number


def win_bingo(input):
    draws, boards = prep_input(input)

    for i_n, number in enumerate(draws):
        for i_b, board in enumerate(boards):
            boards[i_b] = mark_board(number, board)
            if board_wins(boards[i_b]):
                score = calculate_score(number, boards[i_b])
                return score


def lose_bingo(input):
    draws, boards = prep_input(input)
    winning_boards = []
    for i_n, number in enumerate(draws):
        for i_b, board in enumerate(boards):
            boards[i_b] = mark_board(number, board)
            if board_wins(boards[i_b]) and i_b not in winning_boards:
                if len(boards) - len(winning_boards) == 1:
                    score = calculate_score(number, boards[i_b])
                    return score
                winning_boards.append(i_b)


if __name__ == "__main__":
    with open("../input.txt") as input:
        input = input.read()
        print("win:", win_bingo(input))
        print("lose:", lose_bingo(input))
