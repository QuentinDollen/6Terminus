import sys

sys.path.insert(0, '..')


class NoWalker:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = 'no Walker'


class Walker(NoWalker):
    def __init__(self, x, y, bat):
        super().__init__(x, y)
        self.name = 'unknown'
        self.ttl = 20
        self.tab_path = []
        self.batiment = bat
        self.dest_x = -1
        self.dest_y = -1
        self.has_moved = 0
