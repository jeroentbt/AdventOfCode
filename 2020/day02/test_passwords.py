from passwords import *


def test_get_policy():
    assert get_policy("1-3 a") == (1, 3, 'a')


def test_get_policy_2():
    assert get_policy("10-13 b") == (10, 13, 'b')


def test_check_policy():
    assert check_policy("1-2 a: aa") == True

def test_check_policy_should_fail():
    assert check_policy("1-2 a: aaa") == False
