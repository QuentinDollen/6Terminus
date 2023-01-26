import pygame as pg
import pickle
import sys

sys.path.insert(0, '..')

from Model import matrice as m


#walker nx ny, batiment detruire plusieurs cases, maisons construires plusieurs cases
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

Unalterable = [0,1,2,3,4,5,6,666,116,115]

# En jeu (dans le main), on n'utilisera que les fonctions de logique.py, celles prÃ©sente dans les autres fichiers servent de briques pour celles prÃ©sentes ici


# pour les variables globales: il nous faut la liste des greniers et des entrepots, et faire une methode qui dit s'ils sont plein ou pas
# pour eviter de devoir faire un scan sur toute la matrice a chaque fois qu'on a besoin de faire une livraison

# cree un walker pour effectuer une livraison
# prend en parametre le batiment qui invoque la livraison, le type de marchandise, la quantité
def Delivery(Bat_depart, type_march, quant):
    (x, y) = m.SearchforRoad(Bat_depart.pos_x, Bat_depart.pos_y, m.Mat_batiment)
    if x != -1:
        cible = m.SearchforSpace(type_march)
        if cible == None:
            return -1
        print("MUDA MUDA")
        dg = m.add_perso(x, y, 'Delivery Guy', m.Mat_perso, Bat_depart, cible, type_march)
        dg.ajout_marchandise(quant)
        # Bat dest devra être calculé : grenier, entrepot, marché
        (cx, cy) = cible.ret_coord()
        print("cible", cx, cy)
        (dx, dy) = m.SearchforRoad(cx, cy, m.Mat_batiment)
        dg.dest_x = dx
        dg.dest_y = dy
        print(dx, dy)



# renvoie l'ID d'un batiment placé sur une case de la matrice des batiments, dont les coordonées sont données en argument
# Pour un batiment de plusieurs cases, ne donne l'id que si la case est celle en haut, autrement renvoie 666
def getID(i, j):
    if m.Mat_batiment[j][i].pos_x + m.Mat_batiment[j][i].nbr_cases - 1 == i and m.Mat_batiment[j][i].pos_y + \
            m.Mat_batiment[j][i].nbr_cases - 1 == j:
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

def get_fire_level(x,y):
    if m.Mat_batiment[y][x].id not in Unalterable:
        return m.Mat_batiment[y][x].ind_fire
    return -1 

def get_eff_level(x,y):
    if m.Mat_batiment[y][x].id not in Unalterable:
        return m.Mat_batiment[x][y].eff
    return -1

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


def getWalker(i, j):
        return m.Mat_perso[j][i][0]

def getDesirability(bat):
    proxy = m.get_bat_prox(bat.pos_x,bat.pos_y,5)
    somme = 0
    for batis in proxy:
        somme += batis.initDesirability
    return somme

# fonction qui a realiser des opérations entre walkers et batiments:
# si c'est un pompier, il va diminuer les indices de feu des batiments autour de lui, et si il y a un feu, doit aller l'eteindre
# si c'est un ingenieur, il va diminuer les indices d'effondrement des batiments autour de lui
# si c'est un Delivery_Guy, et qu'il est a destination, il va proceder a un echange (il faut enlever cette partie du deplacement pour la mettre içi)
# si c'est pretre, il va augmenter l'indice de foi des maisons autour de lui
# si c'est un Food_Guy, et que sa mission est de distribuer des biens/bouffe aux habitants, il va donner une certaine quantité de ce qu'il a aux maisons autour de lui
def test_walker_logique():
    for i in range(m.nb_cases):
        for j in range(m.nb_cases):
            if m.Mat_perso[j][i][0].name != "no Walker":
                for k in range(len(m.Mat_perso[j][i])):
                    perso = m.Mat_perso[j][i][k]
                    if perso.name == "Prefect":
                        proxy = m.get_bat_prox(i, j, 2)
                        print("proxy", proxy)
                        for bat in proxy:
                            bat.ind_fire = 0
                    elif perso.name == "Engineer":
                        proxy = m.get_bat_prox(i, j, 2)
                        print("proxy", proxy)
                        for bat in proxy:
                            bat.ind_eff = 0
                    elif perso.name == "Priest":
                        proxy = m.get_bat_prox(i, j, 4)
                        print("proxy", proxy)
                        for bat in proxy:
                            if m.InTable(bat.name, ["Maison 1", "Maison 2", "Maison 3", "Maison 4"]):
                                bat.faith = bat.faith + 40
                    elif perso.name == "Recruteur":
                        proxy = m.get_bat_prox(i, j, 4)
                        print("proxy", proxy)
                        for bat in proxy:
                            if m.InTable(bat.name, ["Maison 1", "Maison 2", "Maison 3", "Maison 4"]):
                                recruit = perso.nb_a_recruter
                                if bat.employed < bat.curpop and recruit > 0:
                                    if (bat.curpop - bat.employed) >= recruit:
                                        bat.employed += recruit
                                        perso.nb_a_recruter = 0
                                    else:
                                        perso.nb_a_recruter -= (bat.curpop - bat.employed)
                                        bat.employed = bat.curpop
                        if perso.nb_a_recruter == 0:
                            m.kill_walker(perso)
                    elif perso.name == "Delivery_Guy" and perso.HasSomething():
                        m.echange(perso)
                    elif perso.name == "Food_Guy":
                        if perso.role == 'distributeur':
                            proxy = m.get_bat_prox(i, j, 4)
                            if perso.dest_x == -1:
                                for bat in proxy:
                                    if m.InTable(bat.name, ["Maison 1", "Maison 2", "Maison 3", "Maison 4"]):
                                        m.giveFood(perso, bat)
                        else:
                            continue


