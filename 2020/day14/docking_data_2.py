import re


def apply_bitmasks(input):
    mem = {}
    for line in input.splitlines():
        maskline = re.match(r'^mask = ([01X]{36})', line)
        memline = re.match(r'^mem\[(\d+)\] = (\d+)', line)
        if maskline:
            mask = maskline.group(1)
            # print(mask)
        if memline:
            address = memline.group(1)
            number = int(memline.group(2))
            address_bin = bin(int(address))[2:].zfill(36)
            # print(address)
            # print(number)

            masked_address = []
            for i, n in enumerate(mask):
                if n == '0':
                    masked_address.append(address_bin[i])
                else:
                    masked_address.append(n)
            address = ''.join(masked_address)
            # mem[int(address)] = int(, 2)

            all_addresses = calculate_all_addresses([address])
            print(all_addresses)
            for a in all_addresses:
                mem = write(a, number, mem)
    return mem


def write(address, value, mem):
    mem[address] = value
    return mem


def calculate_all_addresses(addresses):
    all_addresses = []
    for a in addresses:
        x_pos = a.index('X')
        zero = list(a)
        zero[x_pos] = '0'
        one = list(a)
        one[x_pos] = '1'
        all_addresses.append(''.join(one))
        all_addresses.append(''.join(zero))
    if all_addresses[0].count('X') == 0:
        return [int(a, 2) for a in all_addresses]
    else:
        return calculate_all_addresses(all_addresses)


def sum_of_masked(mem):
    return sum([v for k, v in mem.items()])


if __name__ == "__main__":
    with open("input.txt") as program:
        print(sum_of_masked(apply_bitmasks(program.read())))
