def read_coordinates(input):
    input = input.splitlines()
    list_of_coordinates = []
    for line in input:
        c = tuple([tuple([int(x) for x in x_comma_y.split(',')])
             for x_comma_y in line.split(' -> ')])

        list_of_coordinates.append(c)

    return list_of_coordinates


if __name__ == "__main__":
    with open("../input.txt") as input:
        input = input.read()
