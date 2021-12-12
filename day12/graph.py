
class Graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def get_caves(self):
        return list(self.gdict.keys())

    def add_cave(self, name):
        self.gdict.update({name: set()})

    def add_neighbour(self, cavename, neighbour):
        self.gdict.get(cavename).add(neighbour)

    def get_neighbours(self, cavename):
        return self.gdict.get(cavename)
