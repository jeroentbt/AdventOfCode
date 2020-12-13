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
            # print('-' * 20)
            # print('right', value)
            self.turn(value)
        if action == "L":
            # print('-' * 20)
            # print('left', value)
            self.turn(-value)
        if action == "F":
            self.forward(value)
        # print(self.longtitude, self.latitude)
        # print("-->", self.waypoint_longtitude, self.waypoint_latitude)

    def turn(self, value):
        quarters = (value // 90)
        if quarters % 2 == 0 or quarters == 0:
            # print("flip")
            self.waypoint_latitude *= -1
            self.waypoint_longtitude *= -1
        else:
            # print(value, quarters)

            if quarters == 1 or quarters == -3:
                # print("turn right")
                self.waypoint_latitude, self.waypoint_longtitude = \
                    - self.waypoint_longtitude, self.waypoint_latitude
            if quarters == 3 or quarters == -1:
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
