import pickle
import testuwu.test
from Terminus_project.Model import matrice as m


def Delivery(Bat, type_march, quant, Mat):
    (x, y) = m.SearchforRoad(Bat.pos_x, Bat.pos_y, Mat)
    if (x != -1):
        m.add_perso(x, y, 'Delivery Guy', Mat, Bat)


def getID(i, j):
    if (m.Mat_batiment[i][j].pos_x == i and m.Mat_batiment[i][j].pos_y == j):
        return m.Mat_batiment[i][j].id
    else:
        return 666


def init_game():
    m.departureMatrice(m.Mat_batiment)


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


def sauvegarde(nom):
    sauv = State()
    with open(nom, "wb") as f:
        pickle.dump(sauv, f)


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