class Point():
    def __init__(self, height, x, y):
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)
        self.neighbours = {'left': False,
                           'right': False,
                           'up': False,
                           'down': False}
        self.lowest = False
        self.risk = 0

    def __str__(self):
        return \
            "----point----\n" \
            "height: %s\n" \
            "x: %s, y: %s\n\n" \
            "   %s     \n" \
            "%s    %s  \n" \
            "   %s     \n\n" \
            "lowest: %s" % (self.height, self.x, self.y,
                            self.neighbours['up'] is True,
                            self.neighbours['left'] is True,
                            self.neighbours['right'] is True,
                            self.neighbours['down'] is True,
                            self.lowest)


class Cave():
    def __init__(self, heightmap):
        self.heightmap = self.read_map(heightmap)
        self.set_neighbours_for_points()
        self.set_low_points()

    def read_map(self, heightmap):
        self.points = []
        lines = heightmap.splitlines()
        self.max_x = len(lines[0]) - 1
        self.max_y = len(lines) - 1

        print(self.max_x)
        print(self.max_y)

        for y, line in enumerate(lines):
            for x, height in enumerate(list(line)):
                self.points.append(Point(height, x, y))

    def set_neighbours_for_points(self):
        for point in self.points:

            # using array with single dimension
            row_offset = (point.y * (self.max_x + 1))

            if point.x > 0:
                point.neighbours['left'] = self.points[point.x - 1 + row_offset]
            if point.x < self.max_x:
                point.neighbours['right'] = self.points[point.x + 1 + row_offset]
            if point.y > 0:
                point.neighbours['up'] = self.points[point.x - self.max_x - 1 + row_offset]
            if point.y < self.max_y:
                point.neighbours['down'] = self.points[point.x + self.max_x + 1 + row_offset]

    def set_low_points(self):
        for point in self.points:
            neighbours = []
            if point.neighbours['left']:
                neighbours.append(point.neighbours['left'].height)
            if point.neighbours['right']:
                neighbours.append(point.neighbours['right'].height)
            if point.neighbours['up']:
                neighbours.append(point.neighbours['up'].height)
            if point.neighbours['down']:
                neighbours.append(point.neighbours['down'].height)
            print(neighbours)
            if min(neighbours) > point.height:
                point.lowest = True
                point.risk = 1 + point.height
            print(point)


def low_points(heightmap):
    cave = Cave(heightmap)
    return [point for point in cave.points if point.lowest]


def sum_of_risk(heightmap):
    cave = Cave(heightmap)
    return sum([point.risk for point in cave.points])
