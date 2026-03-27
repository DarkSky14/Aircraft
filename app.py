from sys import exit
from clients.module import *
from clients.module.Surface import ScrollingBG
import pygame

from pygame import (
    QUIT, K_DOWN, K_UP, 
    K_RIGHT, K_LEFT, K_ESCAPE,
    KEYDOWN
)

from clients.menu_client import *
from clients.game_client import * 

# Setup pygame/window -----------------------------
log.info("Setup icon window...")
icon_obj = pygame.image.load('library/Aircraft.ico').convert()
icon = pygame.transform.scale(icon_obj, screen)
log.info("Icon window setup complete.")
log.info("Setup background image options...")
fon_obj = pygame.image.load('library/pictures/fon_.png').convert()
fon = pygame.transform.scale(fon_obj, screen)
log.info("Background image options setup complete.")

pygame.display.set_caption('Aircraft',"Aircraft")
pygame.display.set_icon(icon) 

log.info("Load base font...")
BASEFONT = pygame.font.SysFont("Calibri", round(20 * procent))
log.info("Base font successfully loaded.")

def on_music() -> bool:
    if config.check({"effect": "True"}) == True:
        return True
    else:
        return False

is_music = on_music()

def sound_scroll():
    if is_music == True:
        scroll()
        
fon_background = ScrollingBG(bg, bg_speed)

def background():
    fon_background.update()
    fon_background.draw(d)
 
def update_display():
    pygame.display.update(conf_width, conf_height, width, height)

def get_fps(font: pygame.font.Font = BASEFONT, color: tuple = (200, 200, 200), coordinate: tuple = (3,3)):
    main_surface_fps = font.render(str(int(FPS.get_fps())), True, (color))
    rect_obgect = main_surface_fps.get_rect()
    rect_obgect.topleft = coordinate
    d.blit(main_surface_fps, rect_obgect)

button_modified = ModuleButton(GLOBAL_EVENT, d, config, standart_text, procent)

music = mus.Music(config, temp, sound_menu, 0.1)
music.music_all(sound_menu)

game_work = True
work = True

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
            #from options import options
            options(25, 150)
            #button2.moved(50, None, 0) 
            #button2.animation(opti())

        button2.Button(button)
        button2.animation()
        button2.get_text(standart_text, "1")
    
    def button_3():
        def button(): 
            button3.check_config({"effect": "True"}, clicks)
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
        game_work = False  
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

def sourse(speed_w1, speed_w2, ENEMY, max_score, level = {str: int}):   
    global game_work, work 
    from clients.game_client import player_imgs, player_speed
    from clients.game_client import player, player_rect

    fon_background = ScrollingBG(bg, bg_speed1)
    def background():
        fon_background.update()
        fon_background.draw(d)
    
    set_fps(90)

    img_index = 0
    scores = 0 
    bonusies = []
    enemies = []


    def clean_bon_and_en():
        """Delete all bonusies and enemies"""
        bonusies.clear()
        enemies.clear()

    check_first_while = 0  

    while game_work:
        pressed_keys = pygame.key.get_pressed()  
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    check_first_while = 0
                    music.music_pause()
                    music.music_load(sound_menu)
                    work = True
                    options()
        
            if event.type == CREATE_BONUS:
                bonusies.append(create_bonus())
            
            if event.type == ENEMY:
                enemies.append(create_enemy(speed_w1, speed_w2))
            
            if event.type == CHANGE_IMG:
                img_index += 1
                if img_index == len(player_imgs):
                    img_index = 0
                player = player_imgs[img_index] 
        
             
        background()
        d.blit(BASEFONT.render(str(scores), True, BLACK), (d.get_width() - 30, 0))
        d.blit(player, (player_rect))
        version_game()
        
        for enemy in enemies:
            enemy[1] = enemy[1].move(-enemy[2], 0)
            d.blit(enemy[0], enemy[1])
        
            if enemy[1].left < -200:
                enemies.pop(enemies.index(enemy))

            if player_rect.colliderect(enemy[1]):
                game_work = False
                music.music_all(sound_menu)
        
        for bonus in bonusies:             
            bonus[1] = bonus[1].move(-bonus[2], 2)
            d.blit(bonus[0], bonus[1])
        
            if bonus[1].bottom > (height + 300):
                bonusies.pop(bonusies.index(bonus))
        
            if player_rect.colliderect(bonus[1]):
                bonusies.pop(bonusies.index(bonus))
                scores += 1
            
            #try:
             #   if bonus[1].colliderect(enemy[1]):
              #      bonusies.pop(bonusies.index(bonus))
               #     enemies.pop(enemies.index(enemy))
                    
           #except: None
        
        if pressed_keys [K_DOWN] and not player_rect.bottom >= height:
            player_rect = player_rect.move(0, player_speed)
        
        if pressed_keys [K_UP] and not player_rect.top <= 0:
            player_rect = player_rect.move(0, -player_speed)

        if pressed_keys [K_RIGHT] and not player_rect.right >= width:
            player_rect = player_rect.move(player_speed, 0)
         
        if pressed_keys [K_LEFT]and not player_rect.left <= 0:
            player_rect = player_rect.move(-player_speed, 0)
            
        if scores >= max_score:
            if config.check(level, invisible_cursor) == False:
                config.write(level)
            game_work = False

        if check_first_while == 0 and game_work != False:
            check_first_while =+ 1
            
            invisible_cursor()
            music.music_load(sound_game)
            music.music_unpause()
        
        get_fps(GAME_TEXT, RED, (10,10))
        tick_fps()
        update_display()
    
    game_work = True
    clean_bon_and_en()
    music.set_position()
    music.music_all(sound_menu)
    standart_curs() 
    visible_cursor() 

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

