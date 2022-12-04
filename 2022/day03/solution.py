def compartmentalize(rucksack_contents):
    compartment_size = int(len(rucksack_contents)/2)
    compartments = (rucksack_contents[:compartment_size],
                    rucksack_contents[compartment_size:])
    return compartments


def item_in_both_compartments(compartments):
    c1, c2 = compartments
    s1 = set()
    s2 = set()

    for char in c1:
        s1.update(char)
    for char in c2:
        s2.update(char)

    return ''.join(s1.intersection(s2))


def score_item(item):
    scorecard = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return scorecard.index(item)


if __name__ == "__main__":
    with open("input.txt") as sack_contents:
        rucksacks = sack_contents.readlines()
        total = 0
        for rucksack in rucksacks:
            total += score_item(item_in_both_compartments(compartmentalize(rucksack)))
        print("part 1: " + str(total))
