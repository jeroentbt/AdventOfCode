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



if __name__ == "__main__":
    with open("input.txt") as strategy_guide:
        rounds = strategy_guide.readlines()
        total_points = 0
        for round in rounds:
            total_points += score_round(round)
        print(total_points)
