import terrain as T
class Herb(T.Terrain):
    def __init__(self,x,y):
        T.Terrain.__init__(self, x,y,0)
        self.name = "Herb"
