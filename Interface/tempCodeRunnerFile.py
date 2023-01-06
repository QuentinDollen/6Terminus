Cur_page = None
disable_all()
while running :
    

    timer.tick(60)
    mouse_pos = pg.mouse.get_pos()

            
    pg.display.update() 
    pg.display.flip()

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

        if Cur_page == "Select" : 

            if event.type == pg.KEYDOWN :




        if event.type == pg.MOUSEBUTTONDOWN :

            if Cur_page == "Home" :

                if HP_tittle.touched( mouse_pos ):
                   
                    set_screen_HP()
                    HP_tittle.set_disable()

                if HP_exit.touched( mouse_pos ) : 
                    running = False 
                    pg.quit()
                    sys.exit()

                if HP_newc.touched( mouse_pos ) :
                    set_screen_SP()
                    Cur_page = "Select"

            elif Cur_page == "Select" :

                

                if SP_validate.overtext( mouse_pos ) :
                    pass

                if SP_go_home.overtext( mouse_pos ) :
                    set_screen_HP()
                    Cur_page = "Home"


            else : 
                set_screen_HP()
                Cur_page = "Home"
                HP_tittle.set_disable()

