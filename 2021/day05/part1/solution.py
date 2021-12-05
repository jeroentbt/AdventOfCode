def read_coordinates(input):
    return [tuple([tuple([int(x) for x in x_comma_y.split(',')])
                   for x_comma_y in line.split(' -> ')])
            for line in input.splitlines()]


if __name__ == "__main__":
    with open("../input.txt") as input:
        input = input.read()
