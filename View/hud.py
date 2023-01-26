import pygame as pg
import sys

sys.path.insert(0, '..')
from Model.logique import *

action = None


class button_hud():

    def __init__(self, path, path_over, path_clicked, pos, size_button, event_number):
        self.__transparent = False
        self.__image = pg.image.load(path)
        self.__image_over = pg.image.load(path_over)
        self.__image_cliked = pg.image.load(path_clicked)
        self.__image = pg.transform.scale(self.__image, size_button)
        self.__image_over = pg.transform.scale(self.__image_over, size_button)
        self.__image_cliked = pg.transform.scale(self.__image_cliked, size_button)
        self.__left = pos[0] - self.__image.get_width() / 2
        self.__up = pos[1] - self.__image.get_height() / 2
        self.__pos = (self.__left, self.__up)
        self.__clicked = False
        self.__event = event_number

    def is_clicked(self):
        return self.__clicked

    def get_width(self):
        return self.__image.get_width()

    def get_height(self):
        return self.__image.get_height()

    def get_up(self):
        return self.__up

    def get_left(self):
        return self.__left

    def get_image(self):
        return self.__image

    def get_image_over(self):
        return self.__image_over

    def get_image_clicked(self):
        return self.__image_cliked

    def get_pos(self):
        return self.__pos

    def transparenci(self, pos, screen):

        if self.overhead(pos, screen):
            if not self.__transparent:
                self.__transparent = True
                white_rect = pg.Surface((self.get_width(), self.get_height()))
                white_rect.fill((255, 255, 255))
                white_rect.set_alpha(100)
                screen.blit(white_rect, (self.get_left(), self.get_up()))
        else:
            self.__transparent = False
            screen.blit(self.get_image(), (self.get_left(), self.get_up()))

    def overhead(self, pos):
        return self.get_left() <= pos[0] <= self.get_left() + self.get_width() and self.get_up() <= pos[
            1] <= self.get_up() + self.get_height()

    def draw(self, screen):

        if self.__clicked:
            screen.blit(self.get_image_clicked(), self.get_pos())
        else:
            if self.overhead(pg.mouse.get_pos()):
                screen.blit(self.get_image_over(), self.get_pos())
            else:
                screen.blit(self.get_image(), self.get_pos())

    def set_cliked(self):
        self.__clicked = self.overhead(pg.mouse.get_pos())
        if self.__clicked:
            pg.event.post(pg.event.Event(self.__event))
            global action
            action = self.__event
            return self.__event


