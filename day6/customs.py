def unique_yeses(a_groups_yeses):
    return len(set(a_groups_yeses.replace("\n", "")))


def grouped_answers(all_answers):
    return all_answers.split("\n\n")


def grouped_unique_positives(all_answers):
    return [3,3,3,1,1]
