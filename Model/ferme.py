from Terminus_project.Model import batiment as b

class Ferme (b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 3, 100, posx, posy, 4, 0, 2, 1, 1, 2, 10)
        ind_Harv = 0
    def growFood(self):
        self.growFood = self.growFood + 1
        if(self.growFood >= 5):
            self.growFood = 0
            
