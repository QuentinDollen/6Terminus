# Import needed libraries  :

import pygame
from pygame.locals import *
import sys
import Path_images as pi



# Définition of the object Button 

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




# Starting pygame and initialise the home screen :

pygame.init()
running = True
pygame.font.Font("CWFARKAGE.TTF")


HP_Home_page = Button(pi.Pos_HP_background,pi.Path_HP_background)
HP_New_game_button = Button( pi.Pos_HP_new_game , pi.Path_HP_new_carrer)
HP_Exit_button = Button( pi.Pos_HP_exit , pi.Path_HP_exit)
HP_Load_game_button = Button( pi.Pos_HP_load_game  , pi.Path_HP_load_game)

screen = pygame.display.set_mode( (0,0), pygame.FULLSCREEN )
timer = pygame.time.Clock()

# TEST :





# Starting fillinf the home page :

HP_Home_page.draw_image()
HP_Exit_button.draw_image()
HP_New_game_button.draw_image()
HP_Load_game_button.draw_image()


while running :

    timer.tick(60)

    pos = pygame.mouse.get_pos()

    HP_New_game_button.overhead( pos )
    HP_Exit_button.overhead( pos )

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP :
            if HP_New_game_button.touched(pos) :
                pass
            if HP_Exit_button.touched(pos) :
                running = False 
                pygame.quit()
                sys.exit()

    pygame.display.update()
        