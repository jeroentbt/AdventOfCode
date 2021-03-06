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
    variations = 1
    print(jumps)
    for seq in split_jumps(jumps):
        print(seq)
        if seq.count('1') == 2:
            the_number = 2
        elif seq.count('1') == 3:
            the_number = 4
        elif seq.count('1') == 4:
            the_number = 7
        # for i, jump in enumerate(jumps):
        else:
            the_number = 0

        if the_number != 0:
            variations = variations * the_number
    return variations


def split_jumps(jumps):
    jumps = [str(i) for i in jumps]
    jumpstring = ''.join(jumps)
    jump_parts = jumpstring.split('3')
    jump_parts = [seq for seq in jump_parts if seq != '']
    return jump_parts


if __name__ == '__main__':
    with open('input.txt') as bag_of_adapters:
        list_of_adapters = bag_of_adapters.readlines()
        list_of_adapters = [int(i) for i in list_of_adapters]
    print('the number of 1-jolt differences multiplied by '
          'the number of 3-jolt differences:')
    differences = diffs(list_jumps(list_of_adapters))
    print(differences['one'] * differences['three'])
    print('possible variations')
    print(variations(list_jumps(list_of_adapters)))
