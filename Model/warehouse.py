import sys
sys.path.insert(0, '..')
from Model import batiment as b


class Warehouse(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 3, 72, posx, posy, 70, -5, 2, 2, 3, 6)
        self.name = "Warehouse"
        self.max_space = 30
        self.occupied_space = 0
    def isFull(self):
        return self.max_space == self.occupied_space