import sys
import pygame
import clients.Backend.language as Language
import clients.Backend._lib_ as my_json
import clients.Backend.event as Event
import clients.Backend.logged as Log

pygame.init()

import clients.Frontend.surface as Surface
import clients.Frontend.Text as Text
import clients.Frontend.UI as UI
import clients.Frontend.button as Button
from pygame import (
    QUIT, K_DOWN, K_UP, 
    K_RIGHT, K_LEFT, K_ESCAPE,
    MOUSEBUTTONDOWN, KEYDOWN
)

from clients.menu_client import *
from clients.game_client import * 

# Setup pygame/window -----------------------------
icon = pygame.transform.scale(pygame.image.load('library/Aircraft.ico').convert(), Surface.screen)
fon = pygame.transform.scale(pygame.image.load('library/pictures/fon_.png').convert(), Surface.screen)

pygame.display.set_caption('Aircraft',"Aircraft")
pygame.display.set_icon(icon) 

BASEFONT = pygame.font.SysFont("Calibri", 20)
button_list = []

def event_check_button(standart, nostandart, button_list: list = button_list):
        if button_list == ["."]:
            nostandart()
            button_list.clear()
            button_list.append("1")
            my_json.config.check({"effect": "True"}, scroll)
        elif button_list == ["1", "."]:
            nostandart()
            button_list.clear()
            button_list.append("1")
        else:
            button_list.clear()
            standart()
        
fon_background = Surface.ScrollingBG(bg, bg_speed)

def background():
    fon_background.update()
    fon_background.draw(Surface.d)
 
def update_display():
    pygame.display.update(int(Surface.conf_width), int(Surface.conf_height), Surface.width, Surface.height)

e = Event.EventControl()

sub_surface = Surface.SubSurface(350, 250).surface(Surface.d, 50, 240)
b_s = Button.ButtonBased(e, button_list, Surface.d, my_json.config)
b_c = Button.ButtonChecked(e, button_list, Surface.d, my_json.config)
b_l = Button.ButtonLang(e, button_list, Surface.d, my_json.config)

music = mus.Music(my_json.config, my_json.temp, 0.1)
#game_music = mus.Music(my_json.config, my_json.temp, 0.1)
music.music_all(sound_menu)

text_change = Text.ModuleText(Text.standart_text)
big_text = Text.AllText(Text.big_text)
standart_text = Text.AllText(Text.standart_text)

game_work = True
work = True

def main_menu():
    global work

    def exit():     
        pygame.quit()
        sys.exit()
            
    def opti():
        options(50, 240)  

    #sub_surface = initial.UI.MyDrawObject(50, 240, (350, 250), initial.d)
    #sub_surface.draw_object((100, 100, 100), 300, 10)

    button1 = b_s.copy()
    button1.set_button(-300, 220, (300, 30))
    button1.moved(50, None, 300) 
    
    button2 = b_s.copy()
    button2.set_button(-300, 255, (300, 30))
    button2.moved(50, None, 300) 

    button3 = b_s.copy()
    button3.set_button(-300, 290, (300, 30))
    button3.moved(50, None, 300) 

    button4 = b_s.copy()
    button4.set_button(-300, 360, (300, 30))
    button4.moved(50, None, 300) 
        
    def button_1():
        def button(): 
            #button1.moved(-300, None, 0)
            button1.animation(button1.button(clicks, level))               
            #button1.moved(50, None, 300) 
            
        button1.Button(50, 220, (300, 30), button)
        button1.animation()
        button1.text_set(standart_text, "0",  65, 223)
    
    def button_2():
        def button(): 
            #button2.moved(50, None, 0) 
            button2.animation(button2.button(clicks, opti))

        button2.Button(50, 255, (300, 30), button)
        button2.animation()
        button2.text_set(standart_text, "1", 65, 257)
    
    def button_3():
        def button(): button3.button(clicks, language_get)
        button3.Button(50, 290, (300, 30), button)
        button3.animation()
        button3.text_set(standart_text, "2", 65, 292)
    
    def button_4():
        def button(): 
            button4.button(return_exit, exit)
        button4.Button(50, 360, (300, 30), button)
        button4.animation()
        button4.text_set(standart_text, "6")

    set_fps(60)

    while work:       
        background() 
        version_game() 
        event_check_button(standart_curs, click_cursor)

        e.event_pool()
        e.MOUSEBUTTONDOWN()
        
        button_1() 
        button_2() 
        button_3()   
        button_4() 
        
        big_text.text("7", 70, 150)     

        tick_fps()
        update_display()

    work = True    

