import batiment as b
class Herb(b.Batiment):
    def __init__(self,x,y):
        b.Batiment.__init__(self, x,y,0,0,0,0,0,0,0,0)
        self.name = "Herb"
