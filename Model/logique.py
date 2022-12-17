import pickle
import testuwu.test
import os.path
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
        dg = m.add_perso(x, y, 'Delivery Guy', m.Mat_perso, Bat_depart)
        dg.ajout_marchandise(type_march,quant)
        # Bat dest devra être calculé : grenier, entrepot, marché
        #dg.dest_x = Bat_dest.pos_x
        #dg.dest_y = Bat_dest.pos_y

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


init_game()
print(Add_bat_game(2, 0, 5))
m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
print("***  modification en cours ****")
m.add_bat(0,0,0,m.Mat_batiment)
m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
print("***  test de sauvegarde ****")

sauvegarde("sauv1")
m.add_bat(1,0,0,m.Mat_batiment)
m.afficher_matrice_bat(m.Mat_batiment, 3, 3)
print("***  test du load ****")

load("sauv1")
m.afficher_matrice_bat(m.Mat_batiment, 3, 3)