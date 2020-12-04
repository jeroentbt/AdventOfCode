class Passport:

    def __init__(self, passport_string):
        fields = self.split_fields(passport_string)
        for f in fields:
            key, value = self.split_kv(f)
            if key == "byr":
                self.birthyear = int(value)
            if key == "iyr":
                self.issueyear = int(value)


    def split_kv(self, kv_pair):
        return tuple(kv_pair.split(':'))


    def split_fields(self, passport_string):
        return passport_string.split(' ')
