# Définition of the object Button 

class Button :

    # Initialisation of Button object :

    def __init__( self , x , y , path_image ) :
        self.__image = pygame.image.load( path_image )
        self.__left = x
        self.__up = y 
        self.__width = self.__image.get_size()[0]
        self.__height = self.__image.get_size()[1]
      

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
            return True

        # Tell if the mouse click on the button object

    def touched ( self , pos ) : return event.type == pygame.MOUSEBUTTONDOWN and self.overhead( pos )

        # Draw the Image on the screen :

    def draw_image ( self ) : return screen.blit( self.get_image() , self.get_left() , self.get_up() )