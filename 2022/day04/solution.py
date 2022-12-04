def parse_section(sectionstring):
    sections = sectionstring.split(',')
    parsed = list()
    for section in sections:
        section = section.strip()
        parts = [int(i) for i in section.split('-')]
        parsed.append(tuple(parts))

    return tuple(parsed)


def contains(sectionstring):
    s1, s2 = parse_section(sectionstring)
    s1begin, s1end = s1
    s2begin, s2end = s2

    if s1begin >= s2begin and s1end <= s2end:
        return True
    if s2begin >= s1begin and s2end <= s1end:
        return True
    return False


if __name__ == "__main__":
    with open("input.txt") as pairlist:
        pairs_that_contain = [contains(l) for l in pairlist.readlines()]
        print("part 1: " + str(pairs_that_contain.count(True)))
