class Passport:

    def __init__(self, passport_string):
        self.birthyear = int(self.split_kv(passport_string)[1])


    def split_kv(self, kv_pair):
        return tuple(kv_pair.split(':'))
