def is_marker(chars):
    return True if len(set(list(chars))) == len(chars) else False


def find_marker(datastream, length=4):
    for i in range(length, len(datastream)):
        if is_marker(datastream[i-length:i]):
            return i


if __name__ == "__main__":
    with open("input.txt") as data:
        datastream = data.read()

    print("part 1:")
    print(find_marker(datastream))
    print("part 2:")
    print(find_marker(datastream, 14))
