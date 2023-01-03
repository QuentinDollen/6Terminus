import sys
import random
sys.path.insert(0, '..')

from Model import terrain as t
from Model import maison as mais
from Model import Walker as w
from Model import water as wa
from Model import engineering as eng
from Model import security as sec
from Model import herb as h
from Model import delivery_guy as dv
from Model import administration as admin
from Model import path as pa
from Model import tree as tr
from Model import ferme as f
from Model import granary as g
from Model import warehouse as war
from copy import copy

# matrice de depart par defaut
matrix = [[3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           0, 0, 0, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 65, 3, 3, 3, 3,
           3, 3, 0, 0, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 0, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3,
           3, 3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 0, 3,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3,
           3, 3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           3, 3, 3, 0],
          [3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1,
           1, 3, 1, 3],
          [3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1,
           1, 1, 1, 1],
          [3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 1, 1,
           1, 1, 1, 1],
          [3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3,
           1, 1, 1, 1],
          [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
           3, 3, 1, 1],
          [0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
           0, 0, 0, 3],
          [0, 0, 0, 0, 0, 3, 3, 3, 0, 5, 5, 5, 5, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3,
           3, 3, 3, 3],
          [0, 0, 7, 7, 3, 3, 3, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0,
           0, 3, 3, 3],
          [3089, 0, 7, 7, 7, 7, 7, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 3087, 0],
          [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
           5, 5, 5, 5],
          [0, 5, 0, 5, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0,
           0, 0, 0, 0],
          [0, 5, 5, 5, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 0, 0, 3],
          [1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 3],
          [1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 39, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           0, 3, 0, 3, 3],
          [1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 0, 3, 3],
          [1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 39, 3, 3, 3, 3,
           3, 3, 3, 3, 3],
          [0, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 0, 0, 0, 2, 0, 0, 2, 2, 3, 2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3,
           3, 3, 3, 3],
          [3, 0, 1, 1, 1, 1, 1, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 2, 2, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 3, 3],
          [3, 3, 3, 1, 1, 1, 1, 0, 0, 3, 0, 0, 2, 2, 0, 0, 0, 3, 3, 0, 0, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
           3, 3, 3, 3],
          [0, 3, 3, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 2, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 2, 3, 0, 0, 3, 3, 0, 3, 3, 3, 3,
           3, 3, 3, 3, 3],
          [3, 3, 3, 3, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3,
           3, 3, 3, 3],
          [3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 3, 3, 3, 3,
           3, 0, 0, 3, 3],
          [3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 3],
          [3, 3, 0, 0, 0, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0],
          [3, 0, 2, 0, 0, 0, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 2, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0,
           0, 0, 2, 2],
          [0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
           0, 0, 0, 0],
          [0, 0, 0, 2, 0, 0, 2, 2, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 2, 0,
           0, 0, 2, 2],
          [0, 0, 0, 0, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 3, 3, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 2, 2, 2, 0,
           0, 0, 2, 2]
          ]

nb_cases_x = 40
nb_cases_y = 40
nb_cases = 40

#liste servant a retenir l'ensemble des batiments servant a stocker des marchandises
Liste_stock = []


def SearchforSpace():
    for i in range(len(Liste_stock)):
        if(Liste_stock[i].isFull() != 1):
            return Liste_stock[i]
    return None

# creer une matrice de taille passée en argument. (n'est pas utilisable en jeu)
def init_matrice_terrain(Mat, x, y):
    assert (Mat == [])
    for j in range(y):
        Mat.append([])
        for i in range(x):
            Mat[j].append(h.Herb(i, j))


# la fonction initialise le tableau des walker
# Mat [j][i] est un tableau avec la liste des personnages, si y en a aucun c'est le type walker par défaut. (parce qu'on a besoin de l'attribut name)
# en jeu on utilisera Mat_perso
def init_matrice_perso(Mat, x, y):
    assert (Mat == [])
    for j in range(y):
        Mat.append([])       
        for i in range(x):
            Mat[j].append([])
            Mat[j][i].append([])
            Mat[j][i][0] = w.NoWalker()


