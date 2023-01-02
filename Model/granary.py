import sys
sys.path.insert(0, '..')
from Model import batiment as b


class Granary(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 3, 71, posx, posy, 100, -4, 1, 2, 2, 6,)
        self.max_space = 50
        self.occupied_space = 0
        self.name = "Granary"
    def isFull(self):
        return self.max_space == self.occupied_space