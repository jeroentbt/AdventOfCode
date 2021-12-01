def count_increases(depths):
    window_size = 3
    number_of_increases = 0
    max_i = len(depths) - (window_size - 1)

    for i, measure in enumerate(depths):
        if i > 0 and i < (max_i):
            this_window = sum(depths[i:i+window_size])
            previous_window = sum(depths[i-1:i-1+window_size])
            if this_window > previous_window:
                number_of_increases += 1
    return number_of_increases


if __name__ == "__main__":
    with open("../input.txt") as depth_report:
        lines = depth_report.readlines()
        lines = [int(line.rstrip()) for line in lines]
        print(count_increases(lines))
