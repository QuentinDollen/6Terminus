import os
import sys

# Construct the full path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the PYTHONPATH
sys.path.append(parent_dir)

from Model import terrain as t
import pathlib

global dir_path

bat_path = '' + str(pathlib.Path(__file__).absolute())

dir_path: str = bat_path.replace('Batiment.py', '')



class Batiment(t.Terrain):
    def __init__(self, nbr_cases, id_bat, posx, posy, cst, des, stp, sze, rge, emp):
        t.Terrain.__init__(self, posx, posy,id_bat)

        self.nbr_cases = nbr_cases                # espace occupe par le batiment en termes de cases. À modifier selon le type de batiment
        self.acces_route = 0                      # booleen : le batiment a acces ou non a la route
        self.ind_fire = 0                         # indice de feu
        self.ind_eff = 0                          # indice d'effondrement
        self.cost = cst                           # coût en sesterce
        self.initDesirabilty = des                # Attractivité par défaut, par exemple les jardin et les écoles sont positifs, alors que les puits d'argile sont négatif
        self.stepDesirability = sze               # De combien ça baisse à chaque case
        self.sizeDesirability = stp               # Nb cases avant effet: 0 souvent
        self.rangeDesirability = rge              # La portée maximale de la désirabilité
        self.neededEmployees = emp                # le nombre d'employé requis pour que le batiment fonctionne
        self.name = 'Batiment'                    # le nom du batiment. À modifier selon le type de batiment
        self.Walk = []

    
    