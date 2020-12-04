from passport_processing import Passport


def test_recognize_birth_year():
    input = "byr:1937"
    passport = Passport(input)
    assert 1937 == passport.birthyear


def test_recognize_birth_year_2():
    input = "byr:1938"
    passport = Passport(input)
    assert 1938 == passport.birthyear
