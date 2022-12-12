# Warning be on terminus's project folder
# Import needed libraries 

from os import getcwd
import pygame as pg
from pygame.locals import * 
import sys

pg.init()

# Define global variables :

screen = pg.display.set_mode( (0 , 0 ) , pg.FULLSCREEN)
window_width = screen.get_size()[0]
winddow_height = screen.get_size()[1]
timer = pg.time.Clock()
Paragraph = 16
Normal = 24
Big = 36
Path_font = f"{getcwd()}/C3_policy.TTF"
Textefont = pg.font.Font( Path_font , Big )
running = True

# Define buttons path image :

Path_home_page = "/View/Sprites/Home_page/"
Path_HP_back = f"{getcwd()}{Path_home_page}HP_background.PNG"
Path_HP_exit = f"{getcwd()}{Path_home_page}HP_exit.PNG"
Path_HP_new_carrer = f"{getcwd()}{Path_home_page}HP_new_carrer.PNG"
Path_HP_load_game = f"{getcwd()}{Path_home_page}HP_load_game.PNG"
Path_HP_support = f"{getcwd()}{Path_home_page}HP_support.PNG"
Path_HP_tittle = f"{getcwd()}{Path_home_page}HP_tittle.PNG"

Path_save_page = "/View/Sprites/Save_page/"
Path_SP_back = f"{getcwd()}{Path_save_page}SP_background.PNG"
Path_SP_validate = f"{getcwd()}{Path_save_page}SP_validate.PNG"
Path_SP_go_home = f"{getcwd()}{Path_save_page}SP_validate.PNG"
Path_SP_support = f"{getcwd()}{Path_save_page}SP_support.PNG"


# Define buttons position :

Pos_HP_back = ( window_width/2 , winddow_height/2 )
Pos_HP_exit = ( window_width / 2 , 7 * winddow_height / 10 )
Pos_HP_new_carrer = ( window_width /2 , 5 * winddow_height / 10 )
Pos_HP_load_game = ( window_width /2 , 6 * winddow_height / 10 )
Pos_HP_support = ( window_width /5 , 2 * winddow_height / 3 )
Pos_HP_tittle = ( window_width/2 , winddow_height/2 )

Pos_SP_back = ( window_width/2 , winddow_height/2 )
Pos_SP_validate = ( 4* window_width/10 , 3 * winddow_height/4 )
Pos_SP_go_home = ( 6*window_width/10 , 3*winddow_height/4  )
Pos_SP_support = (  window_width/2 , winddow_height/2  )

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

        if path_image :
            self.__image = pg.image.load( path_image )
            self.__width = self.__image.get_size()[0] 
            self.__height = self.__image.get_size()[1]  

        self.__path_image = path_image
        self.__left = pos[0]
        self.__up = pos[1] 
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
    def set_text( self , newtext ) : self.__text = newtext


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


    def set_size( self , dimension ) :
        self.set_width(dimension[0])
        self.set_height(dimension[1])
        self.__image = pg.transform.scale(self.__image , dimension)

 

class Texte_button(Button) :

    def __init__(self, pos, path_image, action , text = None ):
        super().__init__(pos, path_image, action)
        self.__text = text
        self.__color = ( 0 , 0 , 0 )
        self.__size = Textefont.size( self.get_text())

    def get_text(self) : return self.__text
    def get_color(self) : return self.__color

    def set_color(self , new_color) : self.__color = new_color

        # Reshape the text size following the screen size

        # Print the button's texte : 

    def print_texte(self) :
        if self.get_enable() and self.get_text() != None :
            TEXTE = Textefont.render(f"{self.get_text()}", True , self.get_color() )
            
            screen.blit(TEXTE , ( self.get_left() , self.get_up() ) )
            self.set_width(TEXTE.get_size()[0]) , self.set_height(TEXTE.get_size()[1]) 
            
            print (TEXTE.get_size())

    
    def overtext(self, pos):
        return self.get_enable() and self.get_left() <= pos[0] <= self.get_left()  + self.get_width() and self.get_up()  <= pos[1] <= self.get_up() + self.get_height() 
        

    def adapt_text_size( self ) :
        personnalfont = pg.font.Font(Path_font , self.get_height() * winddow_height / 1080)

    def add_char ( self , key ) :
        if self.get_enable() :
            self.__text += key 
        
        

        
         


