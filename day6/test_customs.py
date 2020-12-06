from customs import unique_yeses, grouped_answers, grouped_unique_positives


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


def test_split_groups():
    all_answers = ("a\n" \
                   "\n" \
                   "a\n" \
                   "\n" \
                   "b\n" \
                   "acs")
    assert ["a", "a", "b\nacs"] == grouped_answers(all_answers)


def test_unique_answers_per_group():
    all_answers = ("abc\n" \
                   "\n" \
                   "a" \
                   "b" \
                   "c" \
                   "\n" \
                   "ab" \
                   "ac" \
                   "\n" \
                   "a" \
                   "a" \
                   "a" \
                   "a" \
                   "\n" \
                   "b")
    assert [3,3,3,1,1] == grouped_unique_positives(all_answers)
