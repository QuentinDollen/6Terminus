from cgi import print_form
import sys
import pygame

home_sprite = ( 1920 , 1080  )

class bouton : 
         

    def is_overhead (self,pos) : return  self.__left <= pos[0] <= self.__left + self.__width and self.__up <= pos[1] <= self.__up + self.__height

    def is_touched (self , pos ) : return event.type == pygame.MOUSEBUTTONDOWN and self.is_overhead(self , pos )

    def get_left(self) : return self.__left
    def get_up(self) : return self.__up
    def get_width(self) : return self.__width
    def get_height(self) : return self.__height
    def get_image(self) : return self.image

    def draw(self) : pygame.draw.rect(screen,pygame.Color("Black"),pygame.Rect(self.__left,self.__up,self.__width,self.__height))




    def __init__(self,x,y,l,L,path_image) :
        self.__left = x
        self.__up = y 
        self.__width = l
        self.__height = L
        self.image = pygame.image.load( path_image )

        

# Tester l'objet :

# cool = bouton(10,10,100,100,"Controller/Home_page.PNG")
# cool.image = pygame.transform.scale(cool.image, (1920,1080))
# type(cool.get_image())


# Lancement de pygame :

pygame.init()
running = True

# Création de la fenêtre et du sprite

screen = pygame.display.set_mode( (0,0) , pygame.FULLSCREEN ) # Définition de l'écran
print(screen.get_size())
screen.fill(( 100 , 100 , 100)) # Setting de la couler de l'écran (R,G,B) 
timer = pygame.time.Clock() # Commencer le timer


sprite = pygame.Rect(10,10,100,100) # (x,y,l,L)
pygame.draw.rect(screen,pygame.Color("Green"),sprite)

# screen.blit(cool.get_image(),(0,0) )

# Boucle de jeu :

while running :
    pos = pygame.mouse.get_pos()
    timer.tick(60)
    print(pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Faire quitter le jeu
            running = False 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN : # Cliquer sur le carré
            pos = pygame.mouse.get_pos()
            # print(cool.is_overhead(pos))
           
    pygame.display.update()
