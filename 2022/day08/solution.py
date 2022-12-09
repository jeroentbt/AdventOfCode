import math


def visible_trees(input):
    treegrid = set_visibility(parse_input(input))
    total_visible = 0
    for row in treegrid:
        printer = ''
        for tree in row:
            if tree["visible"]:
                total_visible += 1
                printer += "\033[91m" + str(tree["size"]) + "\033[00m"
            else:
                printer += str(tree["size"])
        # print(printer)
    return total_visible


def parse_input(input):
    treegrid = []
    for line in list(input.split("\n")):
        treegrid.append([{"size": int(i),
                          "visible": None,
                          "scenic score": 0} for i in list(line.strip())])
    return treegrid


def set_visibility(treegrid):
    rows = len(treegrid)
    columns = len(treegrid[0])

    for y in range(rows):
        for x in range(columns):
            if x == 0 or x == rows - 1 or y == 0 or y == columns - 1:
                treegrid[y][x]["visible"] = True

    lines_of_sight = []
    # left to right AND right to left
    for y in range(rows):
        line = []
        for x in range(columns):
            line.append((x, y))
        lines_of_sight.append(line)
        lines_of_sight.append(reversed(line))
    # top to bottom AND bottom to top
    for x in range(columns):
        line = []
        for y in range(rows):
            line.append((x, y))
        lines_of_sight.append(line)
        lines_of_sight.append(reversed(line))

    for line in lines_of_sight:
        previous_visible_height = -1
        for x, y in line:
            if treegrid[y][x]["size"] > previous_visible_height:
                treegrid[y][x]["visible"] = True
                previous_visible_height = treegrid[y][x]["size"]
    return treegrid


def best_trees_scenic_score(input):
    treegrid = parse_input(input)
    best = 0
    for y in range(len(treegrid)):
        for x in range(len(treegrid[0])):
            treegrid = set_scenic_score(treegrid, x, y)
            if treegrid[y][x]["scenic score"] > best:
                best = treegrid[y][x]["scenic score"]
    return best


def set_scenic_score(treegrid, x, y):
    rows = len(treegrid)
    columns = len(treegrid[0])

    lines_of_sight = []
    # left to right AND right to left
    line = []
    for x_ in range(columns):
        line.append((x_, y))
    lines_of_sight.append(line[x:])
    lines_of_sight.append(list(reversed(line[:x])))
    # top to bottom AND bottom to top
    line = []
    for y_ in range(rows):
        line.append((x, y_))
    lines_of_sight.append(line[y:])
    lines_of_sight.append(list(reversed(line[:y])))

    this_tree_size = treegrid[y][x]["size"]
    viewing_distances = []
    for line in lines_of_sight:
        line = [t for t in line if t != (x, y)]
        viewing_distance = 0
        for x_, y_ in line:
            viewing_distance += 1
            if treegrid[y_][x_]["size"] >= this_tree_size:
                break

        viewing_distances.append(viewing_distance)
    treegrid[y][x]["scenic score"] = math.prod(viewing_distances)

    return treegrid


if __name__ == "__main__":
    with open("input.txt") as input:
        i = input.read().rstrip()
    print("part 1:")
    print("visible trees: " + str(visible_trees(i)))
    print("part 2:")
    print("best scenic score: " + str(best_trees_scenic_score(i)))
