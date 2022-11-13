import matrice as m
import math as m
import numpy as np
import batiment as b
import terrain as t
import maison as m
import Walker as w
import Priest as p
import water as wa
import engineering as eng
import security as sec
import herb as h
import delivery_guy as dg

def isPath(x,y,Mat):
    return Mat[x][y].name == 'Path'
        

def SearchforRoad(x,y,Mat):
    n = Mat[x][y].nbr_cases
    x1 = 0
    x2 = 0
    if(x !=0 ):
        x1 = x -1
    if(y != 0):
        y1 = y -1
    for i in range(n+3) :
        if(isPath(x1,y1)):
            return (x1,y1)
        x1 = x1+1
    for j in range(n+3):
        if(isPath(x1,y1)) :
            return (x1,y1)
        y1= y1 +1
    for i in range(0,n+1):
        if(isPath(x1,y1)):
            return (x1,y1)
        x1 = x1-1
    for j in range(n+3):
        if(isPath(x1,y1)) :
            return (x1,y1)
        y1= y1 -1
    return (-1,-1)
    


def Delivery(Bat, type_march, quant, Mat):
    (x,y) = SearchforRoad(Bat.pos_x, Bat.pos_y, Mat)
    if(x != -1):
        m.add_perso(x,y,'Delivery Guy', Mat)
        
        
     


def getID(i,j):
    if(m.Mat_batiment[i][j].main == 1):
        return m.Mat_batiment[i][j].id
    else:  return 666

def Add_bat_game(x,y,id_bat):
    if(m.Mat_batiment[x][y].name ==  "Terrain vide" ): #il faut rajouter un or pour le cas où on rajoute un aqueduc sur une route ou vice versa mais comme c'est trop chiant a taper je l'ai pas fait
        m.add_bat(x,y,id_bat, m.Mat_batiment)
    else: return -1