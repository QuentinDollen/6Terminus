# Warning be on terminus's project folder
# Import needed libraries 

from os import getcwd
import pygame as pg
from pygame.locals import * 
import sys

pg.init()

# Define global variables :

screen = pg.display.set_mode(  (0 , 0 ) , pg.FULLSCREEN)
window_width = screen.get_size()[0]
winddow_height = screen.get_size()[1]
timer = pg.time.Clock()
Textefont = pg.font.Font( f"{getcwd()}\C3_policy.TTF" , 36 )
running = True
event = None
print(event)
# Define buttons path image :

Path_home_page = "/View/Sprites/Home_page/"
Path_HP_back = f"{getcwd()}{Path_home_page}HP_background.PNG"
Path_HP_exit = f"{getcwd()}{Path_home_page}HP_exit.PNG"
Path_HP_new_carrer = f"{getcwd()}{Path_home_page}HP_new_carrer.PNG"
Path_HP_load_game = f"{getcwd()}{Path_home_page}HP_load_game.PNG"

# Define buttons position :

Pos_HP_exit = ( window_width / 2 , 7 * winddow_height / 10 )
Pos_HP_new_carrer = ( window_width /2 , 5 * winddow_height / 10 )
Pos_HP_load_game = ( window_width /2 , 6 * winddow_height / 10)

# Define all buttons events :

go_to_home_page = pg.event.Event ( pg.USEREVENT )
go_to_game_page = pg.event.Event ( pg.USEREVENT + 1 )
exit_game = pg.event.Event ( pg.USEREVENT + 2 )
save_game = pg.event.Event ( pg.USEREVENT + 3 )
pause_game = pg.event.Event ( pg.USEREVENT + 4 )
start_game = pg.event.Event ( pg.USEREVENT + 5 )
go_to_save_repositori = pg.event.Event ( pg.USEREVENT + 6 )
go_to_new_carrer = pg.event.Event ( pg.USEREVENT + 7 )

# Define button class :

class Button :

    # Initialisation of Button object :

    def __init__( self , pos , path_image  , action ) :
        self.__image = pg.image.load( path_image )
        self.__path_image = path_image
        self.__left = pos[0]
        self.__up = pos[1] 
        self.__width = self.__image.get_size()[0] 
        self.__height = self.__image.get_size()[1] 
        self.__text = "Ceci est un texte"
        self.__enable = True
        self.__action = action
        self.__centred = False
      

    # Define geters

    def get_image(self) : return self.__image
    def get_left(self) : return self.__left
    def get_up(self) : return self.__up
    def get_width(self) : return self.__image.get_size()[0]
    def get_height(self) : return self.__image.get_size()[1]
    def get_enable(self) : return self.__enable
    def get_path_image(self) : return self.__path_image

    # Define seters 

    def set_enable(self) : self.__enable = True
    def set_disable(self) : self.__enable = False
    def set_height(self , new_height) : self.__height = new_height
    def set_width(self , new_width) : self.__width = new_width
    def set_image( self ) : self.__image = pg.transform.scale( self.__image , ( self.get_width() , self.get_height()) )
    def set_left( self , new_left) : self.__left = new_left
    def set_up( self , new_up ) : self.__up = new_up


    # Define Button's methods

        # Tell if the mouse is over the button object

    def overhead ( self , pos ) :
        if  self.get_enable() :
            if  self.get_left() <= pos[0] <= self.get_left()  + self.get_width() and self.get_up()  <= pos[1] <= self.get_up() + self.get_height() :

                temp_image = self.get_image()            
                screen.blit(pg.Surface( (self.get_width(),self.get_height() ) , pg.Color("Black")) , (self.get_left() , self.get_up()) )
                pg.Surface.set_alpha(temp_image , 60)
                screen.blit(temp_image  ,(self.get_left() , self.get_up()))
                pg.display.update()
                return True

            else :
                self.draw_image_center()
                
        return False

        # Tell if the mouse click on the button object

    def touched ( self , pos ) : 
        if self.get_enable() and self.overhead( pos ) : 
            pg.event.post( self.__action )
            return True
        

        # Draw form the center of Image on the screen :

    def draw_image_center( self ) : 
        if not self.__centred :
            center = ( self.get_left() - self.get_width()/2 , self.get_up() - self.get_height()/2 )

            if ( self.get_enable()) :
                screen.blit( self.get_image() , center )
         
            self.set_left( center [ 0 ] )
            self.set_up( center [ 1 ] )
            self.__centred = True
            
        else :
            screen.blit( self.get_image() , ( self.__left , self.__up ) )

        # Draw the image on the screen :

    def draw_image( self ) : 

        if ( self.get_enable()) :
         screen.blit( self.get_image() , ( self.get_left() , self.get_height() )  )

         # Resize the button following the screen's dimension :

    def resize( self , dimension ) :
        new_height = self.get_height() * dimension[0] / 1920
        self.set_height(new_height)
        new_width = self.get_width() * dimension[1] / 1080
        self.set_width(new_width)
        self.set_image()




# Define all buttons of the game :

    # Home page ones :

HP_back = Button( ( window_width/2 , winddow_height/2 ) , Path_HP_back , None)
HP_back.resize( ( window_width , winddow_height ) )
HP_back.draw_image_center()
HP_back.set_disable()

HP_exit = Button( Pos_HP_exit , Path_HP_exit , exit_game)
HP_exit.resize( ( window_width , winddow_height ) )
HP_exit.draw_image_center()

HP_newc = Button( Pos_HP_new_carrer , Path_HP_new_carrer , go_to_new_carrer)
HP_newc.resize( ( window_width , winddow_height ) )
HP_newc.draw_image_center()

HP_load_game = Button ( Pos_HP_load_game , Path_HP_load_game , go_to_save_repositori)
HP_load_game.resize( ( window_width , winddow_height ) )
HP_load_game.draw_image_center()


# HP_next = Button( )

# Test game 

while running :

    timer.tick(60)
    mouse_pos = pg.mouse.get_pos()

    TEXTE = Textefont.render("Hellaazertyoppmlkjjhggdqwo Wolrd : ", True , ( 100 , 100 , 100 ))
    screen.blit(TEXTE , ( 100 , 100 ))

    for event in pg.event.get() :

        if event.type == pg.QUIT :
            running = False
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEMOTION :
            HP_exit.overhead( mouse_pos )
            HP_load_game.overhead( mouse_pos )
            HP_newc.overhead( mouse_pos )

        if event.type == pg.MOUSEBUTTONDOWN :

            if HP_exit.touched( mouse_pos ) : 
                running = False 
                pg.quit()
                sys.exit()

  
    
    pg.display.update() 

# mémory 

    # for event in pg.event.get() :

    #     if event.type == pg.QUIT :
    #         running = False
    #         pg.quit()
    #         sys.exit()

    #     if event.type == pg.MOUSEMOTION :
    #         HP_exit.overhead( mouse_pos )
    #         HP_load_game.overhead( mouse_pos )
    #         HP_newc.overhead( mouse_pos )

    #     if event.type == pg.MOUSEBUTTONDOWN :

    #         if HP_exit.touched( mouse_pos ) : 
    #             running = False 
    #             pg.quit()
    #             sys.exit()