# Créer une matrice route utile pour les déplacement des walkers 
def init_matrice_route( Mat_route , cases_x = nb_cases_x , cases_y = nb_cases_y ) :
    assert Mat_route == []
    for i in range ( cases_x ) :
        Mat_route.append([])
        for j in range( cases_y ) :
            Mat_route[i].append([])
            Mat_route[i][j] = 0 



### a garder #############################
Mat_batiment = []
Mat_perso = []
Mat_route = []
init_matrice_terrain(Mat_batiment, nb_cases_x, nb_cases_y)
init_matrice_perso(Mat_perso, nb_cases_x, nb_cases_y)
init_matrice_route( Mat_route , nb_cases_x , nb_cases_y)

############################################


# Actualise la matrice de route
def actualiser_matrice_route() :
    for i in range ( nb_cases_x ) :
        for j in range ( nb_cases_y ) :
            Mat_route[i][j] = isPath(i,j)


# test utiliser pour afficher la matrice des batiments ( utilise le nom )
def afficher_matrice_bat(Mat, x, y):
    for j in range(y):
        print("[", end='')
        for i in range(x):
            print(Mat[j][i].name, " ", end='')
        print("]")


# test utiliser pour afficher la matrice des personnage (utilise le type) (walker revient a ce qu'il n'y aie aucun perso dans la case)
def afficher_matrice_perso(Mat, x, y):
    for j in range(y):
        print("[", end='')
        for i in range(x):
            n = len(Mat[j][i])
            for k in range(n):
                print(Mat[j][i][k].name, " ", end='')
                if n > 1 and k != n - 1:
                    print("; ", end = '')
            if i != x - 1:
                print("| ", end='')
        print("]")

# Afficher la carte de la route :

def afficher_mat_route( taille ) :
    for i in range( taille ) :
        print("[ ", end='')
        for j in range( taille ) :
            print( Mat_route[i][j] , " " , end="")
        print("]")

# dictionnaire reliant l'id des batiments a la taille qu'ils occupent
id_size = {0: 1, 92: 1, 90: 3, 91: 1, 8: 1, 81: 1, 55: 1, 5: 1, 84: 2, 71: 3, 72: 3, 100: 3, 101: 3, 103: 3, 109: 2,
           111: 2, 114: 2, 1: 1, 2: 1, 3: 3, 115: 1, 116: 1, 7: 1}

# dictionnaire reliant le nom des batiments avec leur id
name_id = {"Well" : 92, "Reservoir" : 90, "Fountain" : 91, "Aquaduct" : 8, "EngineersPost" : 81, "Prefecture" : 55, "Path" : 5, "Forum1" : 84, "Water" : 1, "Rock" : 2, "Tree" : 3, "Senate1" : 4, "Maison1" : 10, "Maison2" : 11, "Maison3" : 12, "Maison4": 13, "Farm" : 100, "Granary" : 71, "Warehouse" : 71, "Herb" : 0 }

# permet de inserer un batiment dans la matrice sur toute la taille qu'il occupe (non utilisable en jeu)
def put_bat_mat(x, y, bat, Mat):
    for i in range(0, bat.nbr_cases):
        for j in range(0, bat.nbr_cases):
            Mat[y + j][x + i] = bat


