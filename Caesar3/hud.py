import pygame as pg

class Hud:

     def __init__(self, width, height):

        self.width = width
        self.height = height

        # menu hud
        self.menu1 = pg.image.load("Graphique/paneling_00088.png")
        self.menu2 = pg.image.load("Graphique/paneling_00018.png")
        self.menu3 = pg.image.load("Graphique/paneling_00485.png")
        self.menu4 = pg.image.load("Graphique/paneling_00527.png")
        self.menu5 = pg.image.load("Graphique/paneling_00479.png")
        self.menu6 = pg.image.load("Graphique/paneling_00521.png")

        self.menu7 = pg.image.load("Graphique/paneling_00492.png")
        self.menu8 = pg.image.load("Graphique/paneling_00486.png")
        self.menu9 = pg.image.load("Graphique/paneling_00526.png")
        self.menu10 = pg.image.load("Graphique/paneling_00480.png")
        self.menu11 = pg.image.load("Graphique/paneling_00519.png")


     def draw(self, screen):

         screen.blit(self.menu1, (1374, 24))
         screen.blit(self.menu2, (1374, 698))

         #corner
         screen.blit(self.menu3, (1520, 474))
         screen.blit(self.menu4, (1520, 682))
         screen.blit(self.menu5, (1376, 474))
         screen.blit(self.menu6, (1376, 682))

         for a in range(12):
             screen.blit(self.menu7, (1520, 490 + 16 * a))
             screen.blit(self.menu8, (1376, 490 + 16 * a))
         for b in range(8):
            screen.blit(self.menu9, (1392 + 16 * b, 682))
            screen.blit(self.menu10, (1392 + 16 * b, 474))
         for c in range(8):
             for d in range(12):
                screen.blit(self.menu11, (1392 + 16 * c, 490 + 16 * d))
