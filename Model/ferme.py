import batiment as b


class Ferme (b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self,3, "Farm.png", posx, posy,4, 0,2,1,1,2,10,0,0)
        crop_path = "crop.png"
        harvet_path = "Weed.png"
        ind_Harv = 0