# fonction qui teste les condition des batiments:
# va tester le feu, l'effondrement
# si un batiment a produit quelque chose, appelle un livraison
# si un marché a besoin de produits, va en chercher
# si un marché a des produits, appelle une distribution (reste a implementer)
# si c'est une maison, va consommer de la nourriture, tester l'evolution / regression de la maison
def test_bat_logique():
    m.check_fire_eff()
    for i in range(m.nb_cases):
        for j in range(m.nb_cases):
            bat = m.Mat_batiment[j][i]

            if bat.name != "Enter_Pannel" and bat.curEmployees < bat.neededEmployees and not bat.hasRecruteur:
                m.invoke_walker(bat, "Recruteur")
            elif bat.hasCheck == 0:
                bat.hasCheck = 1
                if bat.name == "Farm":
                    bat.growFood()
                    if bat.ind_Harv >= 6:
                        print("time for delivery")
                        Delivery(bat, 'ble', bat.ind_Harv * 2)
                        bat.ind_Harv = 0
                elif bat.name == "Prefecture":
                    if bat.Walk == []:
                        m.invoke_walker(bat, "Prefect")
                elif bat.name == "EngineersPost":
                    if bat.Walk == []:
                        m.invoke_walker(bat, "Engineer")
                elif bat.name == "Temple":
                    if bat.Walk == []:
                        m.invoke_walker(bat, "Priest")
                elif bat.name == "Market":
                    if bat.occupied_space <= 15:
                        #m.add_perso()
                        pass
                elif m.InTable(bat.name,["Panneau", "Maison 1", "Maison 2", "Maison 3"]):
                    if(bat.curpop < bat.popLim):
                        n = getDesirability(bat)
                        if n >= 0:
                            pass





    for i in range(m.nb_cases):
        for j in range(m.nb_cases):
            m.Mat_batiment[j][i].hasCheck = 0

def test_event(event):
    # if(event == Nume_maison):
    # elif(event == Nume_eau):
    # elif(event == Nume_route):
    # elif(event == Nume_theatre):
    # elif(event == Nume_nourriture):
    # elif(event == Nume_prefecure):
    # elif(event == Nume_pelle):


    print("")

def build_pannel_grid(x1, y1, x2, y2):
    for i in range(min(x1,x2), max(x1,x2)+1):
        for j in range(min(y1,y2), max(y1,y2)+1):
            Add_bat_game(i, j, m.name_id["Panneau"])

