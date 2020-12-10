def list_jumps(adapters):
    adapters.sort()
    jumps = []
    for i, joltage in enumerate(adapters[:-1]):
        next_joltage = adapters[i+1]
        jumps.append(next_joltage - joltage)
    return jumps
