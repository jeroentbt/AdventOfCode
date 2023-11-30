class Rope(object):
    def __init__(self, head=(0, 0), tail=(0, 0), length=1):
        self._knots = [Point(head) for x in range(length)]
        self._last = length - 1
        tail_x, tail_y = tail
        self._knots[self._last].x = tail_x
        self._knots[self._last].y = tail_y
        self._tail_log = [(tail)]

    def get_tail_position(self):
        return self._knots[self._last].position()

    def move_head(self, motion):
        direction, steps = tuple(motion.rstrip().split(" "))
        for s in range(int(steps)):
            self._knots[0].move(direction)
            self.tail_follow()

    def tail_follow(self):
        relative_position = self._knots[self._last].relative_to(self._knots[0])
        max_distance = max([distance for direction, distance in relative_position])

        if max_distance > 1:
            for p in relative_position:
                direction, distance = p
                self._knots[self._last].move(direction)

        self._tail_log.append(self.get_tail_position())

    def unique_tail_positions(self):
        return len(set(self._tail_log))

    def __str__(self):
        max_x = max([self._knots[0].max_x,
                     self._knots[self._last].max_x])
        min_x = min([self._knots[0].min_x,
                     self._knots[self._last].min_x])
        max_y = max([self._knots[0].max_y,
                     self._knots[self._last].max_y])
        min_y = min([self._knots[0].min_y,
                     self._knots[self._last].min_y])

        lines = []
        for y in range(max_y, min_y - 1, -1):
            line = ""
            for x in range(min_x, max_x + 1):
                if x == self._knots[self._last].x and y == self._knots[self._last].y:
                    line += "\033[91mT\033[00m"
                elif x == self._knots[0].x and y == self._knots[0].y:
                    line += "\033[92mH\033[00m"
                elif x == 0 and y == 0:
                    line += "s"
                else:
                    line += "."
            lines.append(line)
        lines.append("-")
        return "\n".join(lines)


class Point(object):
    def __init__(self, position):
        x, y = position
        self.x = x
        self.y = y
        self.max_x = 0
        self.max_y = 0
        self.min_x = 0
        self.min_y = 0

    def move(self, direction):
        if direction == "R":
            self.x += 1
        if direction == "L":
            self.x -= 1
        if direction == "U":
            self.y += 1
        if direction == "D":
            self.y -= 1

        if self.x > self.max_x:
            self.max_x = self.x
        if self.y > self.max_y:
            self.max_y = self.y
        if self.x < self.min_x:
            self.min_x = self.x
        if self.y < self.min_y:
            self.min_y = self.y

    def relative_to(self, point):
        xdiff = self.x - point.x
        ydiff = self.y - point.y

        relative_position = []
        if xdiff == 0 and ydiff == 0:
            relative_position.append((None, 0))
        if ydiff > 0:
            relative_position.append(("D", ydiff))
        if ydiff < 0:
            relative_position.append(("U", abs(ydiff)))
        if xdiff > 0:
            relative_position.append(("L", xdiff))
        if xdiff < 0:
            relative_position.append(("R", abs(xdiff)))
        return relative_position

    def position(self):
        return (self.x, self.y)


if __name__ == "__main__":
    with open("example.txt") as txt:
        motions = txt.readlines()
    r = Rope()
    for m in motions:
        r.move_head(m)
        print(r)
        input("continue..")

    input("Press enter to continue to part 1...")

    with open("input.txt") as txt:
        motions = txt.readlines()
    r = Rope()
    for m in motions:
        r.move_head(m)
        print(r)
        input("continue..")
    print("part 1:")
    print(r.unique_tail_positions())