# ajoute un batiment a une position specifiee en fonction de l'id
# on utilise Mat_batiment
# si le batiment est de type stockage, l'ajoute a la liste des batiments de stockage
def add_bat(x, y, id_bat, Mat):
    if id_bat == 92:
        well = wa.Well(x, y)
        Mat[y][x] = well
    if id_bat == 90:
        Reservoir = wa.Reservoir(x, y)
        put_bat_mat(x, y, Reservoir, Mat)
    if id_bat == 91:
        Fountain = wa.Fountain(x, y)
        Mat[y][x] = Fountain
    if id_bat == 8:
        Aquaduct = wa.Aquaduct(x, y)
        Mat[y][x] = Aquaduct
    if id_bat == 81:
        EngineersPost = eng.EngineersPost(x, y)
        Mat[y][x] = EngineersPost
    if id_bat == 55:
        Prefecture = sec.Prefecture(x, y)
        Mat[y][x] = Prefecture
    if id_bat == 5:
        Route = pa.Path(x, y)
        Mat[y][x] = Route
        Mat_route[y][x] = 1 
    if id_bat == 84:
        Forum = admin.Forum1(x, y)
        put_bat_mat(x, y, Forum, Mat)
    if id_bat == 1:
        Mat[y][x] = t.Water(x, y)
    if id_bat == 2:
        Mat[y][x] = t.Rock(x, y)
    if id_bat == 3:
        Mat[y][x] = tr.tree(x, y)
    if id_bat == 4:
        Senate = admin.Senate1(x, y)
        put_bat_mat(x, y, Senate, Mat)
    if id_bat == 10:
        Maison_1 = mais.Maison_1(x, y)
        put_bat_mat(x, y, Maison_1, Mat)
    if id_bat == 11:
        Maison_2 = mais.Maison_2(x, y)
        put_bat_mat(x, y, Maison_2, Mat)
    if id_bat == 12:
        Maison_3 = mais.Maison_3(x, y)
        put_bat_mat(x, y, Maison_3, Mat)
    if id_bat == 13:
        Maison_4 = mais.Maison_4(x, y)
        put_bat_mat(x, y, Maison_4, Mat)
    if id_bat == 100:
        Ferme = f.Ferme(x, y)
        put_bat_mat(x, y, Ferme, Mat)
    if id_bat == 71:
        Granary = g.Granary(x, y)
        put_bat_mat(x, y, Granary, Mat)
        Liste_stock.append(Granary)
    if id_bat == 72:
        Warehouse = war.Warehouse(x, y)
        put_bat_mat(x, y, Warehouse, Mat)
        Liste_stock.append(Warehouse)
    if id_bat == 115:
        Mat[y][x] = tr.Enter_Pannel(x, y)
    if id_bat == 116:
        Mat[y][x] = tr.Exit_Pannel(x,y)
    if id_bat == 0:
        Herb = h.Herb(x, y)
        Mat[y][x] = Herb


# globals()["Prefecture"+x+y] # truc interessant dont on se sert pas, à conserver pour plus tard

# ajoute un walker a une matrice donnnee en argument (on utilisera Mat_perso)
def add_perso_mat(Mat, perso, x, y):
    if Mat[y][x][0].name == "no Walker":
        Mat[y][x][0] = perso
    else:
        print("test4")
        Mat[y][x].append(perso)


# cree un personnage de type specifié par un string
def add_perso(x, y, type_, Mat, Bat, Bat_cible):
    if type_ == 'Delivery Guy':
        DV = dv.Delivery_Guy(x, y, Bat, Bat_cible)
        add_perso_mat(Mat, DV, x, y)
        Bat.Walk.append(DV)
        return DV
    if type_ == "Engeneer" :
        EN = eng.EngineersPost(x,y)
        add_perso_mat(x,y,type_ , Mat , Bat , Bat_cible )
        Bat.Wal

# charge la matrice de départ par défaut dans la matrice donnée en argument
def departureMatrice(Mat):
    map_depart = matrix
    for i in range(0, nb_cases_x):
        for j in range(0, nb_cases_y):
            if map_depart[j][i]:
                add_bat(i, j, map_depart[j][i], Mat)
    afficher_matrice_bat(Mat, nb_cases_x, nb_cases_y)


# teste si l'emplacement x,y d'une matrice correspond a un chemin
def isPath(x, y, Mat):
    return Mat[y][x].name == 'Path'


# SearchforRoad renvoie la position de la première route rencontrée autour (distance de 1) d'un batiment situé en x,y
def SearchforRoad(x, y, Mat):
    n = Mat[y][x].nbr_cases
    x1 = 0
    y1 = 0
    if x != 0:
        x1 = x - 1
    if y != 0:
        y1 = y - 1
    for i in range(n + 1):
        if isPath(x1, y1, Mat):
            return x1, y1
        x1 = x1 + 1
    for j in range(n + 1):
        if isPath(x1, y1, Mat):
            return x1, y1
        y1 = y1 + 1
    for i in range(0, n + 1):
        if isPath(x1, y1, Mat):
            return x1, y1
        x1 = x1 - 1
    for j in range(n + 1):
        if isPath(x1, y1, Mat):
            return x1, y1
        y1 = y1 - 1
    return -1, -1


# cherche si une valeur est déjà presente dans un tableau
def InTable(x, tab):
    bool_ = 0
    for i in range(len(tab)):
        if x == tab[i]:
            bool_ = 1
    return bool_


