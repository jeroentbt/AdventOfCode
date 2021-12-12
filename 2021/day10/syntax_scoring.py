def is_corrupted(line):
    opened_chunks = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            opened_chunks.append(c)
        if c in [')', ']', '}', '>']:
            should_close = opened_chunks.pop()
            if should_close == '(' and c != ')':
                return c
            if should_close == '[' and c != ']':
                return c
            if should_close == '{' and c != '}':
                return c
            if should_close == '<' and c != '>':
                return c
    return opened_chunks


def missing(input):
    lines = input.splitlines()
    missing_list = []
    for line in lines:
        missing = is_corrupted(line)
        if missing not in [')', ']', '}', '>']:
            missing_list.append(missing)
            # print(missing)
    return missing_list


def part1(input):
    lines = input.splitlines()
    illegals = []
    for line in lines:
        illegals.append(is_corrupted(line))
    # print(illegals)
    syntax_error_score = 0
    for illegal in illegals:
        if illegal == ")":
            syntax_error_score += 3
        if illegal == "]":
            syntax_error_score += 57
        if illegal == "}":
            syntax_error_score += 1197
        if illegal == ">":
            syntax_error_score += 25137
    return syntax_error_score


def score_completion(missing):
    score = 0
    points = {'(': 1,
              '[': 2,
              '{': 3,
              '<': 4}
    for c in reversed(missing):
        score = (score * 5) + points[c]
    return score


def part2(input):
    missing_from_lines = missing(input)
    scores = []
    for needed in missing_from_lines:
        scores.append(score_completion(needed))
    scores = sorted(scores)

    middle = int(float(len(scores))/2 - .5)

    return scores[middle]
