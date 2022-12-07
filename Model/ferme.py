import batiment as b
import logique
class Ferme (b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self,3, "Farm.png", posx, posy,4, 0,2,1,1,2,10,0,0)
        ind_Harv = 0
    def growFood(self):
        self.growFood = self.growFood + 1
        if(self.growFood >= 5):
            self.growFood = 0
            
