from customs import unique_yeses


def test_count_unique_yeses():
    yeses = ("a\n"
             "a")
    assert 1 == unique_yeses(yeses)


def test_count_unique_yeses_2():
    yeses = ("a\n"
             "b")
    assert 2 == unique_yeses(yeses)
