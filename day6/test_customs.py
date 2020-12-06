from customs import unique_yeses, grouped_answers


def test_count_unique_yeses():
    yeses = ("a\n"
             "a")
    assert 1 == unique_yeses(yeses)


def test_count_unique_yeses_2():
    yeses = ("a\n"
             "b")
    assert 2 == unique_yeses(yeses)


def test_count_split_groups():
    all_answers = ("a\n" \
                   "\n" \
                   "a")
    assert 2 == len(grouped_answers(all_answers))


def test_count_split_groups_2():
    all_answers = ("a\n" \
                   "\n" \
                   "a\n" \
                   "\n" \
                   "b\n" \
                   "acs")
    assert 3 == len(grouped_answers(all_answers))
