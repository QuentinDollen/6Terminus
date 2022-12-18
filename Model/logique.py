import os
import sys

# Construct the full path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the PYTHONPATH
sys.path.append(parent_dir)


import Model.matrice as m
import math as ma
import numpy as np
import Model.batiment as b
import Model.terrain as t
import Model.maison as mais
import Model.Walker as w
import Model.Priest as p
import Model.water as wa
import Model.engineering as eng
import Model.security as sec
import Model.herb as h
import Model.delivery_guy as dg


def Delivery(Bat, type_march, quant, Mat):
    (x,y) = m.SearchforRoad(Bat.pos_x, Bat.pos_y, Mat)
    if(x != -1):
        m.add_perso(x,y,'Delivery Guy', Mat)
        
        

def getID(i,j):
    if(m.Mat_batiment[i][j].main == 1):
        return m.Mat_batiment[i][j].id
    else:  return 666

def init_game():
    m.departureMatrice(m.Mat_batiment)

def Add_bat_game(x,y,id_bat):
    for i in range(m.id_size[id_bat]):
        for j in range(m.id_size[id_bat]):
            if m.Mat_batiment[x+i][y+j].name == "Herb":
                return -1
    m.add_bat(x,y,id_bat, m.Mat_batiment)

init_game()
