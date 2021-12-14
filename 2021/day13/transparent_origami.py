class Paper():
    def __init__(self, input):
        self.grid = []
        self.folds = []
        self.read_input(input)

    def read_input(self, input):
        lines = input.splitlines()
        grid_fold_boundary = lines.index('')
        self.add_points_to_grid(lines[:grid_fold_boundary])
        self.read_folds(lines[grid_fold_boundary+1:])

    def add_points_to_grid(self, lines):
        points = [(int(p[0]), int(p[1])) for p in
                  [line.split(',') for line in lines]]
        self.max_x = max([x for x, _ in points])
        self.max_y = max([y for _, y in points])

        for y in range(self.max_y+1):
            xes = []
            for x in range(self.max_x+1):
                xes.append(0)
            self.grid.append(xes)

        for x, y in points:
            self.grid[y][x] = 1

    def read_folds(self, lines):
        self.folds = [(p[0][11:], int(p[1])) for p in
                      [line.split('=') for line in lines]]

    def fold_on(self, fold):
        direction, fold_index = fold
        if direction == 'y':
            overhang = ((fold_index * 2) + 1) - len(self.grid)
            top = self.grid[:fold_index]
            bottom = self.grid[fold_index+1:]

            bottom.reverse()

            folded = []
            for y, line in enumerate(top):
                print("y", y)
                xes = []
                for x, top_value in enumerate(line):
                    print('x', x)
                    new = 1 if top_value + bottom[y][x] > 0 else 0
                    xes.append(new)
                folded.append(xes)

            self.grid = folded

    def fold(self):
        this_fold = self.folds.pop(0)
        self.fold_on(this_fold)

    def print(self):
        print_grid = ""
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                print_grid += '#' if self.grid[y][x] else '.'
            print_grid += '\n'
        return print_grid.rstrip()
