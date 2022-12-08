class Filesystem(object):

    def __init__(self):
        self.tree = {"/": 0}
        self.cwd = "/"

    def cd(self, dir):
        if dir == "/":
            self.cwd = "/"
        if dir == "..":
            new_path = "/".join(self.cwd.split("/")[:-2]) + "/"
            self.cwd = new_path
        else:
            new_path = self.cwd + dir + "/"
            if new_path in self.tree.keys():
                self.cwd = new_path

    def mkdir(self, dir):
        full_path = self.cwd + dir + "/"
        self.tree[full_path] = 0

    def touch(self, name, size):
        full_path = self.cwd + name
        self.tree[full_path] = int(size)

    def recurive_dir_sizes(self):
        recursive_sizes = {}
        for item in self.tree.keys():
            if item[-1] == "/":
                size = 0
                for i, s in self.tree.items():
                    if i.startswith(item):
                        size += s
                recursive_sizes[item] = size
        return recursive_sizes


    def __str__(self):
        out = ""
        for key, value in sorted(self.tree.items()):
            out += key + " " + str(value) + "\n"
        return out


def read_output(output):
    fs = Filesystem()
    for line in output:
        l = line.split(" ")
        if l[0] == "$":
            if l[1] == "cd":
                fs.cd(l[2])
        if l[0] == "dir":
            fs.mkdir(l[1])
        if l[0] not in ["$", "dir"]:
            fs.touch(l[1], l[0])
    return fs


def part_one_count(fs):
    solution = 0
    for s in fs.recurive_dir_sizes().values():
        if s <= 100000:
            solution += s
    return solution


if __name__ == "__main__":
    with open("input.txt") as output:
        o = output.readlines()
    o = [i.strip() for i in o]
    print("part 1:")
    print(part_one_count(read_output(o)))
