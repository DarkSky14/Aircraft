import sys
from pygame import (
    QUIT, K_DOWN, K_UP, 
    K_RIGHT, K_LEFT, K_ESCAPE,
    MOUSEBUTTONDOWN, KEYDOWN
)

from clients.menu_client import *
from clients.game_client import * 
from clients._lib_ import (
    Passage, config, vie, conf_height, TextM,
    MusicConf, main_surface, d, width, height, screen,
    English, Українська, Русский
)


# Setup pygame/window -----------------------------
icon = pygame.transform.scale(pygame.image.load('library/Aircraft.ico').convert(),screen)
fon = pygame.image.load('library/pictures/fon_.png').convert()

pygame.display.set_caption('Aircraft',"Aircraft")
pygame.display.set_icon(icon) 
pygame.init()

font = pygame.font.SysFont("Calibri", 20)

work = True
game_work = True

def background():
    global bgX, bgX2
        
    if bgX < -bg.get_width():
        bgX = bg.get_width()
            
    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()
        
    bgX -= bg_speed
    bgX2 -= bg_speed
        
    
    d.blit(bg, (bgX, 0))
    d.blit(bg, (bgX2, 0))    
   
def background1():
   d.blit(bg, (0, 0))


class SurfaceM(): 
    def __init__(self, s):
        pass
    
    def quit(self, effect_click=None):
        global work
        click = False
        self.click = click
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    work = False
                    config.check(effect_click, {"effect": "True"})
                    return work
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def surface_wait(self, x_c, y_c):
        global work
        sub_surface = pygame.Rect(((x_c - 25), (y_c - 90)), (350, 250))

        mx, my = pygame.mouse.get_pos()
        pygame.draw.rect(d, (100, 100, 100), sub_surface, 300,10,50,50,50,50)

        if self.click:
            if sub_surface.collidepoint((mx, my)) == False:
                work = False      
            else:
                None  
      
    def Button(self, x, y, size, function1, effect_click, check = "None", text=0):      
        global language, work, game_work
        mx, my = pygame.mouse.get_pos() 
        button = pygame.Rect((x, y + conf_height), (size))
                 
        if button.collidepoint((mx, my)) == True:
            if self.click:
                if check == "Check": 
                    config.check(effect_click, {"effect": "True"})
                    if config.check(None, text[0]) == True:                      
                        config.writer_(text[1])
                        function1()  
                    elif config.check(None, text[1]) == True:                       
                        config.writer_(text[0])
                        function1()
                        
                elif check == "None": 
                    work = True
                    game_work = True          
                    config.check(effect_click, {"effect": "True"})
                    function1()            
            
                elif check == "Language":
                    config.check(effect_click, {"effect": "True"})
                    if config.check(vie, text) == False:
                        config.writer_(text)
                        language = function1
                        standart_text.language_change(language)
                        big_text.language_change(language)
                    else: None
            
            click_cursor()        
            pygame.draw.rect(main_surface, (205, 200, 200), button, 15, 10, 50, 50, 50, 50)

        pygame.draw.rect(main_surface, (205, 200, 200), button, 3, 10, 50, 50, 50, 50)


class Button:
    pass

       
def language_get(): 
    surfM = SurfaceM("si")
    s = 35
         
    def exit():
        global work
        work = False
        
    def button_1():
        surfM.Button(50, (220 + s*0), (300, 30), English, clicks, "Language", {"language": "EN"})
        standart_text.draw_text('English', (0, 0, 0), d, 75, (221 + s*0))
    
    def button_2():
        surfM.Button(50, (220 + s*1), (300, 30), Українська, clicks, "Language", {"language": "UA"})
        standart_text.draw_text('Українська', (0, 0, 0), d, 75, (221 + s*1))

    def button_3():
        surfM.Button(50, (220 + s*2), (300, 30), 75, (221 + s*2), 13, clicks, Русский, "Language", {"language": "RU"})
        standart_text.draw_text('Русский', (0, 0, 0), d, 75, (221 + s*2))

    def button_4():
        surfM.Button(50, (220 + s*2 + 6), (300, 30), exit, return_exit)
        standart_text.text_standart(6, 75, (221 + s*2 + 6))
    
    while work:     
        background()
        surfM.quit(return_exit)
        standart_curs()
        
        button_1()
        button_2()
        #button_3()
        button_4()    
        
        version_game()
        big_text.Big_text(2)        
            
        FPS.tick(90)
        pygame.display.update()

