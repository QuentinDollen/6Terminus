import sys
sys.path.insert(0, '..')
from Model import batiment as b


class Senate1(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 4, 84, posx, posy, 250, 8, 2, -2, 2, 20)


class Senate2(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 4, 85, posx, posy, 400, 8, 2, -1, 8, 30)


class Forum1(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 2, 86, posx, posy, 75, 3, 2, -1, 2, 6)


class Forum2(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 2, 87, posx, posy, 125, 3, 2, -1, 2, 8)
