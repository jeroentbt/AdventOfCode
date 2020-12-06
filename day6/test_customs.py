from customs import unique_yeses


def test_count_unique_yeses():
    yeses = ("a\n"
             "a")
    assert 1 == unique_yeses(yeses)
