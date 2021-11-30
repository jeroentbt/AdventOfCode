def simpler(list):
    for n1 in list:
        for n2 in list:
            for n3 in list:
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    list = [int(number) for number in lines]
    print(simpler(list))
