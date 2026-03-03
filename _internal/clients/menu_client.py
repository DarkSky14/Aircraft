#__all__ = []
__version__ = '0.1.0'
__author__ = 'Chinho'

import pygame
import os 
import json
import threading
import asyncio
#import screeni
from pygame import init

BLACK = ((0,0,0))
WHITE = ((255,255,255))
RED = (250, 0, 0)
GREEN = (0, 255, 0)
LIME = (100, 250, 100)

init()

BUTT_TEXT = pygame.font.SysFont('Georgia', 21, 0, 0) #Arial
NAME_MENU = pygame.font.SysFont('Georgia', 36)
VERS_GAME = pygame.font.SysFont('Segou UI', 20)
GAME_TEXT = pygame.font.SysFont("Consolas", 30)

width, height = 1373, 761
#width, height = pygame.display.get_window_size()
screen = width, height
main_surface = pygame.display.set_mode(screen, pygame.WINDOWMAXIMIZED)

error_lvl = ('Пройдіть попередній рівень')

list_1 = ({
    "level": 1, 
    "effect": "True", 
    "music": "True", 
    "language": "EN", 
    "musicID": "None"
})

file_check = ("_internal/library/data/config.json")
f_c = {}

click_open_2 = ('_internal/library/effect/click_open2.mp3')
click_open_1 = ('_internal/library/effect/click_open1.mp3')
click_exit = ('_internal/library/effect/click_exit1.mp3')
effect_game = ('_internal/library/effect/sound3.mp3')
sound_menu = ('_internal/library/music/Menu1 - peace.mp3')
sound_game = ('_internal/library/music/01897.mp3')


class Multi:
    def Thread(target, args, name):
        threa = threading.Thread(
            target = target,                                
            args = args,
            name = name
        )
        threa.start()
        threa.join()
    
    def asyncies(function):
        event_l = asyncio.get_event_loop()

        task = [
            event_l.create_task(function())
        ]
        return event_l, task

        tasks = asyncio.wait(task)
        event_l.run_until_complete(tasks)
        event_l.close()


class MusicConf:   
    def sound(address):
        try:
            address = pygame.mixer.Sound(address)
        except:
            return None
        else:
            return address  
    
    def create_channel(address, volume, loops=0, maxtime=0, fade_ms=0):
        try:
            address = pygame.mixer.Sound(address)
        except:
            return None
        else:
            volume = address.set_volume(volume)
            play = address.play(loops, maxtime, fade_ms)
            return play
    
    def create_mus_channel(address, volume, loops=-1, start=0, fade_ms=0):
        music = pygame.mixer_music
        try:
            music.load(address, "music")
        except:
            return None
        else:
            volume = music.set_volume(volume)
            play = music.play(loops, start, fade_ms)
            return play
    
    def stop_channel(address):
        try:
            sound = pygame.mixer.Sound(address)
        except:
            return None
        else:
            stop = sound.stop()
            return stop
    
    def music_all(name_track=sound_menu, volume=0.1, loops=-1, start=0, fade_ms=100):    
        arg = Passage11.search_value("musicID")
        #print("1 write {}".format(pygame.mixer_music.get_busy()))
        
        if Passage11.check(vie, {"music": "False"}) == True: 
            if pygame.mixer_music.get_busy() == True:
                pygame.mixer_music.pause()
                       
        else:               
            if pygame.mixer_music.get_busy() == False:
                if Passage11.check(vie, {"musicID": "None"}) == True:
                    Multi.Thread(MusicConf.create_mus_channel,(name_track, volume, loops, start, fade_ms), "MusicThread")
                    Passage11.writer_({"musicID": name_track})
                        
                else:
                    pygame.mixer_music.unpause()                
            
            elif pygame.mixer_music.get_busy() == True:
                if arg != name_track:
                    Multi.Thread(MusicConf.create_mus_channel,(name_track, volume, loops, start, fade_ms), "MusicThread")  
                    Passage11.writer_({"musicID": name_track})
                    
                                                                                    
class Passage11:
    def __init__(self):
        pass
    
    def search_value(argID):
        data = Passage11.__check__read__()
        return dict.get(data, argID)
    
    def check(script, args: dict):
        key = args.keys().__str__().lstrip("dict_keys").strip("([''])")
 
        key_dict = Passage11.search_value(key)

        try:
            assert args == {key: key_dict}
                
        except:
            return False
            
        else: 
            try:
                script()
            except:
                script
            return True       

    def __reader__():
        global file_check
        try: 
            with open(file_check,"r") as file:
                return json.load(file)
        except: 
            raise FileNotFoundError
    
    def __check__read__(hundred = None) -> dict:
        """
        This func open with starting game
        and save data in dict.
        """
        global f_c
        if hundred != None:
            f_c.update(hundred)
        
        else:
            if f_c == {}:
                try:
                    data = Passage11.__reader__()
                except FileNotFoundError: 
                    data = list_1
                    
                f_c.update(data)
                
                return f_c
            else:
                return f_c         
    
    def __key_value__(args: dict) -> dict:
        try:
            for data_key, data_value in args.items():
                return data_key, data_value
        except AttributeError as a: 
            print(a)
            return a
        except ReferenceError as r: 
            print(r)
            return r
        
    def __case__(data: dict, args: dict): 
        key = args.keys().__str__().lstrip("dict_keys").strip("([''])")
              
        key_dict = Passage11.search_value(key)
 
        try:
            assert args == {key: key_dict}
            
        except:
            data.update(args)
                    
        return data

    def writer_(args: dict):
        global file_check
        
        data = Passage11.__check__read__()
        
        for arg in args:
            data = Passage11.__case__(data, args)
            data.update(data)
              
        Passage11.__check__read__(data)
        try:
            with open(file_check,"w") as file: 
                json.dump(data, file, indent = 4) 
              
        except FileNotFoundError: 
            os.mkdir("_internal/library/data")          


def vie(): pass

#def effectGame_on(): musicConf.create_channel(effect_game, 0.1)
#def effectGame_off(): musicConf.stop_channel(effect_game)   
    
def clicks(): 
    MusicConf.create_channel(click_open_2, 0.01)

def return_exit(): 
    MusicConf.create_channel(click_exit, 0.01)

def version_game():
    main_surface.blit(
        VERS_GAME.render(
            str(__version__), True, BLACK), 
        (width - 33, 750)
    )

def scroll():
    MusicConf.create_channel(click_open_1, 0.01) 

def click_cursor(): 
    pygame.mouse.set_system_cursor(11)

def standart_curs():
    pygame.mouse.set_system_cursor(0)

def invisible_cursor():
    pygame.mouse.set_visible(0)

def visible_cursor():
    pygame.mouse.set_visible(1)

bg = pygame.transform.scale(pygame.image.load('_internal/library/pictures/background.png').convert(), screen)

bgX = 0
bgX2 = bg.get_width()  
bg_speed = 1
bg_speed1 = 2 


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    main_surface.blit(textobj, textrect)   
    return text