class Hud:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.current_action = None

        # menu hud
        self.menu1 = pg.image.load("View/Graphique/paneling_00017.png")
        self.menu2 = pg.image.load("View/Graphique/paneling_00018.png")
        self.menu3 = pg.image.load("View/Graphique/paneling_00485.png")
        self.menu4 = pg.image.load("View/Graphique/paneling_00527.png")
        self.menu5 = pg.image.load("View/Graphique/paneling_00479.png")
        self.menu6 = pg.image.load("View/Graphique/paneling_00521.png")

        self.menu7 = pg.image.load("View/Graphique/paneling_00492.png")
        self.menu8 = pg.image.load("View/Graphique/paneling_00486.png")
        self.menu9 = pg.image.load("View/Graphique/paneling_00526.png")
        self.menu10 = pg.image.load("View/Graphique/paneling_00480.png")
        self.menu11 = pg.image.load("View/Graphique/paneling_00519.png")

        # Menu bandeau

        self.bandeau = pg.image.load("View/Graphique/Paneling_bandeau.PNG")
        self.value = pg.image.load("View/Graphique/paneling_00015.PNG")
        self.bandeau_size = self.bandeau.get_size()

        self.dim = self.menu1.get_size()
        self.pos = (width - self.dim[0], 0)

        size_button = (9.4 / 36 * self.dim[0], 6.5 / 95 * self.dim[1])

        # Buttons :

        U1 = self.pos[1] + 55 / 95 * self.dim[1] + self.bandeau_size[1]
        U2 = self.pos[1] + 63 / 95 * self.dim[1] + self.bandeau_size[1]
        U3 = self.pos[1] + 70 / 95 * self.dim[1] + self.bandeau_size[1]
        U4 = self.pos[1] + 78 / 95 * self.dim[1] + self.bandeau_size[1]
        U5 = self.pos[1] + 85 / 95 * self.dim[1] + self.bandeau_size[1]
        L1 = self.pos[0] + 6.9 / 32 * self.dim[0]
        L2 = self.pos[0] + 16 / 32 * self.dim[0]
        L3 = self.pos[0] + 26 / 32 * self.dim[0]

        self.maison = button_hud("View/Graphique/paneling_00123.png", "View/Graphique/paneling_00124.png",
                                 "View/Graphique/paneling_00125.png", (L1, U1), size_button, Nume_maison)
        self.eau = button_hud("View/Graphique/paneling_00127.png", "View/Graphique/paneling_00128.png",
                              "View/Graphique/paneling_00129.png", (L1, U2), size_button, Nume_eau)
        self.prefecture = button_hud("View/Graphique/paneling_00159.png", "View/Graphique/paneling_00160.png",
                                     "View/Graphique/paneling_00161.png", (L2, U4), size_button, Nume_prefecure)
        self.nourriture = button_hud("View/Graphique/paneling_00155.png", "View/Graphique/paneling_00156.png",
                                     "View/Graphique/paneling_00157.png", (L3, U4), size_button, Nume_nourriture)
        self.ingenieur = button_hud("View/Graphique/paneling_00167.png", "View/Graphique/paneling_00168.png",
                                    "View/Graphique/paneling_00169.png", (L1, U4), size_button, Nume_ingenieur)
        self.santé = button_hud("View/Graphique/paneling_00163.png", "View/Graphique/paneling_00164.png",
                                "View/Graphique/paneling_00165.png", (L2, U2), size_button, Nume_sante)
        self.route = button_hud("View/Graphique/paneling_00135.png", "View/Graphique/paneling_00136.png",
                                "View/Graphique/paneling_00137.png", (L3, U1), size_button, Nume_route)
        self.administratif = button_hud("View/Graphique/paneling_00139.png", "View/Graphique/paneling_00140.png",
                                        "View/Graphique/paneling_00141.png", (L3, U3), size_button, Nume_administratif)
        self.theatre = button_hud("View/Graphique/paneling_00143.png", "View/Graphique/paneling_00144.png",
                                  "View/Graphique/paneling_00145.png", (L2, U3), size_button, Nume_theatre)
        self.pelle = button_hud("View/Graphique/paneling_00131.png", "View/Graphique/paneling_00132.png",
                                "View/Graphique/paneling_00133.png", (L2, U1), size_button, Nume_pelle)

    def draw(self, screen):
        # screen.blit(self.menu1, (pg.display.Info().current_w - 162, pg.display.Info().current_h - 840))
        screen.blit(self.menu1, self.pos)
        screen.blit(self.bandeau, (0, 0))

        # Placer le bandeau

        coef = self.bandeau_size[1] / self.value.get_size()[1]
        for i in range(self.width // self.bandeau_size[0] + 1):
            screen.blit(self.bandeau, (i * (self.bandeau_size[0]), 0))

        self.value = pg.transform.scale(self.value, (self.value.get_size()[0] * coef, self.value.get_size()[1] * coef))
        screen.blit(self.value, (self.width / 4, 0))
        screen.blit(self.value, (self.width / 2, 0))

        # screen.blit(self.menu2, (pg.display.Info().current_w - 162, pg.display.Info().current_h - 166))

        # corner
        # screen.blit(self.menu3, (pg.display.Info().current_w - 16, pg.display.Info().current_h - 390))
        # screen.blit(self.menu4, (pg.display.Info().current_w - 16, pg.display.Info().current_h - 182))
        # screen.blit(self.menu5, (pg.display.Info().current_w - 160, pg.display.Info().current_h - 390))
        # screen.blit(self.menu6, (pg.display.Info().current_w - 160, pg.display.Info().current_h - 182))

        # for a in range(12):
        #     screen.blit(self.menu7, (pg.display.Info().current_w - 16, pg.display.Info().current_h - 374 + 16 * a))
        #     screen.blit(self.menu8, (pg.display.Info().current_w - 160, pg.display.Info().current_h - 374 + 16 * a))
        # for b in range(8):
        #    screen.blit(self.menu9, (pg.display.Info().current_w - 144 + 16 * b, pg.display.Info().current_h - 182))
        #    screen.blit(self.menu10, (pg.display.Info().current_w - 144 + 16 * b, pg.display.Info().current_h - 390))
        # for c in range(8):
        #     for d in range(12):
        #        screen.blit(self.menu11, (pg.display.Info().current_w - 144 + 16 * c, pg.display.Info().current_h - 374 + 16 * d))

        self.maison.draw(screen)
        self.eau.draw(screen)
        self.prefecture.draw(screen)
        self.nourriture.draw(screen)
        self.route.draw(screen)
        self.theatre.draw(screen)
        self.administratif.draw(screen)
        self.pelle.draw(screen)
        self.ingenieur.draw(screen)
        self.santé.draw(screen)

    def overhead_all(self):
        self.maison.set_cliked()
        self.eau.set_cliked()
        self.prefecture.set_cliked()
        self.nourriture.set_cliked()
        self.route.set_cliked()
        self.theatre.set_cliked()
        self.administratif.set_cliked()
        self.pelle.set_cliked()
        self.ingenieur.set_cliked()
        self.santé.set_cliked()
        global action
        return action

    def is_overhead_all(self):
        pos = pg.mouse.get_pos()
        return self.maison.overhead(pos) or self.eau.overhead(pos) or self.prefecture.overhead(
            pos) or self.nourriture.overhead(pos) or self.route.overhead(pos) \
               or self.theatre.overhead(pos) or self.administratif.overhead(pos) or self.pelle.overhead(
            pos) or self.ingenieur.overhead(pos) or self.santé.overhead(pos)

    #
    #    # read images
    #    panel1 = pg.image.load("View/Graphique/paneling_00010.png")
    #    panel2 = pg.image.load("View/Graphique/paneling_00015.png")
    #    panel3 = pg.image.load("View/Graphique/paneling_00017.png")
    #
    #    images = {
    #        "panel1": panel1,
    #        "panel2": panel2,
    #        "panel3": panel3
    #    }
    #
    #    return images