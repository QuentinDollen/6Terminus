import sys

sys.path.insert(0, '..')
import pygame as pg
import sys
from View.map import Map
from View.settings import *
# from utils import draw_text
from View.camera import Camera
from View.hud import Hud
from Model import logique as l 


list_event = { l.Nume_administratif , l.Nume_eau , l.Nume_ingenieur , l.Nume_maison , l.Nume_nourriture , l.Nume_pelle , l.Nume_prefecure , l.Nume_route , l.Nume_sante , l.Nume_theatre}

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        # map
        self.map = Map(40, 40, self.width, self.height)

        # camera
        self.camera = Camera(self.width, self.height)

        # hud
        self.hud = Hud(self.width, self.height)

        overlay = ""
        self.selection = list()
        self.selection.append([])
        self.selection.append([])
        self.actionned = None 
        


    def run(self):
        self.playing = True
        
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()



    def events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            

            if event.type == pg.MOUSEBUTTONDOWN : 
                (x_,y_) = self.mouse_to_tiles()
                print("Ajout route : (",x_,y_,")")
                l.Add_bat_game(x_,y_,l.m.name_id["Path"])
                l.m.afficher_matrice_bat(l.m.Mat_batiment , 10 , 10 )




    def update(self):
        
        self.camera.update()
        self.map.create_map()
        self.draw()

    def draw(self):
        self.screen.fill(BLACK)

        self.map.draw(self.screen, self.camera)
        self.hud.draw(self.screen)
        self.map.draw_mini(self.screen, self.camera)

        # p = self.map.map[x][y]["iso_poly"]
        # p = [(x + self.width/2, y) for x, y in p]
        # pg.draw.polygon(self.screen, (0, 0, 0), p, 1)

        

        # draw_text(
        #     self.screen,
        #     'fps={}'.format(round(self.clock.get_fps())),
        #     25,
        #     (255, 255, 255),
        #     (10, 10)
        # )

        pg.display.flip()

    def mouse_to_tiles(self) :
        mouse = pg.mouse.get_pos()

        on_grid_x = -self.camera.scroll.x + mouse[0] -self.map.grass_tiles.get_width()/2
        on_grid_y = - self.camera.scroll.y + mouse[1]

        iso_y = ( 2 * on_grid_y - on_grid_x)/2
        iso_x =  iso_y + on_grid_x

        grid_x = int ( iso_x // TILE_SIZE)
        grid_y = int( iso_y // TILE_SIZE)

        if grid_x < 0 : 
            grid_x = 0 
        if grid_x > 39 : 
            grid_x = 39
        
        if grid_y < 0 : 
            grid_y = 0 
        if grid_y > 39 : 
            grid_y = 39

        return (grid_x , grid_y)


    
            