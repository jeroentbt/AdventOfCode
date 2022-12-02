def score_round(round):
    # A, X = Rock, 1
    # B, Y = Paper, 2
    # C, Z = Scissor, 3

    hands = {"A": {"beats": "C",
                   "score": 1},
             "B": {"beats": "A",
                   "score": 2},
             "C": {"beats": "B",
                   "score": 3}}

    their_play, my_play = round.split(" ")
    my_play = my_play.strip()

    if my_play == "X":
        my_play = "A"
    if my_play == "Y":
        my_play = "B"
    if my_play == "Z":
        my_play = "C"

    score = hands[my_play]["score"]

    if my_play == their_play:
        score += 3
    if hands[my_play]["beats"] == their_play:
        score += 6

    return score


def score_strategized_round(round):
    # A = Rock, 1
    # B = Paper, 2
    # C = Scissor, 3
    # X = lose
    # Y = draw
    # Z = win

    hands = {"A": {"beats": "C",
                   "beaten_by": "B",
                   "score": 1},
             "B": {"beats": "A",
                   "beaten_by": "C",
                   "score": 2},
             "C": {"beats": "B",
                   "beaten_by": "A",
                   "score": 3}}

    their_play, my_play = round.split(" ")
    my_play = my_play.strip()

    if my_play == "X":  # Lose
        score = 0
        my_play = hands[their_play]["beats"]
    if my_play == "Y":  # Draw
        score = 3
        my_play = their_play
    if my_play == "Z":  # Win
        score = 6
        my_play = hands[their_play]["beaten_by"]

    score += hands[my_play]["score"]

    return score



if __name__ == "__main__":
    with open("input.txt") as strategy_guide:
        rounds = strategy_guide.readlines()
        total_points = 0
        for round in rounds:
            total_points += score_round(round)
        print("part 1 " + str(total_points))
        total_points2 = 0
        for round in rounds:
            total_points2 += score_strategized_round(round)
        print("part 2 " + str(total_points2))
