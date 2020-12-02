from passwords import *


def test_read_min_and_max():
    assert read_min_and_max("1-3") == (1, 3)


def test_read_min_and_max():
    assert read_min_and_max("10-13") == (10, 13)
