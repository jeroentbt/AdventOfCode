def count_increases(depth_measurements):
    number_of_increases = 0
    for i, measure in enumerate(depth_measurements):
        if i != 0 and measure > depth_measurements[i - 1]:
            number_of_increases += 1
    return number_of_increases


if __name__ == "__main__":
    with open("../input.txt") as depth_report:
        lines = depth_report.readlines()
        lines = [int(line.rstrip()) for line in lines]
        print(count_increases(lines))
