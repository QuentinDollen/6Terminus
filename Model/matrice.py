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
import View.map as Vm

nb_cases_x = 60
nb_cases_y = 60
nb_cases = 60

def init_matrice_terrain(Mat, x, y):
    assert (Mat == [])
    for i in range(x):
        Mat.append([])
        for j in range(y):
            Mat[i].append(t.Terrain(i, j, 2))


# Mat [i][j] : donne un tableau avec la liste des personnages,
def init_matrice_perso(Mat, x, y):
    assert (Mat == [])
    for i in range(x):
        Mat.append([])
        for j in range(y):
            Mat[i].append([])
            Mat[i][j].append([])
            Mat[i][j][0] = w.Walker()


def afficher_matrice_bat(Mat, x, y):
    for i in range(x):
        print("[", end='')
        for j in range(y):
            print(Mat[i][j].name, " ", end='')
        print("]")


def afficher_matrice_perso(Mat, x, y):
    for i in range(x):
        print("[", end='')
        for j in range(y):
            for k in range(len(Mat[i][j])):
                print(Mat[i][j][k].name, " ", end='')
            if (j != y - 1):
                print("| ", end='')
        print("]")

def add_bat(x,y,id_bat):
   
        if(id_bat == 0): globals()["Herb"+x+y] = h.Herb(x,y)
        if(id_bat == 92): bat1 = wa.Well(x,y)
        if(id_bat == 90): globals()["Reservoir"+x+y] = wa.Reservoir(x,y)
        if(id_bat == 91): globals()["Fountain"+x+y] = wa.Fountain(x,y)
        if(id_bat == 8): globals()["Aquaduct"+x+y] = wa.Aquaduct(x,y)
        if(id_bat == 81): globals()["EngineersPost"+x+y] = eng.EngineersPost(x,y)
        if(id_bat == 55): globals()["Prefecture"+x+y] = sec.Prefecture(x,y)


#TESTER SI FONCTIONNE
def departureMatrice(Mat):
    map_depart = View.map.matrix
    for i in range(nb_cases+1):
        for j in range(nb_cases+1):
            Mat[i][j] = map_depart[i][j]
    afficher_matrice_bat(Mat)


#definir calcul de trajectoire
def next_case(i,j,Mat):
    return (i+1,j+1)




def deplacement_perso(Mat,i,j):
    if Mat[i][j][0].name != "Walker":
        for k in range(Mat[i][j].len) :
            if (Mat[i][j][k].destination_x != 666 or Mat[i][j][k].destination_y != 666) :
                (nx,ny) = next_case(i,j,Mat)



Mat_batiment = []
Mat_perso = []

bat1 = b.Batiment(1, "", 1, 1, 0, 0, 0, 0, 0, 0)
p1 = p.Priest()

init_matrice_terrain(Mat_batiment, 3, 3)
Mat_batiment[0][0] = bat1

init_matrice_perso(Mat_perso, 3, 3)

print(Mat_perso[0][0])

afficher_matrice_bat(Mat_batiment, 3, 3)
afficher_matrice_perso(Mat_perso, 3, 3)