def level():
    global work
    from clients.game_client import sw1, sh1, CREATE_ENEMY1, max_score1
    from clients.game_client import sw2, sh2, CREATE_ENEMY2, max_score2
    from clients.game_client import sw3, sh3, CREATE_ENEMY3, max_score3

    def exitLEVEL():
        global work
        work = False
        
    button1 = button_modified.copy()
    button1.set_object(-300 * procent, 220 * procent, (300, 30))
    button1.moved(50, None, 300) 
    
    button2 = button_modified.copy()
    button2.set_object(button1.get_x_pos(), (button1.get_y_pos() + button1.get_size_y() + (10 * procent)), (300, 30))
    button2.moved(50, None, 300) 

    button3 = button_modified.copy()
    button3.set_object(button2.get_x_pos(), (button2.get_y_pos() + button2.get_size_y() + (10 * procent)), (300, 30))
    button3.moved(50, None, 300) 

    button4 = button_modified.copy()
    button4.set_object(button3.get_x_pos(), (button3.get_y_pos() + button3.get_size_y() + (30 * procent)), (300, 30))
    button4.moved(50, None, 300) 

    def button_1():
        def lvl1(): 
            sourse(sw1, sh1, CREATE_ENEMY1, max_score1, {"level": 2}) 
        
        def button(): 
            button1.check_config({"effect": "True"}, clicks)
            lvl1()
            set_fps(60)

        button1.animation()
        button1.Button(button)    
        button1.get_text(standart_text, "3") 
     
    def button_2():   
        def l2():            
            def lvl2(): 
                sourse(sw2, sh2, CREATE_ENEMY2, max_score2, {"level": 3})

            if config.get_value("level") >= 2:
                lvl2()

        def button(): 
            button2.check_config({"effect": "True"}, clicks)
            l2()
            set_fps(60)

        button2.animation()
        button2.Button(button)
        button2.get_text(standart_text, "4")
    
    def button_3():       
        def l3(): 
            def lvl3(): 
                sourse(sw3, sh3, CREATE_ENEMY3, max_score3, {"level": 3.1})
            
            if config.get_value("level") >= 3:
                lvl3()
        
        def button(): 
            button3.check_config({"effect": "True"}, clicks)
            l3()
            set_fps(60)

        button3.animation()
        button3.Button(button)
        button3.get_text(standart_text, "5")
    
    def button_4():
        def button():
            button4.check_config({"effect": "True"}, return_exit) 
            exitLEVEL()
        
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
                exitLEVEL()

        background()

        button_1()
        button_2()
        button_3()
        button_4()
            
        version_game()
        GLOBAL_EVENT.MOUSEBUTTONDOWN()
        GLOBAL_EVENT.event_button_check(standart_curs, click_cursor, sound_scroll)
        big_text.get_set_text("11", 70 * procent, 150 * procent)
        
        get_fps(coordinate=(3, height - (20 * procent)))
        tick_fps()
        update_display()

    while work:
        initialiaze()

    work = True

if __name__ == "__main__":
    log.info("Successful start...")
    main_menu()
