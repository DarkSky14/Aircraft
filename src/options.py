from module import (
    button_modified, GLOBAL_EVENT, work, screen, music, SurfaceM,
    update_display, big_text, sound_scroll, procent, pygame,
    main_surface, conf_height, conf_width, fix_import, d, log
)
import module

from module.menu_client import (
    sound_menu, clicks, return_exit, version_game, 
    visible_cursor, standart_curs, click_cursor
)
from pygame import (
    QUIT, K_ESCAPE, KEYDOWN
)
from module.game_client import set_fps, tick_fps


fon_obj = pygame.image.load(fix_import + 'library/pictures/fon_.png').convert()
fon = pygame.transform.scale(fon_obj, screen)
log.info("Background image options setup complete.")


def options(x_c = (536.5), y_c = (255.5)):
    global work
    x_size = 350 * procent
    y_size = 250 * procent

    surfM = SurfaceM(GLOBAL_EVENT, d, size_config=procent)

    surfM.set_object(x_c*procent, y_c*procent, (x_size, y_size))

    x_c = surfM.get_x_pos()
    y_c = surfM.get_y_pos()

    def quitOPTIONS():
        global work
        work = False
        
    def exitOPTIONS():
        global game_work
        module.game_work = False  
        quitOPTIONS()
    
    def sound():
        music.music_all(sound_menu)

    button1 = button_modified.copy()
    button1.set_object((x_c) + (23 * procent), (y_c) + 85 * procent, (300, 30))
    button1.text_change({"effect": "True"}, "8", "9")
    
    button2 = button_modified.copy()
    button2.set_object(button1.get_x_pos(), (button1.get_y_pos() + button1.get_size_y() + (10 * procent)), (300, 30))
    button2.text_change({"music": "True"}, "8", "9")

    button3 = button_modified.copy()
    button3.set_object(button2.get_x_pos(), (button2.get_y_pos() + button2.get_size_y() + (20 * procent)), (300, 30))
    
    def button_1():
        global is_music
        if button1.check_config({"effect": "True"}, clicks):
            button1.write_in_config({"effect": "False"})
            is_music = False

        elif button1.check_config({"effect": "False"}):
            button1.write_in_config({"effect": "True"})
            is_music = True

        else:
            button1.write_in_config({"effect": "True"})
            log.error("Error in config file, missing 'effect' key. Default value 'True' was set.")
            is_music = True
            
        button1.text_change({"effect": "True"}, "8", "9")     

    def button_2():
        button2.check_config({"effect": "True"}, clicks)

        if button2.check_config({"music": "True"}):
            button2.write_in_config({"music": "False"})
            sound()

        elif button2.check_config({"music": "False"}):
            button2.write_in_config({"music": "True"})
            sound()
        
        else:
            button2.write_in_config({"music": "True"})
            log.error("Error in config file, missing 'music' key. Default value 'True' was set.")
            sound()

        button2.text_change({"music": "True"}, "8", "9")

    def button_3(): 
        button3.check_config({"effect": "True"}, return_exit)
        exitOPTIONS()

    fon.set_alpha(20)
    anim_time_fon = 0

    version_game()
    sound()
    visible_cursor()  
    
    def initialize():
        for event in pygame.event.get():
            GLOBAL_EVENT.event = event
            if GLOBAL_EVENT.event.type == QUIT:
                pygame.quit()
                exit()

            GLOBAL_EVENT.mouse_get()
            GLOBAL_EVENT.MOUSEBUTTONDOWN() 
            
            if GLOBAL_EVENT.comparison_type(KEYDOWN):
                if GLOBAL_EVENT.comparison_key(K_ESCAPE):
                    GLOBAL_EVENT.set_key(0)
                    quitOPTIONS()  

        #surfM.update_pos()
        #surfM.animation_resize()
        surfM.main_work(quitOPTIONS) 

        button1.Button(button_1)
        button1.get_text_self("12")
        
        button2.Button(button_2)
        button2.get_text_self("10") 

        button3.Button(button_3)
        button3.get_text_self("6")
 
        GLOBAL_EVENT.event_button_check(standart_curs, click_cursor, sound_scroll)
        big_text.get_set_text("1", (x_c) + 45 * procent, (y_c) + 25 * procent)
        
        #get_fps(coordinate=(3, Surface.height - 20))
        tick_fps()      
        update_display()

    while work:       
        if anim_time_fon <= 180:
            anim_time_fon += 20
            main_surface.blit(fon, (0 + conf_width, 0 + conf_height))

        initialize()
        
    work = True


if __name__ == "__main__":
    set_fps(60)
    options()