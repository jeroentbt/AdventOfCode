class Paper():
    def __init__(self, input):
        self.grid = []
        self.folds = []
        self.read_input(input)

    def read_input(self, input):
        lines = input.splitlines()
        grid_fold_boundary = lines.index('')
        self.add_points_to_grid(lines[:grid_fold_boundary])
        foldlines = lines[grid_fold_boundary+1:]

    def add_points_to_grid(self, lines):
        points = [(int(p[0]), int(p[1])) for p in
                  [l.split(',') for l in lines]]
        self.max_x = max([x for x, _ in points])
        self.max_y = max([y for _, y in points])

        for y in range(self.max_y+1):
            xes = []
            for x in range(self.max_x+1):
                xes.append(0)
            self.grid.append(xes)

        for x, y in points:
            self.grid[y][x] = 1

    def print(self):
        print_grid = ""
        for y in range(self.max_y+1):
            for x in range(self.max_x+1):
                print_grid += '#' if self.grid[y][x] else '.'
            print_grid += '\n'
        return print_grid.rstrip()
