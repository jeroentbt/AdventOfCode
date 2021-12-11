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
        self.basin = -1

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
        self.basins = []
        self.get_basins()

    def read_map(self, heightmap):
        self.points = []
        lines = heightmap.splitlines()
        self.max_x = len(lines[0]) - 1
        self.max_y = len(lines) - 1

        for y, line in enumerate(lines):
            for x, height in enumerate(list(line)):
                self.points.append(Point(height, x, y))

    def set_neighbours_for_points(self):
        for point in self.points:

            # using array with single dimension
            row_offset = (point.y * (self.max_x + 1))

            if point.x > 0:
                point.neighbours['left'] = \
                    self.points[point.x - 1 + row_offset]
            if point.x < self.max_x:
                point.neighbours['right'] = \
                    self.points[point.x + 1 + row_offset]
            if point.y > 0:
                point.neighbours['up'] = \
                    self.points[point.x - self.max_x - 1 + row_offset]
            if point.y < self.max_y:
                point.neighbours['down'] = \
                    self.points[point.x + self.max_x + 1 + row_offset]

    def set_low_points(self):
        for point in self.points:
            neighbours = []
            for _, n in point.neighbours.items():
                if n:
                    neighbours.append(n.height)
            if min(neighbours) > point.height:
                point.lowest = True
                point.risk = 1 + point.height

    def get_basins(self):
        for h in range(9):
            for point in [point for point in self.points
                          if point.height == h
                          and point.basin < 0]:

                self.define_basin([n for n in point.neighbours.values()
                                   if n is not False], basin=[])

    def define_basin(self, neighbours, basin):
        n = neighbours.pop()
        if n.height < 9:
            n.basin = len(self.basins)
            neighbours += [point for point in n.neighbours.values()
                           if point is not False and
                           point.basin < 0 and
                           point.height < 9]
            basin.append(n)
        if len(neighbours) == 0:
            self.basins.append(list(set(basin)))
            return basin
        else:
            self.define_basin(neighbours, basin)


def low_points(heightmap):
    cave = Cave(heightmap)
    return [point for point in cave.points if point.lowest]


def sum_of_risk(heightmap):
    cave = Cave(heightmap)
    return sum([point.risk for point in cave.points])


def basins(heightmap):
    cave = Cave(heightmap)
    return cave.basins


def solution_part_2(heightmap):
    cave = Cave(heightmap)
    three_largest_basins = sorted([len(basin) for basin in cave.basins],
                                  reverse=True)[0:3]
    product = 1
    for size in three_largest_basins:
        product *= size
    return product
