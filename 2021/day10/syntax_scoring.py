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
    return False


def part1(input):
    lines = input.splitlines()
    illegals = []
    for line in lines:
        illegals.append(is_corrupted(line))
    print(illegals)
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
