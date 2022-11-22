import matrice as m
import math as ma
import numpy as np
import batiment as b
import terrain as t
import maison as mais
import Walker as w
import Priest as p
import water as wa
import engineering as eng
import security as sec
import herb as h
import delivery_guy as dg


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
    if(m.Mat_batiment[x][y].name ==  "Herb" ): #il faut rajouter un or pour le cas où on rajoute un aqueduc sur une route ou vice versa mais comme c'est trop chiant a taper je l'ai pas fait
        m.add_bat(x,y,id_bat, m.Mat_batiment)
    else: return -1

init_game()