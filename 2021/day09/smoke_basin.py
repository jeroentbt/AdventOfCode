class Point():
    def __init__(self, height, x, y):
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)
        self.neighbour_left = False
        self.neighbour_right = False
        self.neighbour_up = False
        self.neighbour_down = False
        self.lowest = False


class Cave():
    def __init__(self, heightmap):
        self.heightmap = self.read_map(heightmap)
        self.set_neighbours_for_points()
        self.set_low_points()

    def read_map(self, heightmap):
        self.points = []
        lines = heightmap.splitlines()
        self.max_x = len(lines[0]) - 1
        self.max_y = len(lines)

        for y, line in enumerate(lines):
            for x, height in enumerate(list(line)):
                self.points.append(Point(height, x, y))


    def set_neighbours_for_points(self):
        for point in self.points:
            if point.x > 0:
                point.neighbour_left = point.x - 1
            if point.x < self.max_x:
                point.neighbour_right = point.x + 1

    def set_low_points(self):
        for point in self.points:
            neighbours = []
            if point.neighbour_left:
                neighbours.append(self.points[point.neighbour_left].height)
            if point.neighbour_right:
                neighbours.append(self.points[point.neighbour_right].height)
            if min(neighbours) > point.height:
                point.lowest = True


def low_points(heightmap):
    cave = Cave(heightmap)
    return [point for point in cave.points if point.lowest]