def min_tab_tab_notnull(tab):  # take a tab of tab and return the tab in the tab of tab, with the smallest size
    n = len(tab)
    min_ = tab[0]
    for i in range(n):
        if len(min_) > len(tab[i]):
            min_ = tab[i]
    return min_


# fonction de pathfinding
def next_case(x, y, tab_path, dest_x, dest_y, Mat):
    assert (isPath(x, y, Mat))
    if x == dest_x and y == dest_y:
        return tab_path
    else:
        tab1 = []
        tab2 = []
        tab3 = []
        tab4 = []
        test = 0
        if isPath(x + 1, y, Mat) and not InTable((x + 1, y), tab_path):
            test = 1
            tab1 = copy(tab_path)
            tab1.append((x + 1, y))
            tab1 = next_case(x + 1, y, tab1, dest_x, dest_y, Mat)
        if isPath(x, y + 1, Mat) and not InTable((x, y + 1), tab_path):
            test = 1
            tab2 = copy(tab_path)
            tab2.append((x, y + 1))
            tab2 = next_case(x, y + 1, tab2, dest_x, dest_y, Mat)
        if isPath(x - 1, y, Mat) and not InTable((x - 1, y), tab_path):
            test = 1
            tab3 = copy(tab_path)
            tab3.append((x - 1, y))
            tab3 = next_case(x - 1, y, tab3, dest_x, dest_y, Mat)
        if isPath(x, y - 1, Mat) and not InTable((x, y - 1), tab_path):
            test = 1
            tab4 = copy(tab_path)
            tab4.append((x, y - 1)) 
            tab4 = next_case(x, y - 1, tab4, dest_x, dest_y, Mat)
        if(test == 0):
            return []
        tab = []
        if tab1 != []:
            tab.append(tab1)
        if tab2 != []:
            tab.append(tab2)
        if tab3 != []:
            tab.append(tab3)
        if tab4 != []:
            tab.append(tab4)
        final_tab = []
        if(tab != []):
            final_tab = min_tab_tab_notnull(tab)
        return final_tab

# supprime un batiment d'une matrice, à l'aide de ses coordonées
def suppr_Batiment(x,y,Mat):
    for i in range(0, Mat[y][x].nbr_cases):
        for j in range(0, Mat[y][x].nbr_cases):
            Mat[Mat[y][x].pos_y + j][Mat[y][x].pos_x + i] = h.Herb(Mat[y][x].pos_x + i, Mat[y][x].pos_y + j)


# !!! Pour un walker !!!
# deplacement normal: aller tout de droit puis faire demi tour apres une certaine distance
# doit prendre une direction au pif a un croisement
# renvoie le prochain x et le prochain y
def Deplacement_basique_v2( Mat = Mat_perso, nb_x = nb_cases_x , nb_y = nb_cases_y , no_walker = 0  ): 
    for i in range( nb_x ) :
        for j in range( nb_y ) :
            if  Mat[i][j][0].name != "no Walker" :
                print( ( i , j) )
                tab_possibles_chemins = []
                if Mat_route[i+1][j] and ( Mat[i][j][no_walker].prev_x , Mat[i][j][no_walker].prev_y ) != ( i , j ) :
                    tab_possibles_chemins.append((i,j))
                if Mat_route[i-1][j] and ( Mat[i][j][no_walker].prev_x , Mat[i][j][no_walker].prev_y ) != ( i , j ) :
                    tab_possibles_chemins.append((i,j))
                if Mat_route[i][j+1] and ( Mat[i][j][no_walker].prev_x , Mat[i][j][no_walker].prev_y ) != ( i , j ) :
                    tab_possibles_chemins.append((i,j))
                if Mat_route[i][j-1] and ( Mat[i][j][no_walker].prev_x , Mat[i][j][no_walker].prev_y ) != ( i , j ) :
                    tab_possibles_chemins.append((i,j))
                match len( tab_possibles_chemins ) :
                    case 0 : 
                        
                         return ( Mat[i][j][no_walker].prev_x , Mat[i][j][no_walker].prev_y ) # Demi tour
                    case _  : return tab_possibles_chemins[ random.randrange(0 ,  len ( tab_possibles_chemins ) ) ] # Aléatoire 

