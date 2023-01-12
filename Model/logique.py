import pickle
import sys

sys.path.insert(0, '..')

from Model import matrice as m

# En jeu (dans le main), on n'utilisera que les fonctions de logique.py, celles présente dans les autres fichiers servent de briques pour celles présentes ici


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
        print("MUDA MUDA")
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

def getWalker(i,j):
    if(m.Mat_perso[j][i][0].name != 'no Walker'):
        return m.Mat_perso[j][i]



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
                    if(m.Mat_perso[j][i][k].name == "Prefect"):
                        proxy = m.get_bat_prox(i,j,2)
                        print("proxy", proxy)
                        for bat in proxy:
                            bat.ind_fire = 0
                    if(m.Mat_perso[j][i][k].name == "Engineer"):
                        proxy = m.get_bat_prox(i,j,2)
                        print("proxy", proxy)
                        for bat in proxy:
                            bat.ind_eff = 0
                    if(m.Mat_perso[j][i][k].name == "Priest"):
                        proxy = m.get_bat_prox(i,j,4)
                        print("proxy", proxy)
                        for bat in proxy:
                            if(m.InTable(bat.name, ["Maison 1", "Maison 2", "Maison 3", "Maison 4"])):
                                bat.faith = bat.faith + 40



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
            if(bat.hasCheck == 0):
                bat.hasCheck = 1
                if bat.name == "Farm":
                    bat.growFood()
                    if(bat.ind_Harv >= 6):
                        print("time for delivery")
                        Delivery(bat, 'ble', bat.ind_Harv*2)
                        bat.ind_Harv = 0
                if(bat.name == "Prefecture"):
                    if(bat.Walk == []):
                        m.invoke_walker(bat,"Prefect")
                if(bat.name == "EngineersPost"):
                    if(bat.Walk == []):
                        m.invoke_walker(bat,"Engineer")
                if(bat.name == "Temple"):
                    if(bat.Walk == []):
                        m.invoke_walker(bat,"Priest")
    for i in range(m.nb_cases):
        for j in range(m.nb_cases):
            m.Mat_batiment[j][i].hasCheck = 0

# a garder
#init_game()

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
Add_bat_game(0,6,100)
Add_bat_game(1,5,5)
print("Harvest:",m.Mat_batiment[6][0].ind_Harv)

# test logique:
m.afficher_matrice_bat(m.Mat_batiment, 7, 7)
m.afficher_matrice_perso(m.Mat_perso, 7, 7)
print("ZEHAHAHAHAHAHAHAH")

test_bat_logique()
test_walker_logique()
print("Harvest:",m.Mat_batiment[6][0].ind_Harv)

m.afficher_matrice_bat(m.Mat_batiment, 7, 7)
m.afficher_matrice_perso(m.Mat_perso, 7, 7)
print("HAHHAHAHAHAHHA")

test_bat_logique()
test_bat_logique()
test_bat_logique()
test_bat_logique()
test_bat_logique()

print("Harvest:",m.Mat_batiment[6][0].ind_Harv)
m.deplacement_perso(m.Mat_perso)
m.afficher_matrice_bat(m.Mat_batiment, 7, 7)
m.afficher_matrice_perso(m.Mat_perso, 7, 7)
print(" ")
m.deplacement_perso(m.Mat_perso)
m.afficher_matrice_perso(m.Mat_perso, 7, 7)



