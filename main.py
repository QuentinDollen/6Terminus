import pygame as pg

from Interface.Data_controller import *
from Interface.InputBoxName import *
from View.game import * 
from Model.logique import * 


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

    Game_terminus = Game(screen , clock)


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

                if event.type == pg.MOUSEMOTION :

                    if Cur_page == "Home" :

                        HP_exit.transparenci( mouse_track , screen )
                        HP_load_game.transparenci( mouse_track , screen )
                        HP_newc.transparenci( mouse_track , screen )
                        pg.display.flip()

                if event.type == pg.KEYDOWN and event.type != pg.K_LSHIFT :

                    if Cur_page == "Select" :
                        SP_input.ajout_char(event , screen)

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
                            SP_input.draw(screen)                       
                
                        elif HP_load_game.overhead( mouse_track , screen ) :
                            pass

                    elif Cur_page == "Select" : # Si on se trouve sur la page Select

                        # Erreur dans la conception avec les rectangle 

                        if SP_go_home_txt_R.collidepoint(  mouse_track ) :
                            Cur_page = "Home"
                            set_screen_HP( screen )

                        if SP_validate_txt_R.collidepoint( mouse_track ) : 
                            Launch = False
                            playing = True 
                        
                        SP_input.collide(mouse_track)
                            

                    else : # Si on se trouve dans l'écran titre

                        Cur_page = "Home"
                        set_screen_HP( screen )
                       
        

        while playing :

            Game_terminus.run()
            
            

if __name__ == "__main__":
    main()