# deplacement normal: aller tout de droit puis faire demi tour apres une certaine distance
# doit prendre une direction au pif a un croisement
# renvoie le prochain x et le prochain y
def Deplacement_basique( x , y , no_walker = 0  ): 

    if Mat_perso[y][x][no_walker].ttl <= 0 :
        ( Mat_perso[y][x][no_walker].dest_y , Mat_perso[y][x][no_walker].dest_x ) = ( Mat_perso[y][x][no_walker].bat.pos_y, Mat_perso[y][x][no_walker].bat.pos_x )
        pass # Aller vers son batiment 

        tab_possibles_chemins = []
        if x < nb_cases_x - 1 :

            if Mat_route[y][x+1] and ( Mat_perso[y][x][no_walker].prev_x , Mat_perso[y][x][no_walker].prev_y ) != ( x , y ) :
                tab_possibles_chemins.append((x+1,y))
        if x > 0  :
            if Mat_route[y][x-1] and ( Mat_perso[y][x][no_walker].prev_x , Mat_perso[y][x][no_walker].prev_y ) != ( x , y ) :
                tab_possibles_chemins.append(( x-1 , y ))
        if y < nb_cases_y - 1 :        
            if Mat_route[y+1][x] and ( Mat_perso[y][x][no_walker].prev_x , Mat_perso[y][x][no_walker].prev_y ) != ( x , y ) :
                tab_possibles_chemins.append(( x , y+1 ))
        if y > 0 :
            if Mat_route[y-1][x] and ( Mat_perso[y][x][no_walker].prev_x , Mat_perso[y][x][no_walker].prev_y ) != ( x , y ) :
                tab_possibles_chemins.append(( x , y-1 ))

        if len( tab_possibles_chemins ) > 0 :
            return tab_possibles_chemins[ random.randrange(0 ,  len ( tab_possibles_chemins ) ) ] # Aléatoire 
        else : 
            return ( Mat_perso[y][x][no_walker].prev_y , Mat_perso[y][x][no_walker].prev_x )
                

                    

# verifie que la distance entre deux cases est de 1 (y compris en diagonale)
def dist(x1,y1,x2,y2):
    return( (x1 == x2 and (abs(y1-y2) == 1)) or (y1 == y2 and (abs(x1-x2) == 1)) or ( (x2-x1)**2 + (y2-y1)**2 == 2))

# procede a un echange d'un walker de type delivery guy passé en parametre, ssi il se trouve a proximite de son batiment cible
def echange(DV):
    print("echange")
    if dist(DV.bat_destination.pos_x, DV.bat_destination.pos_y, DV.x, DV.y):
        print("dechargement:",DV.cargaison_nourriture)
        DV.bat_destination.get_delivery(DV.dechargement('ble'))

# deplace l'ensemble des walker
# possibilité de l'implémenter avec de la mise en parralèle
# si un walker arrive a destination procede a un echange
# pas terminé: il faut que on puisse echanger dès qu'on est a proximité et que le path soit remis a jours
# un walker arrive a destination doit soit mourir soit revenir a son batiment d'origine
# il faut implémenter des "missions" pour les walkers: definir le type de marchandise a acheminer, parce que echange marche juste avec ble pour l'instant
def deplacement_perso(Mat, tx=nb_cases, ty=nb_cases):
    for i in range(tx):
        for j in range(ty):
            if Mat[j][i][0].name != "no Walker": # Pour toute cases, si on a un walker
                for k in range(len(Mat[j][i])):
                    count = 0
                    if Mat[j][i][count].has_moved == 1:
                        count = count+1
                    else :
                        Mat[j][i][count].has_moved = 1
                        if Mat[j][i][count].dest_x != -1 and Mat[j][i][count].dest_y != -1:
                            if Mat[j][i][count].tab_path == []:
                                new_path = next_case(i, j, [(i, j)], Mat[j][i][count].dest_x, Mat[j][i][count].dest_y, Mat_batiment)
                                if(new_path == []):
                                    new_path.append((i,j))
                                Mat[j][i][count].tab_path = new_path
                                
                            Mat[j][i][count].tab_path.pop(0)
                            if len(Mat[j][i][count].tab_path) != 0:
                                (nx, ny) = Mat[j][i][count].tab_path[0]
                            else:
                                if(Mat[i][j][count].name == "Delivery_Guy" or Mat[i][j][count].name == "Food_guy"):
                                    echange(Mat[j][i][count])
                                nx = i
                                ny = j
                        else:
                            (nx,ny) = Deplacement_basique(i ,j , no_walker=count )
                            
                        if(nx == i and ny == j):
                            count = count + 1
                        else:
                            if(not isPath(nx,ny,Mat_batiment)):
                                new_path = next_case(i, j, [(i, j)], Mat[j][i][count].dest_x, Mat[j][i][count].dest_y, Mat_batiment)
                                Mat[j][i][count].tab_path = new_path
                                count = count + 1
                            else:
                                walk = Mat[j][i][count]
                                Mat[j][i].pop(count)
                                if len(Mat[j][i]) == 0:
                                    Mat[j][i].append(w.NoWalker())
                                walk.x = nx
                                walk.y = ny
                                walk.prev_x = i
                                walk.prev_y = j
                                add_perso_mat(Mat, walk, nx, ny)
    for i in range(tx):
        for j in range(ty):
            if Mat[j][i][0].name != "no Walker":
                for k in range(len(Mat[j][i])):
                    Mat[j][i][k].has_moved = 0