# Define all buttons of the game :

    # Home page ones :

HP_back = Button( Pos_HP_back , Path_HP_back , None)
HP_back.resize( ( window_width , winddow_height ) )

HP_support = Button ( Pos_SP_support , Path_SP_support , None)
HP_support.set_size( ( ( window_width/3 , 2*winddow_height/3 ) ))

HP_exit = Button( Pos_HP_exit , Path_HP_exit , exit_game)
HP_exit.resize( ( window_width , winddow_height ) )

HP_newc = Button( Pos_HP_new_carrer , Path_HP_new_carrer , go_to_new_carrer)
HP_newc.resize( ( window_width , winddow_height ) )

HP_load_game = Button ( Pos_HP_load_game , Path_HP_load_game , go_to_save_repositori)
HP_load_game.resize( ( window_width , winddow_height ) )

HP_tittle = Button ( Pos_HP_tittle , Path_HP_tittle , go_to_home_page)
HP_tittle.resize( ( window_width , winddow_height ) )
HP_tittle.draw_image_center()

    # Save page Ones :

SP_back = Button( Pos_SP_back , Path_SP_back , None)
SP_back.resize( ( window_width , winddow_height ) )
SP_validate = Texte_button( Pos_SP_validate , Path_SP_validate , None , "Confirm")
SP_validate.set_size(( window_width /10, winddow_height /10 ))
SP_go_home = Texte_button ( Pos_SP_go_home , Path_SP_go_home , None , "Back")
SP_validate.set_size(( window_width /10, winddow_height /10 ))
SP_support = Button( Pos_SP_support , Path_SP_support , None)
SP_support.set_size( ( 2*window_width /3, 2*winddow_height /3 ) )
# SP_go_home = Button( )


# HP_next = Button( )


# Define fonctions :

def disable_all() :
    disable_all_HP_button()
    disable_all_SP_button()

def disable_all_HP_button() : 
    HP_back.set_disable()
    HP_exit.set_disable()
    HP_load_game.set_disable()
    HP_newc.set_disable()
    HP_support.set_disable()

def disable_all_SP_button() :
    SP_support.set_disable()
    SP_validate.set_disable()
    SP_go_home.set_disable()
    SP_back.set_disable()

def enable_all_HP_button() : 
    HP_back.set_enable()
    HP_exit.set_enable()
    HP_load_game.set_enable()
    HP_newc.set_enable()
    HP_support.set_enable()

def enable_all_SP_button() :
    SP_validate.set_enable()
    SP_go_home.set_enable()
    SP_back.set_enable()
    SP_support.set_enable()


def set_screen_SP() :
    disable_all_HP_button()
    enable_all_SP_button()

    SP_back.draw_image_center()
    SP_support.draw_image_center()
    SP_validate.draw_image_center()
    SP_validate.print_texte() 
    SP_go_home.draw_image_center()
    SP_go_home.print_texte()
    

    pg.display.update() 

def set_screen_HP() :
    disable_all_SP_button()
    enable_all_HP_button()

    HP_back.draw_image_center()
    HP_support.draw_image_center()
    HP_newc.draw_image_center()
    HP_exit.draw_image_center()
    HP_load_game.draw_image_center()
    pg.display.update()

# Test game 


disable_all()
while running :

    timer.tick(60)
    mouse_pos = pg.mouse.get_pos()

        
    # for event in pg.event.get() :
    #     if event.type == pg.QUIT :
    #         running = False
    #         pg.quit()
    #         sys.exit()
  
    
    pg.display.update() 

# mémory 

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

            if HP_tittle.touched( mouse_pos):
                set_screen_HP()
                HP_tittle.set_disable()

            if HP_exit.touched( mouse_pos ) : 
                running = False 
                pg.quit()
                sys.exit()

            if HP_newc.touched( mouse_pos ) :
                set_screen_SP()

            if SP_validate.overtext( mouse_pos ) :
                set_screen_HP()


