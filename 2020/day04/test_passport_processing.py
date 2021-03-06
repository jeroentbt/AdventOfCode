from passport_processing import Passport, count_valid_passports


def test_recognize_birth_year():
    input = "byr:1937"
    passport = Passport(input)
    assert 1937 == passport.birthyear


def test_recognize_birth_year_2():
    input = "byr:1938"
    passport = Passport(input)
    assert 1938 == passport.birthyear


def test_recognize_issue_year():
    input = "iyr:2010"
    passport = Passport(input)
    assert 2010 == passport.issueyear


def test_recognize_issue_year_and_birth_year_sepparated_with_space():
    input = "iyr:2010 byr:1920"
    passport = Passport(input)
    assert 2010 == passport.issueyear
    assert 1920 == passport.birthyear


def test_recognize_issue_year_and_birth_year_sepparated_with_newline():
    input = ("iyr:2010\n"
             "byr:1920")
    passport = Passport(input)
    assert 2010 == passport.issueyear
    assert 1920 == passport.birthyear


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


def test_passport_is_valid():
    input = ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n"
             "byr:1937 iyr:2017 cid:147 hgt:183cm")
    passport = Passport(input)
    assert passport.is_valid()


def test_passport_is_invalid():
    input = ("pid:860033327 eyr:2020 hcl:#fffffd\n"
             "byr:1937 iyr:2017 cid:147 hgt:183cm")
    passport = Passport(input)
    assert False == passport.is_valid()


def test_batch_two_valid_passports():
    input = ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n"
             "byr:1937 iyr:2017 cid:147 hgt:183cm\n"
             "\n"
             "hcl:#ae17e1 iyr:2013\n"
             "eyr:2024\n"
             "ecl:brn pid:760753108 byr:1931\n"
             "hgt:179cm")
    assert 2 == count_valid_passports(input)


def test_batch_three_valid_passports():
    input = ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n"
             "byr:1937 iyr:2017 cid:147 hgt:183cm\n"
             "\n"
             "hcl:#ae17e1 iyr:2013\n"
             "eyr:2024\n"
             "ecl:brn pid:760753108 byr:1931\n"
             "hgt:179cm\n"
             "\n"
             "hcl:#ae17e1 iyr:2013\n"
             "eyr:2024\n"
             "ecl:brn pid:760753108 byr:1931\n"
             "hgt:179cm")
    assert 3 == count_valid_passports(input)


def test_batch_three_of_which_two_valid_passports():
    input = ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n"
             "byr:1937 iyr:2017 cid:147 hgt:183cm\n"
             "\n"
             "hcl:#ae17e1 iyr:2013\n"
             "eyr:2024\n"
             "ecl:brn pid:760753108 byr:1931\n"
             "hgt:179cm\n"
             "\n"
             "iyr:2013\n"
             "eyr:2024\n"
             "ecl:brn pid:760753108 byr:1931\n"
             "hgt:179cm")
    assert 2 == count_valid_passports(input)


def test_wrong_value_for_passportid():
    input = "byr:1971 eyr:2039 hgt:172in pid:170cm hcl:17106b iyr:2012 ecl:gry cid:339"
    p = Passport(input)
    assert not hasattr(p, "passportid")
