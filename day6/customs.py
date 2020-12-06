def unique_positives(a_groups_positives):
    return len(set(a_groups_positives.replace("\n", "")))


def grouped_positives(all_positives):
    return all_positives.split("\n\n")


def grouped_unique_positives(all_positives):
    return [unique_positives(group) for group in grouped_positives(all_positives)]
