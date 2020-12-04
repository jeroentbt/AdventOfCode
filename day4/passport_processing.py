import re

def count_valid_passports(batch):
    passports = batch.split('\n\n')
    valid_passports = 0
    for p in passports:
        passport = Passport(p)
        if passport.is_valid():
            valid_passports += 1
    return valid_passports


class Passport:

    def __init__(self, passport_string):
        fields = self.split_fields(passport_string)
        for f in fields:
            key, value = self.split_kv(f)
            if key == "byr" and value.isnumeric() and 1920 <= int(value) <= 2002:
                self.birthyear = int(value)
            if key == "iyr" and value.isnumeric() and 2010 <= int(value) <= 2020:
                self.issueyear = int(value)
            if key == "ecl" and value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                self.eyecolor = value
            if key == "pid" and re.search(r'^\d{9}$', value):
                self.passportid = int(value)
            if key == "eyr" and value.isnumeric() and 2020 <= int(value) <= 2030:
                self.expirationyear = int(value)
            if key == "hcl" and re.search(r'^#[0-9a-f]{6}$', value):
                self.haircolor = value
            if key == "cid":
                self.countryid = int(value)
            if key == "hgt":
                r = re.search(r'^(\d+)(cm|in)$', value)
                if r and ((r.group(2) == "cm" and 150 <= int(r.group(1)) <= 193) or \
                          (r.group(2) == "in" and 59 <= int(r.group(1)) <= 76)):
                    self.height = value



    def split_kv(self, kv_pair):
        return tuple(kv_pair.split(':'))


    def split_fields(self, passport_string):
        return passport_string.split()


    def is_valid(self):
        if hasattr(self, "birthyear") and \
           hasattr(self, "issueyear") and \
           hasattr(self, "eyecolor") and \
           hasattr(self, "passportid") and \
           hasattr(self, "expirationyear") and \
           hasattr(self, "haircolor") and \
           hasattr(self, "height"):
            return True
        else:
            return False


if __name__ == "__main__":
    with open("input.txt") as batch:
        print(count_valid_passports(batch.read()))
