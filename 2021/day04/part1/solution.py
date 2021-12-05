import numpy as np


def prep_input(input):
    input = input.splitlines()
    draws = [int(x) for x in input.pop(0).split(',')]

    boards = []
    current_board = []
    for line in input:
        if line:
            current_board.append([(int(x), 0) for x in line.split()])
        if not line and current_board:
            boards.append(current_board)
            current_board = []
    else:
        boards.append(current_board)
    return draws, boards


def mark_number_on_board(n, board):
    for i in range(0, len(board)):
        board[i] = [(o, 1) if o == n else (o, m) for o, m in board[i]]
    return board


def board_wins(board):
    marked_board = np.array([[m for x, m in row] for row in board])
    for row in marked_board:
        if set(row) == {1}:
            return True
    for i in range(0, len(marked_board[0])):
        if set(marked_board[:, i]) == {1}:
            return True
    return False


def calculate_score(last_number, winning_board):
    unmarked_numbers = []
    for row in winning_board:
        unmarked_numbers += [o if m == 0 else 0 for o, m in row]
    return sum(unmarked_numbers) * last_number


def win_bingo(input):
    draws, boards = prep_input(input)
    for number in draws:
        for i, board in enumerate(boards):
            boards[i] = mark_number_on_board(number, board)
            if board_wins(boards[i]):
                return calculate_score(number, boards[i])


def lose_bingo(input):
    draws, boards = prep_input(input)
    winning_boards = []
    for number in draws:
        for i, board in enumerate(boards):
            boards[i] = mark_number_on_board(number, board)
            if board_wins(boards[i]) and i not in winning_boards:
                winning_boards.append(i)
                if len(boards) == len(winning_boards):
                    return calculate_score(number, boards[i])


if __name__ == "__main__":
    with open("../input.txt") as input:
        input = input.read()
        print("win:", win_bingo(input))
        print("lose:", lose_bingo(input))
