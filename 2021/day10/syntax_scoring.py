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
