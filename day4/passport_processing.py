class Passport:

    def __init__(self, passport_string):
        self.birthyear = int(passport_string.split(':')[1])
