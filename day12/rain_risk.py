class Boat():
    def __init__(self):
        self.facing = "E"
        self.latitude = 0  # N-S
        self.longtitude = 0  # E-W

    def move(self, instruction):
        action, value = instruction
        if action == "N":
            self.latitude += value


def read_nav(nav_txt):
    return [(str(l[:1]), int(l[1:])) for l in nav_txt.splitlines()]
