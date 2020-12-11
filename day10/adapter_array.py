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


def possibilities(jumps):
    return 0



if __name__ == '__main__':
    with open('input.txt') as bag_of_adapters:
        list_of_adapters = bag_of_adapters.readlines()
        list_of_adapters = [int(i) for i in list_of_adapters]
    print('the number of 1-jolt differences multiplied by '
          'the number of 3-jolt differences:')
    differences = diffs(list_jumps(list_of_adapters))
    print(differences['one'] * differences['three'])
