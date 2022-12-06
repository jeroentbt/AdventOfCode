def is_marker(chars):
    return True if len(set(list(chars))) == len(chars) else False


def find_marker(datastream):
    for i in range(4,len(datastream)):
        if is_marker(datastream[i-4:i]):
            return i


if __name__ == "__main__":
    with open("input.txt") as data:
        datastream = data.read()

    print("part 1:")
    print(find_marker(datastream))
