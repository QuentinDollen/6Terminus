import sys

sys.path.insert(0, '..')
from Model import Walker as W


# food_guy a essentielement le mÃªme fonctionnement que delivery guy,
# faut juste le faire heriter et rajouter les condition appropriÃ©es:
# doit uniquement Ãªtre appelable d'un marchÃ©
# les dÃ©placement vont soit du marchÃ© aux greniers, soit du marchÃ© au random

class Food_Guy(W.Walker):
    def __init__(self, x, y, bat):
        W.Walker.__init__(self, x, y, bat)
        self.cargaison = [['blÃ©', 0], ['fruits', 0], ['viande', 0]]
        self.name = 'Food_Guy'

    def ajout_marchandise(self, type_nourriture, nb):
        if type_nourriture == 'blÃ©':
            self.cargaison[0][1] = self.cargaison[0][1] + nb
        if type_nourriture == 'fruits':
            self.cargaison[1][1] = self.cargaison[1][1] + nb
        if type_nourriture == 'viandes':
            self.cargaison[2][1] = self.cargaison[2][1] + nb