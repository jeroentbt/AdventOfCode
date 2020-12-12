class Boat():
    def __init__(self):
        self.facing = 90
        self.latitude = 0  # N-S
        self.longtitude = 0  # E-W

    def move(self, instruction):
        action, value = instruction
        if action == "N":
            self.latitude += value
        if action == "S":
            self.latitude -= value
        if action == "E":
            self.longtitude += value
        if action == "W":
            self.longtitude -= value
        if action == "R":
            self.facing += value
        if action == "L":
            self.facing -= value





def read_nav(nav_txt):
    return [(str(line[:1]), int(line[1:])) for line in nav_txt.splitlines()]
