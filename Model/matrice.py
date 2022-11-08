import math as m
import numpy as np
import batiment as b
import terrain as t
import maison as m
import Walker as w
import Priest as p

nb_cases_x = 60
nb_cases_y = 60


def init_matrice_terrain(Mat, x, y):
    assert (Mat == [])
    for i in range(x):
        Mat.append([])
        for j in range(y):
            Mat[i].append(t.Terrain(i, j))


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