def destroy_grid(x1,y1,x2,y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            m.suppr_Batiment(i,j,m.Mat_batiment)

def isHerb(x,y):
    return m.Mat_batiment[y][x].name == "Herb"


def Square_path(x1,y1,x2,y2):
    if all(isHerb(i,y1) for i in range(x1,x2+1)) and all(isHerb(x2,j) for j in range(y1,y2+1)):
        for i in range(x1,x2+1):
            Add_bat_game(i,y1,m.name_id["Path"])
        for j in range(y1,y2+1):
            Add_bat_game(x2,j,m.name_id["Path"])
    elif all(isHerb(x1,j) for j in range(y1,y2+1)) and all(isHerb(i,y2) for i in range(x1,x2+1)):
        for j in range(y1,y2+1):
            Add_bat_game(x1,j,m.name_id["Path"])
        for i in range(x1,x2+1):
            Add_bat_game(i,y2,m.name_id["Path"])


def event_to_logic(nume, pos_init, pos_final):
    if nume == Nume_maison:
        (x1, y1) = pos_init
        (x2, y2) = pos_final
        build_pannel_grid(x1,y1,x2,y2)
    elif nume == Nume_pelle:
        (x1, y1) = pos_init
        (x2, y2) = pos_final
        destroy_grid(x1,y1,x2,y2)
    elif nume == Nume_route:
        (x1, y1) = pos_init
        (x2, y2) = pos_final
        Square_path(x1,y1,x2,y2)
    #elif(nume == Nume_well):
    #    if(pos_init == pos_final):
    #        (x,y) = pos_init
    #        Add_bat_game(x,y,m.name_id["Well"])


    # elif(nume == Nume_nourriture):
    # elif(event == Nume_prefecure):



    print("")


# a garder
# init_game()

#

# partie test

# print(Add_bat_game(2, 0, 5))
# m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
# print("***  modification en cours ****")
# m.add_bat(0,0,0,m.Mat_batiment)
# m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
# print("***  test de sauvegarde ****")

# sauvegarde("sauv1")
# m.add_bat(1,0,0,m.Mat_batiment)
# m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
# print("**** test du load ****")

# load("sauv1")
# m.afficher_matrice_bat(m.Mat_batiment, 3, 3)

#print("Harvest:", m.Mat_batiment[6][0].ind_Harv)


# test logique:
#m.afficher_matrice_bat(m.Mat_batiment, 12, 12)
#m.afficher_matrice_perso(m.Mat_perso, 7, 7)
#print("ZEHAHAHAHAHAHAHAH")

#test_bat_logique()
#test_walker_logique()
#print("Harvest:", m.Mat_batiment[6][0].ind_Harv)

#m.afficher_matrice_bat(m.Mat_batiment, 7, 7)
#m.afficher_matrice_perso(m.Mat_perso, 7, 7)
#print("HAHHAHAHAHAHHA")

#test_bat_logique()
#test_bat_logique()
#test_bat_logique()
#print("Harvest:", m.Mat_batiment[6][0].ind_Harv)

#test_bat_logique()
#test_bat_logique()

#print("Harvest:", m.Mat_batiment[6][0].ind_Harv)

#m.afficher_matrice_bat(m.Mat_batiment, 7, 7)
#m.afficher_matrice_perso(m.Mat_perso, 7, 7)
#m.deplacement_perso(m.Mat_perso)
#m.deplacement_perso(m.Mat_perso)
#m.deplacement_perso(m.Mat_perso)
#print("Après")
#m.afficher_matrice_perso(m.Mat_perso, 7, 7)

# print(m.Mat_perso[5][1][0].cargaison_nourriture)
# print(m.Mat_batiment[6][0].Walk)
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)
# m.add_perso(1, 5, "Delivery Guy", m.Mat_perso, m.Mat_batiment[6][0], m.Mat_batiment[6][0], 'ble', 1, 5)
# m.add_perso(1, 5, "Delivery Guy", m.Mat_perso, m.Mat_batiment[6][0], m.Mat_batiment[6][0], 'ble', 1, 5)
# m.add_perso(1, 5, "Delivery Guy", m.Mat_perso, m.Mat_batiment[6][0], m.Mat_batiment[6][0], 'ble', 1, 5)
# m.add_perso(1, 5, "Delivery Guy", m.Mat_perso, m.Mat_batiment[6][0], m.Mat_batiment[6][0], 'ble', 1, 5)
# m.add_perso(1, 5, "Delivery Guy", m.Mat_perso, m.Mat_batiment[6][0], m.Mat_batiment[6][0], 'ble', 1, 5)
# print(" ")
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)
# m.kill_walker(m.Mat_perso[5][1][0])
# #m.destroy_Bat(m.Mat_batiment[6][0])
# print("")
# print(m.Mat_batiment[6][0].Walk)
# m.afficher_matrice_perso(m.Mat_perso, 6, 6)
# print("test teet")
# #print(m.Mat_perso[5][1][0].cargaison_nourriture) # erreur normale