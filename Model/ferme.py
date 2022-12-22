import sys
sys.path.insert(0, '..')
from Model import batiment as b

class Ferme (b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 3, 100, posx, posy, 40, -2, 1, 1, 2, 10)
        ind_Harv = 0
    def growFood(self):
        self.growFood = self.growFood + 1
        if(self.growFood >= 5):
            #time for delivery
            self.growFood = 0
            
