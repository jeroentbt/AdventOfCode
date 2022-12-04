def parse_section(sectionstring):
    sections = sectionstring.split(',')
    parsed = list()
    for section in sections:
        section = section.strip()
        parts = [int(i) for i in section.split('-')]
        parsed.append(tuple(parts))

    return tuple(parsed)


def complete_overlap(sectionstring):
    s1, s2 = parse_section(sectionstring)
    s1begin, s1end = s1
    s2begin, s2end = s2

    if s1begin >= s2begin and s1end <= s2end:
        return True
    if s2begin >= s1begin and s2end <= s1end:
        return True
    return False


def any_overlap(sectionstring):
    s1, s2 = parse_section(sectionstring)
    s1begin, s1end = s1
    s2begin, s2end = s2

    s1_set = set([*range(s1begin, s1end + 1)])
    s2_set = set([*range(s2begin, s2end + 1)])

    if s1_set.intersection(s2_set):
        return True

    return False



if __name__ == "__main__":
    with open("input.txt") as pairlist:
        lines = pairlist.readlines()
        pairs_that_completely_overlap = [complete_overlap(l) for l in lines]
        print("part 1: " + str(pairs_that_completely_overlap.count(True)))
        pairs_that_overlap = [any_overlap(l) for l in lines]
        print("part 2: " + str(pairs_that_overlap.count(True)))
