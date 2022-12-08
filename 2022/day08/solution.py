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
        print(printer)
    return total_visible


def parse_input(input):
    treegrid = []
    for line in list(input.split("\n")):
        treegrid.append([{"size": int(i),
                          "visible": None} for i in list(line.strip())])
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


if __name__ == "__main__":
    with open("input.txt") as input:
        i = input.read().rstrip()
    print("part 1:")
    print("visible trees: " + str(visible_trees(i)))
