class Terrain():
    def __init__(self,x,y,id_t):
        self.taille_case = 1
        self.pos_x = x  # position x sur la map
        self.pos_y = y  # position y sur la map
        self.name = 'Terrain vide'
        self.id = id_t # id du terrain
        self.main = 0  # Condition imposée pour l'affichage de batiment à taille n*n: le coin en haut vaut 1 et les autres 0

