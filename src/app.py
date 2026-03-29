from sys import exit

from module import ( 
    button_modified, standart_text, GLOBAL_EVENT, background, work,
    update_display, big_text, sound_scroll, log, fix_import, procent,
    height, screen
)

import pygame

from pygame import QUIT

from module.menu_client import (
    clicks, return_exit, version_game, standart_curs, click_cursor
)

from module.game_client import (
    set_fps, get_fps, tick_fps
)


# Setup pygame/window -----------------------------
log.info("Setup icon window...")
icon_obj = pygame.image.load(fix_import + 'library/Aircraft.ico').convert()
icon = pygame.transform.scale(icon_obj, screen)
log.info("Icon window setup complete.")
log.info("Setup background image options...")

pygame.display.set_caption('Aircraft',"Aircraft")
pygame.display.set_icon(icon) 

def main_menu():
    global work

    def exitGame():     
        log.info("Successful stop.")
        pygame.quit()
        exit()

    #sub_surface = initial.UI.MyDrawObject(50, 240, (350, 250), initial.d)
    #sub_surface.draw_object((100, 100, 100), 300, 10)

    button1 = button_modified.copy()
    button1.set_object((-300 * procent), (220 * procent), (300, 30))
    button1.moved(50, None, 300) 
    
    button2 = button_modified.copy()
    button2.set_object((-300 * procent), (button1.get_y_pos() + button1.get_size_y() + (10 * procent)), (300, 30))
    button2.moved(50, None, 300) 

    button3 = button_modified.copy()
    button3.set_object((-300 * procent), (button2.get_y_pos() + button2.get_size_y() + (10 * procent)), (300, 30))
    button3.moved(50, None, 300) 

    button4 = button_modified.copy()
    button4.set_object((-300 * procent), (button3.get_y_pos() + button3.get_size_y() + (25 * procent)), (300, 30))
    button4.moved(50, None, 300) 

    def button_1():
        def button(): 
            button1.check_config({"effect": "True"}, clicks)
            from level import level
            level()
            #button1.moved(-300, None, 0)
            #button1.animation(level())               
            #button1.moved(50, None, 300) 
            
        button1.Button(button)
        button1.animation()
        button1.get_text(standart_text, "0")
    
    def button_2():
        def button(): 
            button2.check_config({"effect": "True"}, clicks)
            from options import options
            options(25, 150)
            #button2.moved(50, None, 0) 
            #button2.animation(opti())

        button2.Button(button)
        button2.animation()
        button2.get_text(standart_text, "1")
    
    def button_3():
        def button(): 
            button3.check_config({"effect": "True"}, clicks)
            from languageUI import language_get
            language_get()

        button3.Button(button)
        button3.animation()
        button3.get_text(standart_text, "2")
    
    def button_4():
        def button(): 
            button4.check_config({"effect": "True"}, return_exit)
            exitGame()

        button4.Button(button)
        button4.animation()
        button4.get_text(standart_text, "6")

    set_fps(60)

    def initialize():
        for event in pygame.event.get():
            GLOBAL_EVENT.event = event

            if GLOBAL_EVENT.comparison_type(QUIT):
                pygame.quit()
                exit()

            GLOBAL_EVENT.mouse_get()
            GLOBAL_EVENT.MOUSEBUTTONDOWN() 

        background() 
        
        button_1() 
        button_2() 
        button_3()   
        button_4() 

        version_game()
        GLOBAL_EVENT.event_button_check(standart_curs, click_cursor, sound_scroll)
        big_text.get_set_text("7", 70 * procent, 150 * procent)     

        get_fps(coordinate=(3, height - (20 * procent)))
        tick_fps()
        update_display()

    while work:   
        initialize()    

    work = True    

if __name__ == "__main__":
    log.info("Successful start...")
    main_menu()
