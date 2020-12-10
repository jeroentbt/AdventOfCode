def list_jumps(adapters):
    adapters.sort()
    jumps = []
    for i, joltage in enumerate(adapters[:-1]):
        next_joltage = adapters[i+1]
        jumps.append(next_joltage - joltage)
    jumps.append(3)  # internal adapter is 3 jolts higher than highest output
    return jumps


def diffs(jumps):
    diffs = {}
    diffs['one'] = jumps.count(1)
    diffs['two'] = jumps.count(2)
    diffs['three'] = jumps.count(3)
    return diffs
