import os
import sys

# Construct the full path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the PYTHONPATH
sys.path.append(parent_dir)

import pygame as pg
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


# Definition des Userevents

Nume_maison = pg.USEREVENT 
Nume_eau = pg.USEREVENT +1
Nume_route = pg.USEREVENT +2
Nume_theatre = pg.USEREVENT +3
Nume_nourriture = pg.USEREVENT+4 
Nume_sante = pg.USEREVENT +5
Nume_prefecure = pg.USEREVENT+6 
Nume_ingenieur = pg.USEREVENT +7
Nume_administratif = pg.USEREVENT+8 
Nume_pelle = pg.USEREVENT +9


# pour les variables globales: il nous faut la liste des greniers et des entrepots, et faire une methode qui dit s'ils sont plein ou pas
# pour eviter de devoir faire un scan sur toute la matrice a chaque fois qu'on a besoin de faire une livraison

# cree un walker pour effectuer une livraison
# prend en parametre le batiment qui invoque la livraison, le type de marchandise, la quantité 
def Delivery(Bat_depart, type_march, quant):
    (x, y) = m.SearchforRoad(Bat_depart.pos_x, Bat_depart.pos_y, m.Mat_batiment)
    if (x != -1):
        cible = m.SearchforSpace(type_march)
        if cible == None:
            return -1
        dg = m.add_perso(x, y, 'Delivery Guy', m.Mat_perso, Bat_depart, cible, type_march)
        dg.ajout_marchandise(quant)
        # Bat dest devra être calculé : grenier, entrepot, marché
        (cx,cy) = cible.ret_coord()
        print("cible",cx,cy)
        (dx, dy) = m.SearchforRoad(cx, cy, m.Mat_batiment)
        dg.dest_x = dx
        dg.dest_y = dy
        print(dx,dy)


# renvoie l'ID d'un batiment placé sur une case de la matrice des batiments, dont les coordonées sont données en argument
# Pour un batiment de plusieurs cases, ne donne l'id que si la case est celle en haut, autrement renvoie 666
def getID(i, j):
    if m.Mat_batiment[j][i].pos_x + m.Mat_batiment[j][i].nbr_cases - 1 == i and m.Mat_batiment[j][i].pos_y + m.Mat_batiment[j][i].nbr_cases - 1 == j:
        return m.Mat_batiment[j][i].id
    else:
        return 666

def getID_base_matrix( i , j ) : 
    return m.matrix[j][i]

# initialise les matrices de jeux
# incomplet: reste à implémenter les load
def init_game():
    m.departureMatrice(m.Mat_batiment)

# ajoute un batiment si l'espace sur la carte est libre
def Add_bat_game(x, y, id_bat):
    for i in range(m.id_size[id_bat]):
        for j in range(m.id_size[id_bat]):
            if m.Mat_batiment[y + j][x + i].name != "Herb":
                return -1
    m.add_bat(x, y, id_bat, m.Mat_batiment)
    return 0


class State:
    def __init__(self):
        self.Matrice_bat = m.Mat_batiment
        self.Matrice_perso = m.Mat_perso
        # self.Variable_Globale = [] # will be used later, now there's nothing to put in there

    def mise_a_jour(self):
        self.Matrice_bat = m.Mat_batiment
        self.Matrice_perso = m.Mat_perso
        # self.Variable_Globale = []

    def uploadFromSave(self):
        m.Mat_batiment = self.Matrice_bat
        m.Mat_perso = self.Matrice_perso

# creer un fichier de sauvegarde, à partir de l'état actuel du jeu
def sauvegarde(nom):
    sauv = State()
    with open(nom, "wb") as f:
        pickle.dump(sauv, f)

# charge un fichier de sauvegarde et met a jour le jeu
def load(nom):
    sauv = State()
    with open(nom, "rb") as f:
        sauv = pickle.load(f)
    sauv.uploadFromSave()

# a garder
init_game()

#

# partie test

#print(Add_bat_game(2, 0, 5))
#m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
#print("***  modification en cours ****")
#m.add_bat(0,0,0,m.Mat_batiment)
#m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
#print("***  test de sauvegarde ****")

#sauvegarde("sauv1")
#m.add_bat(1,0,0,m.Mat_batiment)
#m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
#print("**** test du load ****")

#load("sauv1")
#m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
# Add_bat_game(0,6,100)
# Add_bat_game(1,5,5)

# Delivery(m.Mat_batiment[6][0],'ble',11)
# Delivery(m.Mat_batiment[6][0],'ble',8)
# Delivery(m.Mat_batiment[6][0],'argile',15)

# print("coordonee",m.SearchforRoad(2,1,m.Mat_batiment))
# m.afficher_matrice_bat(m.Mat_batiment, 9, 9)
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)
# m.deplacement_perso(m.Mat_perso)
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)

# m.deplacement_perso(m.Mat_perso)
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)

# m.deplacement_perso(m.Mat_perso)
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)

# m.deplacement_perso(m.Mat_perso)
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)


# m.deplacement_perso(m.Mat_perso)
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)

# m.deplacement_perso(m.Mat_perso)

# m.deplacement_perso(m.Mat_perso)
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)
# print(" ")
# m.afficher_matrice_bat(m.Mat_batiment, 9, 9)

# print(m.Mat_batiment[1][2].nourriture)
# print(m.Mat_batiment[1][2].produits)