def level():
    from clients.game_client import sw1, sh1, CREATE_ENEMY1, max_score1
    from clients.game_client import sw2, sh2, CREATE_ENEMY2, max_score2
    from clients.game_client import sw3, sh3, CREATE_ENEMY3, max_score3
    
    surfM = SurfaceM("si")

    def exit():
        global work
        work = False
            
    def button_1():
        def lvl1(): 
            sourse(sw1, sh1, CREATE_ENEMY1, max_score1, {"level": 2}) 
        
        surfM.Button(50, 220, (300, 30), lvl1, clicks)    
        standart_text.text_standart(3, 75, 222) 
     
    def button_2():   
        def l2():            
            def lvl2(): 
                sourse(sw2, sh2, CREATE_ENEMY2, max_score2, {"level": 3})
        
            config.check(lvl2, {"level": 2})

        surfM.Button(50, 255, (300, 30), l2, clicks)
        standart_text.text_standart(4, 75, 256)
    
    def button_3():       
        def l3(): 
            def lvl3(): 
                sourse(sw3, sh3, CREATE_ENEMY3, max_score3, {"level": 3.1})
        
            config.check(lvl3, {"level": 3})

        surfM.Button(50, 290, (300, 30), l3, clicks)
        standart_text.text_standart(5, 75, 291)
    
    def button_4():
        surfM.Button(50, 330, (300, 30), exit, return_exit)
        standart_text.text_standart(6, 75, 332)

    while work:
        background()
        surfM.quit(return_exit)
        standart_curs()

        button_1()
        button_2()
        button_3()
        button_4()
            
        version_game()
        big_text.Big_text(11)
            
        FPS.tick(90)
        pygame.display.update()

def sourse(speed_w1, speed_w2, ENEMY, max_score, level=None):                   
    from clients.game_client import scores,player_imgs,player_speed,bgX
    from clients.game_client import player,player_rect,img_index,bgX2
    global game_work, work
    
    ch = 0  
    pygame.init()

    while game_work:
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    work = True
                    ch = 0
                    options()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clic = True
            
            if event.type == CREATE_BONUS:
                bonusies.append(create_bonus())
            
            if event.type == ENEMY:
                enemies.append(create_enemy(speed_w1, speed_w2))
            
            if event.type == CHANGE_IMG:
                img_index += 1
                if img_index == len(player_imgs):
                    img_index = 0
                player = player_imgs[img_index]
         
        bgX -= bg_speed1
        if bgX < -bg.get_width():
            bgX = bg.get_width()
        bgX2 -= bg_speed1      
        if bgX2 < -bg.get_width():
            bgX2 = bg.get_width()

        d.blit(bg, (bgX, 0))
        d.blit(bg, (bgX2, 0))
        d.blit(font.render(str(scores), True, BLACK), (width - 30, 0))
        d.blit(player, (player_rect))
        version_game()
        
        for enemy in enemies:
            enemy[1] = enemy[1].move(-enemy[2], 0)
            d.blit(enemy[0], enemy[1])
        
            if enemy[1].left < -200:
                enemies.pop(enemies.index(enemy))

            if player_rect.colliderect(enemy[1]):
                game_work = False
        
        for bonus in bonusies:             
            bonus[1] = bonus[1].move(-bonus[2], 2)
            d.blit(bonus[0], bonus[1])
        
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
        
        if pressed_keys [K_DOWN] and not player_rect.bottom >= height:
            player_rect = player_rect.move(0, player_speed)
        
        if pressed_keys [K_UP] and not player_rect.top <= 0:
            player_rect = player_rect.move(0, -player_speed)
          
        if pressed_keys [K_RIGHT] and not player_rect.right >= width:
            player_rect = player_rect.move(player_speed, 0)
         
        if pressed_keys [K_LEFT]and not player_rect.left <= 0:
            player_rect = player_rect.move(-player_speed, 0)
            
        if scores >= max_score:
            if Passage.check(invisible_cursor, level) == False:
                Passage.writer_(level)
            game_work = False

        if ch == 0 and game_work != False:
            ch =+ 1
            
            invisible_cursor()
            MusicConf.music_all(sound_game)
        
        main_surface_fps = GAME_TEXT.render(str(int(FPS.get_fps())), 10, (RED))
        d.blit(main_surface_fps, (10, 10))
        FPS.tick(90)
        pygame.display.update()
    
    clean_bon_and_en()
    MusicConf.music_all(sound_menu)
    standart_curs() 
    visible_cursor() 

