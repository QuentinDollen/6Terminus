import batiment as b


class Well(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 92, posx, posy, 5, -1, 1, 2, 1, 1)


class Reservior(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 3, 90, posx, posy, 80, -6, 1, 2, 3, 0)


class Aquaduct(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 8, posx, posy, 8, -2, 1, 1, 2, 0)


class Fountain(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 1, 91, posx, posy, 15, 0, 0, 0, 0, 4)
