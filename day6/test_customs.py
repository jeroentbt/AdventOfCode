from customs import unique_positives, grouped_positives, grouped_unique_positives


def test_count_unique_positives():
    positives = ("a\n"
             "a")
    assert 1 == unique_positives(positives)


def test_count_unique_positives_2():
    positives = ("a\n"
             "b")
    assert 2 == unique_positives(positives)


def test_count_split_groups():
    all_positives = ("a\n" \
                   "\n" \
                   "a")
    assert 2 == len(grouped_positives(all_positives))


def test_count_split_groups_2():
    all_positives = ("a\n" \
                   "\n" \
                   "a\n" \
                   "\n" \
                   "b\n" \
                   "acs")
    assert 3 == len(grouped_positives(all_positives))


def test_split_groups():
    all_positives = ("a\n" \
                   "\n" \
                   "a\n" \
                   "\n" \
                   "b\n" \
                   "acs")
    assert ["a", "a", "b\nacs"] == grouped_positives(all_positives)


def test_unique_positives_per_group():
    all_positives = ("abc\n" \
                     "\n" \
                     "a\n" \
                     "b\n" \
                     "c\n" \
                     "\n" \
                     "ab\n" \
                     "ac\n" \
                     "\n" \
                     "a\n" \
                     "a\n" \
                     "a\n" \
                     "a\n" \
                     "\n" \
                     "b\n")
    assert [3,3,3,1,1] == grouped_unique_positives(all_positives)


def test_unique_positives_per_group():
    all_positives = ("a\n" \
                     "b\n" \
                     "c\n" \
                     "\n" \
                     "ab\n" \
                     "ac\n" \
                     "\n" \
                     "a\n" \
                     "a\n" \
                     "a\n" \
                     "a\n" \
                     "\n" \
                     "b")
    assert [3,3,1,1] == grouped_unique_positives(all_positives)