# non necessaire, juste un test

add_bat(1, 1, 5, Mat_batiment)
add_bat(1, 2, 5, Mat_batiment)
add_bat(1, 3, 5, Mat_batiment)
add_bat(1, 4, 5, Mat_batiment)
add_bat(2, 4, 5, Mat_batiment)
add_bat(3, 4, 5, Mat_batiment)
add_bat(4, 4, 5, Mat_batiment)

afficher_matrice_bat(Mat_batiment,8,8)


add_bat(4,5,10, Mat_batiment)
add_bat(2,1,72,Mat_batiment)
DV = add_perso(1, 1, "Delivery Guy", Mat_perso, Mat_batiment[1][1], Mat_batiment[5][4])
DV.ajout_marchandise('ble',6)
print("cargaison",DV.cargaison_nourriture)
Mat_perso[1][1][0].dest_x = 4 # ces valeurs devraient normalement être obtenue avec SearchforRoad()
Mat_perso[1][1][0].dest_y = 4

#
#
# 
afficher_matrice_bat(Mat_batiment, 7, 7)
afficher_matrice_perso(Mat_perso, 5, 5)

deplacement_perso(Mat_perso)

deplacement_perso(Mat_perso)
suppr_Batiment(1,4,Mat_batiment)
afficher_matrice_bat(Mat_batiment, 7,7)
deplacement_perso(Mat_perso)

deplacement_perso(Mat_perso)
deplacement_perso(Mat_perso)
deplacement_perso(Mat_perso)
print(" ")
add_bat(1,4,5,Mat_batiment)
afficher_matrice_bat(Mat_batiment, 7, 7)
deplacement_perso(Mat_perso)
afficher_matrice_perso(Mat_perso,7,7)

print(" ")
deplacement_perso(Mat_perso)

afficher_matrice_perso(Mat_perso,7,7)
deplacement_perso(Mat_perso)
deplacement_perso(Mat_perso)
deplacement_perso(Mat_perso)
deplacement_perso(Mat_perso)
deplacement_perso(Mat_perso)
afficher_matrice_perso(Mat_perso,7,7)
deplacement_perso(Mat_perso)
afficher_matrice_perso(Mat_perso,7,7)
print("test livraison")
print(Mat_batiment[5][4].nourriture)

add_bat(1,0,5,Mat_batiment)
afficher_matrice_bat(Mat_batiment,3,3)
print(Mat_batiment[0][1].name)

print("Test Quentin")

DVD = add_perso(0 , 0 , "Delivery Guy" ,Mat_perso , Mat_batiment[1][1], Mat_batiment[5][4])
DVD.prev_x = 1 
DVD.prev_y = 4
afficher_mat_route( 7 )
afficher_matrice_perso(Mat_perso,7,7)
add_bat( 4 , 5 , 5 , Mat_batiment )
afficher_matrice_bat(Mat_batiment , 7 , 7 )
print( Deplacement_basique( 0 , 0 ) )
