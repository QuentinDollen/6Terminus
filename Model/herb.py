import terrain as T
class Herb(T.Terrain):
    def __init__(self,x,y,id_t):
        T.Terrain.__init__(x,y,id_t)
        self.name = "Herb"
