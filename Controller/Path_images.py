# Warning : Be on terminus folder 

# Gathering all pictures path :

# Home page as HP :

from os import getcwd
import pygame

screen = pygame.display.set_mode( (0,0), pygame.FULLSCREEN )

class Button :

    # Initialisation of Button object :

    def __init__( self , pos , path_image ) :
        self.__image = pygame.image.load( path_image )
        self.__left = pos[0]
        self.__up = pos[1] 
        self.__width = self.__image.get_size()[0]
        self.__height = self.__image.get_size()[1]
        self.__text = "Ceci est un texte"
      

    # Define geters

    def get_image(self) : return self.__image
    def get_left(self) : return self.__left
    def get_up(self) : return self.__up
    def get_width(self) : return self.__image.get_size()[0]
    def get_height(self) : return self.__image.get_size()[1]


    # Define Button's methods

        # Tell if the mouse is over the button object

    def overhead ( self , pos ) :
        if  self.get_left() <= pos[0] <= self.get_left()  + self.get_width() and self.get_up()  <= pos[1] <= self.get_up() + self.get_height() :
            temp_image = self.get_image()            
            screen.blit(pygame.Surface( (self.get_width(),self.get_height() ) , pygame.Color("Black")) , (self.get_left() , self.get_up()) )
            pygame.Surface.set_alpha(temp_image , 60)
            screen.blit(temp_image  ,(self.get_left() , self.get_up()))
            return True
        else :
            self.draw_image()
            return False

        # Tell if the mouse click on the button object

    def touched ( self , pos ) : return event.type == pygame.MOUSEBUTTONUP and self.overhead( pos )

        # Draw the Image on the screen :

    def draw_image ( self ) :  screen.blit( self.get_image() , ( self.get_left() , self.get_up() ) )


test_screen = pygame.display.set_mode( (0,0) , pygame.FULLSCREEN)



path_home_page = "/Version_MVC/View/Sprites/Home_page/"
dimension_home_page = test_screen.get_size()

Path_HP_background = f"{getcwd()}{path_home_page}HP_background.PNG"
Path_HP_exit = f"{getcwd()}{path_home_page}HP_exit.PNG"
Path_HP_new_carrer = f"{getcwd()}{path_home_page}HP_new_carrer.PNG"
Path_HP_load_game = f"{getcwd()}{path_home_page}HP_load_game.PNG"

Pos_HP_background = ( 0 , 0 )
Pos_HP_exit = ( 810 , 660 )
Pos_HP_new_game = ( 810 , 580 )
Pos_HP_load_game = ( 810 , 620 )

# Game page :
path_game_page = "/Version_MVC/View/Sprites/Game_page/"
Path_GP_background = f"{getcwd()}{path_game_page}GP_back_panel.PNG"

Pos_GP_backGround = ( 1400 , 0)