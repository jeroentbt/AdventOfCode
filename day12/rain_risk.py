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
            self.facing = (self.facing + value) % 360
        if action == "L":
            self.facing = (self.facing - value) % 360
        if action == "F":
            self.forward(10)

    def forward(self, value):
        directions = ["N", "E", "S", "W"]
        general_direction = directions[self.facing//90]
        deviation = self.facing % 90
        print(general_direction)
        print(deviation)

        if deviation == 0:
            self.move((general_direction, value))






def read_nav(nav_txt):
    return [(str(line[:1]), int(line[1:])) for line in nav_txt.splitlines()]
