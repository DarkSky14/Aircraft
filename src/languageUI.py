from module import (
    button_modified, standart_text, GLOBAL_EVENT, background, work,
    update_display, big_text, sound_scroll, procent, height,
    ENGLISH, UKRAINIAN, config, pygame
)

from module.menu_client import (
    clicks, return_exit, version_game, 
    standart_curs, click_cursor
)

from pygame import (
    QUIT, K_ESCAPE, KEYDOWN
)
from module.game_client import set_fps, get_fps, tick_fps 


def language_get(): 
    global work
    #surfM = UI.SurfaceM(e, Surface.main_surface)
    s = 35

    def update_text():
        global language
        standart_text.set_language(language)
        big_text.set_language(language)
        button_modified.set_language(language)
         
    def exitLANGUAGE():
        global work
        work = False
    
    button1 = button_modified.copy()
    button1.set_object((-300) * procent, (220) * procent, (300, 30))
    button1.moved(50, None, 300)
    
    button2 = button_modified.copy()
    button2.set_object(button1.get_x_pos(), (button1.get_y_pos() + button1.get_size_y() + (10 * procent)), (300, 30))
    button2.moved(50, None, 300)

    button4 = button_modified.copy()
    button4.set_object(button2.get_x_pos(), (button2.get_y_pos() + button2.get_size_y() + (30 * procent)), (300, 30))
    button4.moved(50, None, 300)

    def button_1():
        def button(): 
            global language
            button1.check_config({"effect": "True"}, clicks)
            if button1.check_config({"language": "EN"}) == False:
                button1.write_in_config({"language": "EN"})
                language = (ENGLISH)
                update_text()

        button1.animation()
        button1.Button(button)
        button1.get_text(standart_text,'English', (0, 0, 0))

    def button_2():
        def button(): 
            global language
            button2.check_config({"effect": "True"}, clicks)
            if button2.check_config({"language": "UA"}) == False:
                button2.write_in_config({"language": "UA"})
                language = (UKRAINIAN)
                update_text()

        button2.animation()
        button2.Button(button)
        button2.get_text(standart_text, 'Українська', (0, 0, 0))

    def button_3():
        #surfM.Button(50, (220 + s*2), (300, 30), 75, (221 + s*2), 13, clicks, Русский, "Language", {"language": "RU"})
        standart_text.draw_text('Русский', 75, (221 + s*2), (0, 0, 0))

    def button_4():
        def button(): 
            button4.check_config({"effect": "True"}, return_exit)
            exitLANGUAGE()

        button4.animation()
        button4.Button(button)
        button4.get_text(standart_text, "6")
    
    set_fps(60)

    def initialiaze():
        for event in pygame.event.get():
            GLOBAL_EVENT.event = event
            if GLOBAL_EVENT.event.type == QUIT:
                pygame.quit()
                exit()

            GLOBAL_EVENT.mouse_get()
            GLOBAL_EVENT.MOUSEBUTTONDOWN() 
            
            if GLOBAL_EVENT.comparison_type(KEYDOWN) and GLOBAL_EVENT.comparison_key(K_ESCAPE):
                config.check({"effect": "True"}, return_exit)
                GLOBAL_EVENT.set_key(0)
                exitLANGUAGE()

        background()
        
        button_1()
        button_2()
        button_4()    
        
        version_game()
        GLOBAL_EVENT.MOUSEBUTTONDOWN()
        GLOBAL_EVENT.event_button_check(standart_curs, click_cursor, sound_scroll)
        big_text.get_set_text("2", 70 * procent, 150 * procent)        
        
        get_fps(coordinate=(3, height - (20 * procent)))
        tick_fps()
        update_display()

    while work:     
        initialiaze()

    work = True

if __name__ == "__main__":
    set_fps(60)
    language_get()