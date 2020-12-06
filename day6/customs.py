def unique_positives(a_groups_positives):
    return len(set(a_groups_positives.replace("\n", "")))


def grouped_positives(all_positives):
    return all_positives.split("\n\n")


def grouped_unique_positives(all_positives):
    return [unique_positives(group) for group in grouped_positives(all_positives)]


def number_of_shared_positives(a_groups_positives):
    return 3


if __name__ == "__main__":
    with open("input.txt") as answers:
        all_answers = answers.read()
        print("sum of counts:")
        print(sum(grouped_unique_positives(all_answers)))
