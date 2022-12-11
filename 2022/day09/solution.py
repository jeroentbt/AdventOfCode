class Rope(object):
    def __init__(self, head=(0, 0), tail=(0, 0)):
        self._head = Point(head)
        self._tail = Point(tail)
        self._length = 1
        self._tail_log = [(tail)]

    def get_tail_position(self):
        return self._tail.position()

    def move_head(self, motion):
        direction, steps = tuple(motion.rstrip().split(" "))
        for s in range(int(steps)):
            self._head.move(direction)
            self.tail_follow()

    def tail_follow(self):
        relative_position = self._tail.relative_to(self._head)
        max_distance = max([distance for direction, distance in relative_position])
        print(relative_position)

        if max_distance > 1:
            for p in relative_position:
                direction, distance = p
                self._tail.move(direction)

        self._tail_log.append(self.get_tail_position())

    def unique_tail_positions(self):
        return len(set(self._tail_log))

    def __str__(self):
        max_x = max([self._head.max_x,
                     self._tail.max_x])
        min_x = min([self._head.min_x,
                     self._tail.min_x])
        max_y = max([self._head.max_y,
                     self._tail.max_y])
        min_y = min([self._head.min_y,
                     self._tail.min_y])

        lines = []
        for y in range(max_y, min_y - 1, -1):
            line = ""
            for x in range(min_x, max_x + 1):
                if x == self._tail.x and y == self._tail.y:
                    line += "\033[91mT\033[00m"
                elif x == self._head.x and y == self._head.y:
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
    with open("input.txt") as txt:
        motions = txt.readlines()
    r = Rope()
    for m in motions:
        r.move_head(m)
        print(r)
        input("continue..")
    print("part 1:")
    print(r.unique_tail_positions())
