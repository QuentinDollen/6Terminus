import pygame as pg
# import View.game as game
from Controller.Data_controller import *







def main():


# Global varibles 

    # Variable pour les boucles dans le jeu 
    running = True
    playing = True
    Launch = True
    global Cur_page
    Cur_page = None

    

    pg.init()
    pg.mixer.init()
    global screen
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    clock = pg.time.Clock()
    set_screen_tittle( screen )   

    # implement game
    
    # Game = game.Game(screen, clock)

    while running:


        clock.tick(60)
        
        mouse_track = pg.mouse.get_pos()    
        pg.display.update() 
        pg.display.flip()

        
        
        while Launch :

            pg.display.flip()
            mouse_track = pg.mouse.get_pos()  

            for event in pg.event.get() :

                if event.type == pg.QUIT :
                    running = False 
                    Launch = False 
                    pg.quit()
                    sys.exit()


                if event.type == pg.MOUSEBUTTONDOWN : 
                        
                    if Cur_page == "Home" : # Si on se trouve sur la page Home 

                        if HP_exit.overhead( mouse_track , screen ) :
                            running = False 
                            Launch = False 
                            pg.quit()
                            sys.exit()

                        elif HP_newc.overhead( mouse_track , screen ) :
                            Cur_page = "Select"
                            set_screen_SP( screen )                         
                
                        elif HP_load_game.overhead( mouse_track , screen ) :
                            pass

                    elif Cur_page == "Select" : # Si on se trouve sur la page Select

                        # Erreur dans la conception avec les rectangle 

                        if SP_go_home_txt.collidepoint(  mouse_track ) :
                            Cur_page = "Home"
                            set_screen_HP( screen )

                        if SP_validate_txt.get_rect().collidepoint( mouse_track[0] , mouse_track[1]) : 
                            print("Lancement de partie ")
                            

                    else : # Si on se trouve dans l'écran titre

                        Cur_page = "Home"
                        set_screen_HP( screen )
                       
        

        # while playing :
        #     pass
            # game loop here
            # Game.run()



if __name__ == "__main__":
    main()