def compartmentalize(rucksack_contents):
    compartment_size = int(len(rucksack_contents)/2)
    compartments = (rucksack_contents[:compartment_size],
                    rucksack_contents[compartment_size:])
    return compartments


def group_by_three(rucksacks):
    return [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]


def item_in_all(groups):
    groups = list(groups)

    intersection = set()
    for c in groups:
        s = set()
        for char in c:
            s.update(char)
        if not intersection:
            intersection = s
        else:
            intersection = intersection.intersection(s)

    return ''.join(intersection)


def score_item(item):
    scorecard = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return scorecard.index(item)


if __name__ == "__main__":
    with open("input.txt") as sack_contents:
        rucksacks = [l.strip() for l in sack_contents.readlines()]

        total = 0
        for rucksack in rucksacks:
            total += score_item(item_in_all(compartmentalize(rucksack)))
        print("part 1: " + str(total))

        total2 = 0
        for group in group_by_three(rucksacks):
            total2 += score_item(item_in_all(group))
        print("part 2: " + str(total2))
