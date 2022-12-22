import sys

sys.path.insert(0, '..')
from Model import Walker as W


class Recruteur(W.Walker):
    def __init__(self, x, y):
        W.Walker.__init__(self, x, y)
        self.transport
        self.name = 'Recruteur'