def options(x_c = 540.0, y_c = 347.5):
    global work
    surfM = UI.SurfaceM(e, Surface.d)
    surfM.set_object(x_c, y_c, (350, 250))
    surfM.change_size(900, 600, 300)

    def quit():
        global work
        work = False
        st = 0
        return st, work
        
    def exit():
        global game_work
        clean_bon_and_en() 
        game_work = False  
        quit()
    
    def sound():
        music.music_all(sound_menu)
    
    version_game()
    sound()
    visible_cursor()  

    button1 = b_c.copy()
    button1.set_button(x_c, y_c, (300, 30))
    button1.text_change(text_change, {"effect": "True"}, "8", "9")
    
    button2 = b_c.copy()
    button2.set_button(x_c, (y_c + 35), (300, 30))
    button2.text_change(text_change, {"music": "True"}, "8", "9")

    button3 = b_s.copy()
    button3.set_button(x_c, (y_c + 81), (300, 30))
    
    def button_1():
        def button(): 
            button1.button(({"effect": "True"}, {"effect": "False"}), clicks, vie)
            button1.text_change(text_change, {"effect": "True"}, "8", "9")

        button1.Button(x_c, y_c, (300, 30), button)
        button1.text_set(text_change, {"effect": "True"}, "12", "8", "9")
            
    def button_2():
        def button(): 
            button2.button(({"music": "True"}, {"music": "False"}), clicks, sound)
            button2.text_change(text_change, {"music": "True"}, "8", "9")

        button2.Button(x_c, (y_c + 35), (300, 30), button)
        button2.text_set(text_change, {"music": "True"}, "10", "8", "9")

    def button_3():
        def button(): 
            button3.button(return_exit, exit)
        button3.Button(x_c, (y_c + 81), (300, 30), button)
        button3.text_set(standart_text, "6", (x_c + 20), (y_c + 80.5))

    fon.set_alpha(150)
    Surface.main_surface.blit(fon, (0 + Surface.conf_width, 0 + Surface.conf_height))

    while work:       
        event_check_button(standart_curs, click_cursor)
        e.event_pool()
        e.K_ESCAPE(exit=quit)
        e.MOUSEBUTTONDOWN()    

        #surfM.animation_resize(surfM.update_pos())  
        surfM.surface_wait(quit)

        button_1()
        button_2() 
        button_3()
        
        big_text.text("1", (x_c + 20), (y_c - 60))
        
        tick_fps()      
        update_display()

    work = True

def sourse(speed_w1, speed_w2, ENEMY, max_score, level = {str: int}):   
    global game_work 
    from clients.game_client import scores, player_imgs, player_speed
    from clients.game_client import player, player_rect, img_index
    
    pygame.init()    

    fon_background = Surface.ScrollingBG(bg, bg_speed1)
    def background():
        fon_background.update()
        fon_background.draw(Surface.d)
    
    set_fps(90)

    #music.music_stop()
    #game_music.create_mus_channel(sound_game)
    ch = 0  

    while game_work:
        pressed_keys = pygame.key.get_pressed()  
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    #initial.UI.work = True
                    ch = 0
                    #game_music.music_stop()
                    options()
                    #music.music_play()
        
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
        Surface.d.blit(BASEFONT.render(str(scores), True, BLACK), (Surface.d.get_width() - 30, 0))
        Surface.d.blit(player, (player_rect))
        version_game()
        
        for enemy in enemies:
            enemy[1] = enemy[1].move(-enemy[2], 0)
            Surface.d.blit(enemy[0], enemy[1])
        
            if enemy[1].left < -200:
                enemies.pop(enemies.index(enemy))

            if player_rect.colliderect(enemy[1]):
                game_work = False
                #music.music_all(sound_menu)
        
        for bonus in bonusies:             
            bonus[1] = bonus[1].move(-bonus[2], 2)
            Surface.d.blit(bonus[0], bonus[1])
        
            if bonus[1].bottom > 1000:
                bonusies.pop(bonusies.index(bonus))
        
            if player_rect.colliderect(bonus[1]):
                bonusies.pop(bonusies.index(bonus))
                scores += 1
            
            #try:
             #   if bonus[1].colliderect(enemy[1]):
              #      bonusies.pop(bonusies.index(bonus))
               #     enemies.pop(enemies.index(enemy))
                    
           #except: None
        
        if pressed_keys [K_DOWN] and not player_rect.bottom >= Surface.height:
            player_rect = player_rect.move(0, player_speed)
        
        if pressed_keys [K_UP] and not player_rect.top <= 0:
            player_rect = player_rect.move(0, -player_speed)

        if pressed_keys [K_RIGHT] and not player_rect.right >= Surface.width:
            player_rect = player_rect.move(player_speed, 0)
         
        if pressed_keys [K_LEFT]and not player_rect.left <= 0:
            player_rect = player_rect.move(-player_speed, 0)
            
        if scores >= max_score:
            if my_json.config.check(level, invisible_cursor) == False:
                my_json.config.write(level)
            game_work = False

        if ch == 0 and game_work != False:
            ch =+ 1
            
            invisible_cursor()
            #game_music.music_play()
            music.music_all(sound_game)
        
        main_surface_fps = GAME_TEXT.render(str(int(FPS.get_fps())), True, (RED))
        Surface.d.blit(main_surface_fps, (10, 10))
        tick_fps()
        update_display()
    
    game_work = True
    clean_bon_and_en()
    #game_music.music_stop()
    #music.music_play()
    music.music_all(sound_menu)
    standart_curs() 
    visible_cursor() 

