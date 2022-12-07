class Filesystem(object):

    def __init__(self):
        self.tree = Item("/")

    def pwd(self):
        return self.tree.name

    def command(self, cmd):
        pass

    def __str__(self):
        return self.tree.name


class Item(object):

    def __init__(self, name, size=0, parent=False):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def __str__(self):
        output = self.name
        return output
