class Boat():
    def __init__(self):
        self.waypoint_latitude = 1
        self.waypoint_longtitude = 10
        self.latitude = 0  # N-S
        self.longtitude = 0  # E-W

    def move(self, instruction):
        action, value = instruction
        if action == "N":
            self.waypoint_latitude += value
        if action == "S":
            self.waypoint_latitude -= value
        if action == "E":
            self.waypoint_longtitude += value
        if action == "W":
            self.waypoint_longtitude -= value
        if action == "R":
            self.turn(value)
        if action == "L":
            self.turn(-value)
        if action == "F":
            self.forward(value)
        # print(self.longtitude, self.latitude)

    def turn(self, value):
        quarters = (value // 90) % 2
        if quarters == 0:
            # print("flip")
            self.waypoint_latitude, self.waypoint_longtitude = \
                - self.waypoint_longtitude, - self.waypoint_latitude
        else:
            if value > 0:
                # print("turn right")
                self.waypoint_latitude, self.waypoint_longtitude = \
                    - self.waypoint_longtitude, self.waypoint_latitude
            else:
                # print("turn left")
                self.waypoint_latitude, self.waypoint_longtitude = \
                    self.waypoint_longtitude, - self.waypoint_latitude

    def forward(self, value):
        self.latitude = self.latitude + (self.waypoint_latitude * value)
        self.longtitude = self.longtitude + (self.waypoint_longtitude * value)

    def navigate(self, instructions):
        for instruction in instructions:
            # print("-" * 20)
            self.move(instruction)

    def manhattan(self):
        return abs(self.longtitude) + abs(self.latitude)

    def __str__(self):
        return f"latitude (N-S):  {self.latitude}\n \
                longtitude (E-W): {self.longtitude}"


def read_nav(nav_txt):
    return [(str(line[:1]), int(line[1:])) for line in nav_txt.splitlines()]


if __name__ == "__main__":
    with open("input.txt") as nav_txt:
        b = Boat()
        b.navigate(read_nav(nav_txt.read()))
        print(b.manhattan())
