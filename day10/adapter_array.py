def list_jumps(adapters):
    adapters.append(0)  # outlet is 0 jolts
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


def variations(jumps):
    # remove first and last jump (wall outlet and inernal adapter)
    jumps = jumps[1:-1]
    print(jumps)
    if jumps.count(1) == 2:
        return 2
    if jumps.count(1) == 3:
        return 4
    if jumps.count(1) == 4:
        return 5
    if jumps.count(1) == 5:
        return 8
    # for i, jump in enumerate(jumps):

    return 1



if __name__ == '__main__':
    with open('input.txt') as bag_of_adapters:
        list_of_adapters = bag_of_adapters.readlines()
        list_of_adapters = [int(i) for i in list_of_adapters]
    print('the number of 1-jolt differences multiplied by '
          'the number of 3-jolt differences:')
    differences = diffs(list_jumps(list_of_adapters))
    print(differences['one'] * differences['three'])