def language_get(): 
    global work
    surfM = UI.SurfaceM(e, Surface.main_surface)
    s = 35

    def update_text():
        standart_text.set_language(Language.language)
        big_text.set_language(Language.language)
        text_change.set_language(Language.language)
         
    def exit():
        global work
        work = False
    
    button1 = b_l.copy()
    button1.set_button(-300, (220 + s*0), (300, 30))
    button1.moved(50, None, 300)
    
    button2 = b_l.copy()
    button2.set_button(-300, (220 + s*1), (300, 30))
    button2.moved(50, None, 300)

    button4 = b_s.copy()
    button4.set_button(-300, (220 + s*2 + 6), (300, 30))
    button4.moved(50, None, 300)

    def button_1():
        def button(): 
            button1.button({"language": "EN"}, Language.ENGLISH, clicks)
            update_text()

        button1.animation()
        button1.Button(50, (220 + s*0), (300, 30), button)
        button1.text_set(standart_text, 'English', 75, (221 + s*0), (0, 0, 0))

    def button_2():
        def button(): 
            button2.button({"language": "UA"}, Language.UKRAINIAN, clicks)
            update_text()

        button2.animation()
        button2.Button(50, (220 + s*1), (300, 30), button)
        button2.text_set(standart_text, 'Українська', 75, (221 + s*1), (0, 0, 0))

    def button_3():
        #surfM.Button(50, (220 + s*2), (300, 30), 75, (221 + s*2), 13, clicks, Русский, "Language", {"language": "RU"})
        Text.standart_text.draw_text('Русский', 75, (221 + s*2), (0, 0, 0))

    def button_4():
        def button(): 
            button4.button(return_exit, exit)

        button4.animation()
        button4.Button(50, (220 + s*2 + 6), (300, 30), button)
        button4.text_set(standart_text,"6", 75, (221 + s*2 + 6))
    

    set_fps(60)

    while work:     
        background()
        event_check_button(standart_curs, click_cursor)

        e.event_pool()
        e.K_ESCAPE(exit, return_exit)
        e.MOUSEBUTTONDOWN()
        
        button_1()
        button_2()
        button_4()    
        
        version_game()
        big_text.text("2", 70, 150)        
            
        tick_fps()
        update_display()

    work = True

def level():
    global work
    from clients.game_client import sw1, sh1, CREATE_ENEMY1, max_score1
    from clients.game_client import sw2, sh2, CREATE_ENEMY2, max_score2
    from clients.game_client import sw3, sh3, CREATE_ENEMY3, max_score3

    def exit():
        global work
        work = False
        
    button1 = b_s.copy()
    button1.set_button(-300, 220, (300, 30))
    button1.moved(50, None, 300) 
    
    button2 = b_s.copy()
    button2.set_button(-300, 255, (300, 30))
    button2.moved(50, None, 300) 

    button3 = b_s.copy()
    button3.set_button(-300, 290, (300, 30))
    button3.moved(50, None, 300) 

    button4 = b_s.copy()
    button4.set_button(-300, 330, (300, 30))
    button4.moved(50, None, 300) 

    def button_1():
        def lvl1(): 
            sourse(sw1, sh1, CREATE_ENEMY1, max_score1, {"level": 2}) 
        
        def button(): 
            button1.button(clicks, lvl1)
            set_fps(60)

        button1.animation()
        button1.Button(50, 220, (300, 30), button)    
        button1.text_set(standart_text,"3", 75, 222) 
     
    def button_2():   
        def l2():            
            def lvl2(): 
                sourse(sw2, sh2, CREATE_ENEMY2, max_score2, {"level": 3})
        
            my_json.config.check({"level": 2}, lvl2)

        def button(): 
            button2.button(clicks, l2)
            set_fps(60)

        button2.animation()
        button2.Button(50, 255, (300, 30), button)
        button2.text_set(standart_text, "4", 75, 256)
    
    def button_3():       
        def l3(): 
            def lvl3(): 
                sourse(sw3, sh3, CREATE_ENEMY3, max_score3, {"level": 3.1})
        
            my_json.config.check({"level": 3}, lvl3)
        
        def button(): 
            button3.button(clicks, l3)
            set_fps(60)

        button3.animation()
        button3.Button(50, 290, (300, 30), button)
        button3.text_set(standart_text, "5", 75, 291)
    
    def button_4():
        def button(): 
            button4.button(return_exit, exit)
        
        button4.animation()
        button4.Button(50, 330, (300, 30), button)
        button4.text_set(standart_text, "6", 75, 332)


    set_fps(60)

    while work:
        background()
        event_check_button(standart_curs, click_cursor)
        
        e.event_pool()
        e.K_ESCAPE(exit, return_exit)
        e.MOUSEBUTTONDOWN()

        button_1()
        button_2()
        button_3()
        button_4()
            
        version_game()
        big_text.text("11", 70, 150)
            
        tick_fps()
        update_display()

    work = True

if __name__ == "__main__":
    main_menu()