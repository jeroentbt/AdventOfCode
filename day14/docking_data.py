import re


def apply_bitmasks(input):
    mem = {}
    for line in input.splitlines():
        maskline = re.match(r'^mask = ([01X]{36})', line)
        memline = re.match(r'^mem\[(\d+)\] = (\d+)', line)
        if maskline:
            mask = maskline.group(1)
            print(mask)
        if memline:
            address = memline.group(1)
            number = int(memline.group(2))
            number_bin = bin(number)[2:].zfill(36)
            print(address)
            print(number)

            masked_number = []
            for i, n in enumerate(mask):
                if n == 'X':
                    masked_number.append(number_bin[i])
                else:
                    masked_number.append(n)
            mem[int(address)] = int(''.join(masked_number), 2)
    return mem
