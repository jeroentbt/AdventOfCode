def unique_yeses(a_groups_yeses):
    return len(set(a_groups_yeses.replace("\n", "")))


def grouped_answers(all_answers):
    return all_answers.split("\n\n")
