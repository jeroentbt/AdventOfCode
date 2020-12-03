from passwords_2 import *


def test_get_policy():
    assert get_policy("1-3 a") == (0, 2, 'a')


def test_get_policy_2():
    assert get_policy("10-13 b") == (9, 12, 'b')


def test_check_policy():
    assert check_policy("1-2 a: aa") == False

def test_check_policy_should_fail():
    assert check_policy("1-2 a: aaa") == False


def test_check_policy_should_succeed():
    assert check_policy("1-3 a: abcde") == True


def test_check_policy_should_fail_2():
    assert check_policy("1-3 b: cdefg") == False


def test_check_policy_should_fail_3():
    assert check_policy("2-9 c: ccccccccc") == False
