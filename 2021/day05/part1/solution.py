def read_coordinates(input):
    input = input.splitlines()
    list_of_coordinates = []
    for line in input:
        ventlines_text = line.split(' -> ')
        c_start = tuple([int(x) for x in ventlines_text[0].split(',')])
        c_end = tuple([int(x) for x in ventlines_text[1].split(',')])
        list_of_coordinates.append(tuple([c_start, c_end]))

    return list_of_coordinates


if __name__ == "__main__":
    with open("../input.txt") as input:
        input = input.read()
