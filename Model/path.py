import batiment as b

class Path(b.Batiment):
    def __init__(self,x,y):
        b.Batiment.__init__(self,1,5,x,y,4,0,0,0,0,0)
        isOnAquaduct = 0
        self.name = 'Path'