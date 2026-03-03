import pygame
import screeninfo
import json
import os
if __name__ == "__main__":
    from language import * 
else:
    from clients.language import *

def vie(): pass

BLACK = ((0,0,0))


class _ClassSurface:
    def __init__(self, width: int = None, height: int = None):
        self.width = width
        self.height = height
        self.screen = self.width, self.height
    
    def set_main_surface(self) -> pygame.Surface:
        return pygame.display.set_mode(self.screen, pygame.WINDOWMAXIMIZED)
    
    def set_fullscreen(self) -> pygame.Surface:
        screen = screeninfo.get_monitors()
        for s in screen:
            self.width = s.width
            self.height = s.height
            self.screen = self.width, self.height
        return pygame.display.set_mode(self.screen, pygame.WINDOWMAXIMIZED)

    def subsurface(surface, left: float, top: float, width: float, height: float):
        return surface.subsurface((left, top, width, height))

    def set_subsurface(self, surface) -> pygame.Surface:
        if surface.get_width() - self.width <= 0:
            procent = (surface.get_width() / self.width)
            size_width = surface.get_width()
        procent_height = (self.height * procent)
        conf_height = (surface.get_height() - procent_height) / 2
        
        self.width = size_width
        self.procent_height = procent_height
        self.conf_height = conf_height

        return surface.subsurface(0, 0 + conf_height, size_width, procent_height + conf_height)

    def __get_procent_height__(self) -> float:
        return self.procent_height
    
    def __get_conf_height__(self) -> float:
        return self.conf_height

    def __get_size_surface__(self) -> tuple:
        return self.screen

    def __get_width__(self) -> int:
        return self.width

    def __get_height__(self) -> int:
        return self.height


s = _ClassSurface()
main_surface = s.set_fullscreen()
e = _ClassSurface(1373, 761)
d = e.set_subsurface(main_surface)

height = e.__get_height__()
width =  e.__get_width__()
screen = e.__get_size_surface__()
conf_height = e.__get_conf_height__()
procent_height = e.__get_procent_height__()


class _DLib:
    def __init__(self, name: str, url: str, dict: dict, file: str = None):
        self.name = name
        self.url = url
        self.dict = dict
        self.file = file

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_dict(self):
        return self.dict

    def get_file(self):
        return self.file

    def change_name(self, new_name: str):
        self.name = new_name

    def change_url(self, new_url: str):
        self.url = new_url

    def change_dict(self, new_dict: dict):
        self.dict = new_dict

    def change_file(self, new_file: str):
        self.file = new_file


class Passage(_DLib):
    def __init__(self, name: str, url: str, data: dict, file: str = None):
        _DLib.__init__(self, name, url, data, file)

    def search_value(self, argID: str):
        return dict.get(self.dict, argID)
    
    def check(self, script, args: dict):
        key = args.keys().__str__().lstrip("dict_keys").strip("([''])")
 
        key_dict = self.search_value(key)
        fi = {key: key_dict}
        #full = {"111": fi, "222": args}
        #print(full)

        if args != fi:
            return False
            
        else: 
            try:
                script()
            except:
                script
            return True       

    def __reader__(self):
        try: 
            with open((self.url + "/" + self.file),"r") as file:
                data = json.load(file)
                self.change_dict(data)
                return data
        except: 
            raise FileNotFoundError
    
    def __safe_reader__(self):
        try:
            self.__reader__()
        except FileNotFoundError:
            os.makedirs(self.url, exist_ok=True)
            self.writer_(self.dict)
        except json.JSONDecodeError:
            print("Error decoding JSON")

    def __key_value__(self, args: dict) -> dict:
        try:
            for data_key, data_value in args.items():
                return data_key, data_value
        except AttributeError as a: 
            print(a)
            return a
        except ReferenceError as r: 
            print(r)
            return r
        
    def __case__(self, args: dict):
        data = self.dict.copy()
        key = args.keys().__str__().lstrip("dict_keys").strip("([''])")
              
        key_dict = self.search_value(key)
 
        try:
            assert args == {key: key_dict}
            
        except:
            data.update(args)
                    
        return data

    def writer_(self, *args: dict):        
        for arg in args:
            new_data = self.__case__(arg)
              
        if new_data != self.dict:
            print({"LOG_PRINT": new_data})

            self.dict.update(new_data)
            os.makedirs(self.url, exist_ok=True)

            with open((self.url + "/" + self.file), "w") as file:
                json.dump(new_data, file, indent = 4) 
                  
            
config = Passage(
    "config",
    "library/data",
    {
        "level": 1, 
        "effect": "True", 
        "music": "True", 
        "language": "EN"
    },
    "config.json"
)
config.__safe_reader__()


temp = Passage(
    "temporary_options",
    "none",
    {"musicID": "None"}
)


print({"INITIALIAZE_CONFIG": config.get_dict()})


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
    
    def music_all(name_track, volume=0.1, loops=-1, start=0, fade_ms=100):    
        arg = temp.search_value("musicID")
 
        if temp.check(vie, {"music": "False"}) == True: 
            if pygame.mixer_music.get_busy() == True:
                pygame.mixer_music.pause()
                       
        else:               
            if pygame.mixer_music.get_busy() == False:
                if temp.check(vie, {"musicID": "None"}) == True:
                    MusicConf.create_mus_channel(name_track, volume, loops, start, fade_ms)
                    temp.change_dict({"musicID": name_track})

                else:
                    pygame.mixer_music.unpause()                
            
            elif pygame.mixer_music.get_busy() == True:
                if arg != name_track:
                    MusicConf.create_mus_channel(name_track, volume, loops, start, fade_ms)
                    temp.change_dict({"musicID": name_track})
      

class TextM:
    def __init__(self, font = True, color: tuple = BLACK, language = None):
        self.font = font
        self.color = color
        self.language = language

    def draw_text(self, text, color, surface, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)   
        return text

    def text_standart(self, num_text, x_text, y_text):
        self.draw_text(self.language[num_text], self.color, d, x_text, y_text)

    def Big_text(self, num_text=0, x_text = 80, y_text = 150):
        self.draw_text(self.language[num_text], self.color, d, x_text, y_text)

    def text_change(self, change, num_text, change_x, change_y, x_text, y_text):
        num_text = self.language[num_text]

        if config.check(vie, change) == True:
            number = self.language[change_x]

        elif config.check(vie, change) == False:
            number = self.language[change_y]
        self.draw_text("{} {}".format(num_text, number), self.color, d, x_text, y_text)
    
    def font_change(self, new_font):
        self.font = new_font
    
    def color_change(self, new_color: tuple):
        self.color = new_color

    def language_change(self, new_language):
        self.language = new_language
    
    def copy(self):
        return TextM(self.font, self.color, self.language)