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
        cible = m.SearchforSpace()
        if(cible == None):
            return -1
        dg = m.add_perso(x, y, 'Delivery Guy', m.Mat_perso, Bat_depart, cible)
        dg.ajout_marchandise(type_march,quant)
        # Bat dest devra être calculé : grenier, entrepot, marché
        (cx,cy) = cible.ret_coord()
        print("cible",cx,cy)
        (dx, dy) = m.SearchforRoad( cx, cy, m.Mat_batiment)
        dg.dest_x = dx
        dg.dest_y = dy
        print(dx,dy)


# renvoie l'ID d'un batiment placé sur une case de la matrice des batiments, dont les coordonées sont données en argument
# Pour un batiment de plusieurs cases, ne donne l'id que si la case est celle en haut, autrement renvoie 666
def getID(i, j):
    if (m.Mat_batiment[i][j].pos_x == i and m.Mat_batiment[i][j].pos_y == j):
        return m.Mat_batiment[i][j].id
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
            if m.Mat_batiment[x + i][y + j].name != "Herb":
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

Delivery(m.Mat_batiment[0][6],'ble',11)

m.afficher_matrice_bat(m.Mat_batiment, 9, 9)
m.afficher_matrice_perso(m.Mat_perso, 6, 6)
m.deplacement_perso(m.Mat_perso)
m.afficher_matrice_perso(m.Mat_perso, 6, 6)