def main_menu():
    work = True    
    surfM = SurfaceM("si")

    def exit():     
        pygame.quit()
        sys.exit()
            
    def opti():
        options(50,240)  
        
    def button_1():
        surfM.Button(50, 220, (300, 30), level, clicks)
        standart_text.text_standart(0, 75, 222)
    
    def button_2():
        surfM.Button(50, 255, (300, 30), opti, clicks)
        standart_text.text_standart(1, 75, 256)
    
    def button_3():
        surfM.Button(50, 290, (300, 30), language_get, clicks)
        standart_text.text_standart(2, 75, 291)
    
    def button_4():
        surfM.Button(50, 360, (300, 30), exit, return_exit)
        standart_text.text_standart(6, 75, 361)
    
    while work:       
        background() 
        version_game() 
        standart_curs()
        surfM.quit(vie)
        
        button_1() 
        button_2() 
        button_3()   
        button_4() 
        
        big_text.Big_text(7)
        

        FPS.tick(90)
        pygame.display.flip()

def options(x_c = 540, y_c = 347.5):
    global width   
    surfM = SurfaceM("si")

    def quit():
        global work
        work = False
        st = 0
        return st
        
    def exit():
        global game_work 
        clean_bon_and_en() 
        game_work = False  
        quit()
    
    version_game()
    MusicConf.music_all(sound_menu)
    visible_cursor()  
    
    def button_1():
        surfM.Button(x_c, y_c, (300, 30), vie, clicks, "Check", ({"effect": "True"}, {"effect": "False"}))
        standart_text.text_change({"effect": "True"}, 12, 8, 9, (x_c + 25), (y_c - 0.5))
            
    def button_2():
        surfM.Button(x_c, (y_c + 35), (300, 30), MusicConf.music_all, MusicConf.music_all, "Check", ({"music": "True"},{"music": "False"}))
        standart_text.text_change({"music": "True"}, 10, 8, 9, (x_c + 25), (y_c + 34.5))

    def button_3():
        surfM.Button(x_c, (y_c + 81), (300, 30), exit, return_exit)
        standart_text.text_standart(6, (x_c + 20), (y_c + 80.5))
    
    fon.set_alpha(150)
    main_surface.blit(fon, (0, 0 + conf_height))
    
    while work:
        surfM.quit()
        standart_curs()
        surfM.surface_wait(x_c, y_c)
        
        button_1()
        button_2() 
        button_3()
        
        big_text.Big_text(1, (x_c + 20), (y_c - 60))
        
        FPS.tick(90)
        pygame.display.flip()

def language_set(*kwargs: dict):
    language = English
    
    for kwar in kwargs:
        data_key, data_value = config.__key_value__(kwar)
        check = {"language": data_key}
        if config.check(vie, check) == True: 
            language = data_value
            return language
        else:
            continue

    return language

language = language_set({"EN": English}, {"UA": Українська})#, {"RU": Русский})

text = TextM(language=language)
big_text = text.copy()
big_text.font_change(BIG_TEXT)
standart_text = text.copy()
standart_text.font_change(STANDART_TEXT)

MusicConf.music_all(sound_menu)
main_menu()