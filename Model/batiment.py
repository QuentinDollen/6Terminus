import sys

sys.path.insert(0, '..')
from Model import terrain as t


class Batiment(t.Terrain):
    def __init__(self, nbr_cases, id_bat, posx, posy, cst, des, stp, sze, rge, emp):
        t.Terrain.__init__(self, posx, posy, id_bat)

        self.nbr_cases = nbr_cases  # espace occupe par le batiment en termes de cases. À modifier selon le type de batiment
        self.acces_route = 0  # booleen : le batiment a acces ou non a la route
        self.ind_fire = 0  # indice de feu
        self.ind_eff = 0  # indice d'effondrement
        self.cost = cst  # coût en sesterce
        self.initDesirabilty = des  # Attractivité par défaut, par exemple les jardin et les écoles sont positifs, alors que les puits d'argile sont négatif
        self.stepDesirability = sze  # De combien ça baisse à chaque case
        self.sizeDesirability = stp  # Nb cases avant effet: 0 souvent
        self.rangeDesirability = rge  # La portée maximale de la désirabilité
        self.neededEmployees = emp  # le nombre d'employé requis pour que le batiment fonctionne
        self.name = 'Batiment'  # le nom du batiment. À modifier selon le type de batiment
        self.Walk = []
    def ret_coord(self):
        return (self.pos_x , self.pos_y)
        
    def get_delivery(self, chargement):
        print("chargement",chargement)
        if(chargement[0] == 'ble'):
            self.nourriture[0][1] = self.nourriture[0][1] + chargement[1]
        if chargement[0] == 'fruits':
            self.nourriture[1][1] += chargement[1]
        if chargement[0] == 'viandes':
            self.nourriture[2][1] += chargement[1]
        if chargement[0] == 'olives':
            self.produits[2][1] += chargement[1]
        if chargement[0] == 'viandes':
            self.produits[0][1] += chargement[1]


