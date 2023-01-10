import pygame as pg

class Hud:

     def __init__(self, width, height):

        self.width = width
        self.height = height

        # menu hud
        self.menu1 = pg.image.load("Graphique/paneling_00017.png")
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

         screen.blit(self.menu1, (pg.display.Info().current_w - 162, pg.display.Info().current_h - 840))
         screen.blit(self.menu2, (pg.display.Info().current_w - 162, pg.display.Info().current_h - 166))

         #corner
         screen.blit(self.menu3, (pg.display.Info().current_w - 16, pg.display.Info().current_h - 390))
         screen.blit(self.menu4, (pg.display.Info().current_w - 16, pg.display.Info().current_h - 182))
         screen.blit(self.menu5, (pg.display.Info().current_w - 160, pg.display.Info().current_h - 390))
         screen.blit(self.menu6, (pg.display.Info().current_w - 160, pg.display.Info().current_h - 182))

         for a in range(12):
             screen.blit(self.menu7, (pg.display.Info().current_w - 16, pg.display.Info().current_h - 374 + 16 * a))
             screen.blit(self.menu8, (pg.display.Info().current_w - 160, pg.display.Info().current_h - 374 + 16 * a))
         for b in range(8):
            screen.blit(self.menu9, (pg.display.Info().current_w - 144 + 16 * b, pg.display.Info().current_h - 182))
            screen.blit(self.menu10, (pg.display.Info().current_w - 144 + 16 * b, pg.display.Info().current_h - 390))
         for c in range(8):
             for d in range(12):
                screen.blit(self.menu11, (pg.display.Info().current_w - 144 + 16 * c, pg.display.Info().current_h - 374 + 16 * d))


     #
     #    # read images
     #    panel1 = pg.image.load("Graphique/paneling_00010.png")
     #    panel2 = pg.image.load("Graphique/paneling_00015.png")
     #    panel3 = pg.image.load("Graphique/paneling_00017.png")
     #
     #    images = {
     #        "panel1": panel1,
     #        "panel2": panel2,
     #        "panel3": panel3
     #    }
     #
     #    return images
