from passport_processing import Passport


def test_recognize_birth_year():
    input = "byr:1937"
    passport = Passport(input)
    assert 1937 == passport.birthyear


def test_recognize_birth_year_2():
    input = "byr:1938"
    passport = Passport(input)
    assert 1938 == passport.birthyear


def test_recognize_issue_year():
    input = "iyr:2000"
    passport = Passport(input)
    assert 2000 == passport.issueyear


def test_recognize_issue_year_and_birth_year_sepparated_with_space():
    input = "iyr:2000 byr:1900"
    passport = Passport(input)
    assert 2000 == passport.issueyear
    assert 1900 == passport.birthyear


def test_recognize_issue_year_and_birth_year_sepparated_with_newline():
    input = ("iyr:2000\n"
             "byr:1900")
    passport = Passport(input)
    assert 2000 == passport.issueyear
    assert 1900 == passport.birthyear


def test_recognise_all_fields():
    input = ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n"
             "byr:1937 iyr:2017 cid:147 hgt:183cm")
    passport = Passport(input)
    assert "gry" == passport.eyecolor
    assert 860033327 == passport.passportid
    assert 2020 == passport.expirationyear
    assert "#fffffd" == passport.haircolor
    assert 1937 == passport.birthyear
    assert 2017 == passport.issueyear
    assert 147 == passport.countryid
    assert "183cm" == passport.height
