import batiment as b


#class Panneau():
class Maison_1(b.Batiment):
    def __init__(self,x,y):
        b.Batiment.__init__(self,1,11,x,y,)
        self.name = 'Maison'
        self.nb_habitants = 0
        self.nourriture = []
        self.produits = []
        self.acces_eau = 0
        self.id = 10

#class Maison_2():