def calc_power_consumption(report):
    report_list = report.splitlines()
    report_length = len(report_list)
    gamma_bin_string = ''
    epsilon_bin_string = ''

    columns = [x for x in zip(*report_list)]
    for c in columns:
        column_sum = sum([int(x) for x in c])
        if column_sum > report_length/2:
            gamma_bit = 1
            epsilon_bit = 0
        else:
            gamma_bit = 0
            epsilon_bit = 1
        gamma_bin_string += str(gamma_bit)
        epsilon_bin_string += str(epsilon_bit)

    gamma_rate = int(gamma_bin_string, 2)
    epsilon_rate = int(epsilon_bin_string, 2)

    power_consumption = gamma_rate * epsilon_rate
    return power_consumption


if __name__ == "__main__":
    with open("../input.txt") as report:
        report = report.read()
        print(calc_power_consumption(report))
