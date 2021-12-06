def fish_after_days(input, days):
    school = input_to_dict(input)
    for i in range(0, days):
        school = one_day_later(school)
    return sum(school.values())


def input_to_dict(input):
    school = dict.fromkeys([*range(0, 9)], 0)
    for t in [int(x) for x in input.split(",")]:
        school[t] += 1
    return school


def one_day_later(younger):
    older = {}
    older[0] = younger[1]
    older[1] = younger[2]
    older[2] = younger[3]
    older[3] = younger[4]
    older[4] = younger[5]
    older[5] = younger[6]
    older[6] = younger[7] + younger[0]
    older[7] = younger[8]
    older[8] = younger[0]

    return older


if __name__ == "__main__":
    with open("input.txt") as input:
        input = input.read()
        print("part1,  80 days:", fish_after_days(input, 80))
        print("part2, 256 days:", fish_after_days(input, 256))
