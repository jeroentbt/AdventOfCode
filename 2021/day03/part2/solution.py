def calc_life_support_rating(report):
    report_list = report.splitlines()
    report_length = len(report_list)

    columns = [x for x in zip(*report_list)]

    valid_oxy_indexes = [*range(0, report_length)]
    valid_co2_indexes = [*range(0, report_length)]

    for c in columns:

        column_sum_oxy = sum([int(x)
                              for i, x in enumerate(c)
                              if i in valid_oxy_indexes])
        valid_oxy = 1 if column_sum_oxy >= len(valid_oxy_indexes)/2 else 0
        column_sum_co2 = sum([int(x)
                              for i, x in enumerate(c)
                              if i in valid_co2_indexes])
        valid_co2 = 1 if column_sum_co2 < len(valid_co2_indexes)/2 else 0

        for i in range(0, report_length):
            if i in valid_co2_indexes and \
               int(c[i]) != valid_co2 and \
               len(valid_co2_indexes) > 1:
                valid_co2_indexes.remove(i)
            if i in valid_oxy_indexes and \
               int(c[i]) != valid_oxy and \
               len(valid_oxy_indexes) > 1:
                valid_oxy_indexes.remove(i)

    oxygen_generator_rating = int(report_list[valid_oxy_indexes[0]], 2)
    co2_generator_rating = int(report_list[valid_co2_indexes[0]], 2)

    life_support_rating = oxygen_generator_rating * co2_generator_rating
    return life_support_rating


if __name__ == "__main__":
    with open("../input.txt") as report:
        report = report.read()
        print(calc_life_support_rating(report))
