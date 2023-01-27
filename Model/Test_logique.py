import pygame as pg
import pickle
import sys

sys.path.insert(0, '..')

from Model.logique import *


def reset_maps() : 
    m.Mat_perso = []
    m.Mat_batiment = []
    m.init_matrice_perso(m.Mat_perso,m.nb_cases_x , m.nb_cases_y)
    m.init_matrice_terrain(m.Mat_batiment,m.nb_cases_x , m.nb_cases_y)
    Add_bat_game(39,21 , m.name_id["Path"])
    Add_bat_game(39,20 , m.name_id["Panneau Entree"])
    


def Construction_1() : 
    for i in range(m.nb_cases_x) :
        Add_bat_game(1,i, m.name_id["Path"])

    Add_bat_game(2 , 20 , m.name_id["Maison1"])
    Add_bat_game(2 , 25 , m.name_id["EngineersPost"])
    m.add_perso(1,0,"Engineer" , m.Mat_perso , m.Mat_batiment[2][25] , None)
    m.add_perso(1,4,"Priest" , m.Mat_perso , m.Mat_batiment[2][20] , None)

def Tour_jeu() :
    m.deplacement_perso(m.Mat_perso , m.nb_cases_x , m.nb_cases_y)
    m.check_fire_eff()
    test_bat_logique()
    test_walker_logique()
    