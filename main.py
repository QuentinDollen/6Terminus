import pygame as pg
# import View.game as game
from Controller.Data_controller import *


def main():


# Global varibles 

    running = True
    playing = True
    Launch = True

    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()
    disable_all()    

    # implement game
    
    # Game = game.Game(screen, clock)

    while running:


        clock.tick(60)
        mouse_pos = pg.mouse.get_pos()    
        pg.display.update() 
        pg.display.flip()



        while Launch :
                global Cur_page
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

                        if Cur_page == "Home" :

                                if HP_tittle.touched( mouse_pos ):
                                    set_screen_HP()
                                    HP_tittle.set_disable()

                                if HP_exit.touched( mouse_pos ) : 
                                    Launch = False 
                                    pg.quit()
                                    sys.exit()

                                if HP_newc.touched( mouse_pos ) :
                                    set_screen_SP()

                        elif Cur_page == "Select" :


                            if SP_validate.overtext( mouse_pos ) :
                                pass

                            if SP_go_home.overtext( mouse_pos ) :
                                set_screen_HP()

                            if SP_gname.collidepoint( mouse_pos ) :
                                on_button_click()

                        else : 
                            set_screen_HP()
                            HP_tittle.set_disable()
            

        while playing :
            pass
            # game loop here
            # Game.run()



if __name__ == "__main__":
    main()