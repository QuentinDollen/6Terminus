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
        self.curEmployees = 0 # Le nombre d'employées 
        self.name = "Batiment"  # le nom du batiment. À modifier selon le type de batiment
        self.Walk = [] 
        self.wakler_in = False # Si le walker du batiement est dans le batiment
        
    def ret_coord(self):
        return (self.pos_x , self.pos_y)
        
    def need_employees( self , Nb_immigrant ) :
        if Nb_immigrant > 0 and self.curEmployees < self.neededEmployees : 
            self.curEmployees += 1
            return  Nb_immigrant - 1 
        else :
            return Nb_immigrant

    def recieve_walker( self , walker ):
        self.Walk.append(walker)
        self.wakler_in = True




    

