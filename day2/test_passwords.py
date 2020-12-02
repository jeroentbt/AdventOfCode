from passwords import *


def test_get_policy():
    assert get_policy("1-3") == (1, 3)


def test_get_policy():
    assert get_policy("10-13") == (10, 13)
