class Point():
    def __init__(self, height, x, y):
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)


def low_points(heightmap):
    points = []
    for y, horizontal in enumerate(heightmap.splitlines()):
        for x, height in enumerate(list(horizontal)):
            print(height, x, y)
            points.append(Point(height, x, y))
    return [point for point in points if point.height == 1]
