# Warning be on terminus's project folder
# Import needed libraries 

from os import getcwd
import pygame as pg
import sys

# Define global variables :

screen = pg.display.set_mode( (0,0) , pg.FULLSCREEN )
window_width = pg.FULLSCREEN[0]
winddow_height = pg.FULLSCREEN[1]
timer = pg.time.Clock()
pg.font.Font("CWFARKAGE.TTF")
running = True

# Define buttons path image :

path_home_page = "/Version_MVC/View/Sprites/Home_page/"
Path_HP_background = f"{getcwd()}{path_home_page}HP_background.PNG"
Path_HP_exit = f"{getcwd()}{path_home_page}HP_exit.PNG"
Path_HP_new_carrer = f"{getcwd()}{path_home_page}HP_new_carrer.PNG"
Path_HP_load_game = f"{getcwd()}{path_home_page}HP_load_game.PNG"

# Define button class :

class Button :

    # Initialisation of Button object :

    def __init__( self , pos , path_image ) :
        self.__image = pg.image.load( path_image ).convert_alpha()
        self.__path_image = path_image
        self.__left = pos[0]
        self.__up = pos[1] 
        self.__width = self.__image.get_size()[0] 
        self.__height = self.__image.get_size()[1] 
        self.__text = "Ceci est un texte"
        self.__enable = True
      

    # Define geters

    def get_image(self) : return self.__image
    def get_left(self) : return self.__left
    def get_up(self) : return self.__up
    def get_width(self) : return self.__image.get_size()[0]
    def get_height(self) : return self.__image.get_size()[1]
    def get_enable(self) : return self.__enable
    def get_path_image(self) : return self.__path_image

    # Define seters 

    def set_enable(self) : self.enable = True
    def set_disable(self) : self.enable = False
    def set_height(self , new_height) : self.__height = new_height
    def set_width(self , new_width) : self.__width = new_width
    def set_image( self ) : self.__image = pg.image.load( self.__path_image , ( self.__width , self.__height) )


    # Define Button's methods

        # Tell if the mouse is over the button object

    def overhead ( self , pos ) :
        if   self.get_enable()  and self.get_left() <= pos[0] <= self.get_left()  + self.get_width() and self.get_up()  <= pos[1] <= self.get_up() + self.get_height() :
            temp_image = self.get_image()            
            screen.blit(pg.Surface( (self.get_width(),self.get_height() ) , pg.Color("Black")) , (self.get_left() , self.get_up()) )
            pg.Surface.set_alpha(temp_image , 60)
            screen.blit(temp_image  ,(self.get_left() , self.get_up()))
            return True
        else :
            self.draw_image()
            return False

        # Tell if the mouse click on the button object

    def touched ( self , pos ) : return self.get_enable() and event.type == pg.MOUSEBUTTONUP and self.overhead( pos )

        # Draw the Image on the screen :

    def draw_image ( self ) : 
        if ( self.get_enable()) :
         screen.blit( self.get_image() , ( self.get_left() , self.get_up() ) )

         # Resize the button following the screen's dimension :

    def resize( self , dimension ) :
        new_height = self.get_height() * dimension[0] / 1920
        self.set_height(new_height)
        new_width = self.get_width() * dimension[1] / 1080
        self.set_width(new_width)
        self.set_image()



# Define all buttons of the game :

    # Home page ones :

HP_back = Button( ( 0 , 0 ) , path_home_page)
HP_back.resize( ( winddow_height , window_width ) )



# Test game 

while running :

    timer.tick(60)
    pos = pg.mouse.get_pos()

    for event in pg.event.get() :
        if event.type == pg.QUIT :
            running = False
            pg.quit()
            sys.exit()
    
    pg.display.update() 