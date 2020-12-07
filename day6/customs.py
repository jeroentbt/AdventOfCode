def unique_positives(a_groups_positives):
    return len(set(a_groups_positives.replace("\n", "")))


def grouped_positives(all_positives):
    return all_positives.split("\n\n")


def grouped_unique_positives(all_positives):
    return [unique_positives(group) for group in grouped_positives(all_positives)]

def grouped_shared_positives(all_positives):
    return [number_of_shared_positives(group) for group in grouped_positives(all_positives)]


def number_of_shared_positives(a_groups_positives):
    positives_per_person = [set(a_persons_positives) for a_persons_positives in a_groups_positives.splitlines()]
    shared_positives = set.intersection(*positives_per_person)
    return len(shared_positives)


if __name__ == "__main__":
    with open("input.txt") as answers:
        all_answers = answers.read()
        print("sum of counts:")
        print(sum(grouped_unique_positives(all_answers)))
        print("sum of shared positives:")
        print(sum(grouped_shared_positives(all_answers)))
