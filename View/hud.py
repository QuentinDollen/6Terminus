
import pygame as pg
class button_hud():

   def __init__(self , path , path_over,  pos ) :
      self.__transparent = False
      self.__image = pg.image.load(path)
      self.__image_over = pg.image.load(path_over)
      self.__left = pos[0] - self.__image.get_width() /2 
      self.__up = pos[1] - self.__image.get_height()/2
      self.__pos = (self.__left, self.__up)


   def get_width(self) : return self.__image.get_width()
   def get_height(self) : return self.__image.get_height()
   def get_up(self) : return self.__up
   def get_left(self) : return self.__left
   def get_image(self) : return self.__image
   def get_image_over(self) : return self.__image_over
   def get_pos(self) : return self.__pos

   def transparenci( self , pos , screen ) :
        
      if self.overhead(pos , screen ) :
            if not self.__transparent :
               self.__transparent = True
               white_rect = pg.Surface( (self.get_width(), self.get_height()) ) 
               white_rect.fill((255,255,255)) 
               white_rect.set_alpha(100)
               screen.blit(white_rect , (self.get_left(),self.get_up()) )
      else :
            self.__transparent = False
            screen.blit(self.get_image() , (self.get_left(),self.get_up()) )

   def overhead( self , pos ): return  self.get_left() <= pos[0] <= self.get_left()  + self.get_width() and self.get_up()  <= pos[1] <= self.get_up() + self.get_height()

   def draw( self ,screen ) : 
      if self.overhead(pg.mouse.get_pos()) :
         screen.blit( self.get_image_over() , self.get_pos())
      else : 
         screen.blit( self.get_image() , self.get_pos())
class Hud:

     def __init__(self, width, height):

        self.width = width
        self.height = height

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
        
        # Buttons :
        self.maison = button_hud("View/Graphique/paneling_00123.png","View/Graphique/paneling_00124.png", (200 , 300) )
        self.eau = button_hud("View/Graphique/paneling_00127.png","View/Graphique/paneling_00128.png", (200 , 400) )
        self.prefecture = button_hud("View/Graphique/paneling_00159.png","View/Graphique/paneling_00160.png", (200 , 500) )
        self.nourriture = button_hud("View/Graphique/paneling_00155.png","View/Graphique/paneling_00156.png", (200 , 600) )
        self.ingenieur = button_hud("View/Graphique/paneling_00167.png","View/Graphique/paneling_00168.png", (200 , 700) )
        self.santé = button_hud("View/Graphique/paneling_00163.png","View/Graphique/paneling_00164.png", (200 , 800) )
        self.route = button_hud("View/Graphique/paneling_00135.png","View/Graphique/paneling_00136.png", (200 , 900) )
        self.administratif = button_hud("View/Graphique/paneling_00139.png","View/Graphique/paneling_00140.png", (200 , 1000) )
        self.theatre = button_hud("View/Graphique/paneling_00143.png","View/Graphique/paneling_00144.png", (400 , 200) )
        

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