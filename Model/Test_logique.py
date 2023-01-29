import pygame as pg
import pickle
import sys

sys.path.insert(0, '..')

from Model.logique import *



def reset_maps() :
    m.Mat_perso = []
    m.Mat_batiment = []
    m.Mat_fire = []
    m.Mat_water = []
    m.init_matrice_perso(m.Mat_perso,m.nb_cases_x , m.nb_cases_y)
    m.init_matrice_terrain(m.Mat_batiment,m.nb_cases_x , m.nb_cases_y)
    m.init_mat_fire()
    m.init_mat_water()
    Add_bat_game(19,0 , m.name_id["Panneau Entree"])
    Add_bat_game( 20 , 0 , m.name_id["Path"])

    


def Construction_1() : 
    for i in range(1,m.nb_cases_x) :
        Add_bat_game(1,i, m.name_id["Path"])

    Add_bat_game(2 , 20 , m.name_id["Maison1"])
    Add_bat_game(2 , 25 , m.name_id["EngineersPost"])
    m.add_perso(1,1,"Engineer" , m.Mat_perso , m.Mat_batiment[2][25] , None)
    m.add_perso(1,4,"Priest" , m.Mat_perso , m.Mat_batiment[2][20] , None)


def Construction_maison_1() : 
    reset_maps()
    for i in range ( 1 , m.nb_cases_y ) :
        Add_bat_game( 20 , i , m.name_id["Path"])
        if 10 < i < 15 :
            Add_bat_game(21 , i , m.name_id["Panneau"])

        

    


    

