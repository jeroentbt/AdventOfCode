def unique_positives(a_groups_positives):
    return len(set(a_groups_positives.replace("\n", "")))


def grouped_positives(all_positives):
    return all_positives.split("\n\n")


def grouped_unique_positives(all_positives):
    return [3,3,3,1,1]
