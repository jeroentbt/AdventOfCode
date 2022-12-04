def compartmentalize(rucksack_contents):
    compartment_size = int(len(rucksack_contents)/2)
    compartments = (rucksack_contents[:compartment_size],
                    rucksack_contents[compartment_size:])
    return compartments


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
        rucksacks = sack_contents.readlines()
        total = 0
        for rucksack in rucksacks:
            total += score_item(item_in_all(compartmentalize(rucksack)))
        print("part 1: " + str(total))
