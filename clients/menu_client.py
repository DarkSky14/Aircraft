__version__ = '0.2.5'
__author__ = 'Chinho'

import pygame.font
from pygame import init
import clients.module.music as mus
if __name__ == "__main__":    
    import clients.module.Surface as Surface
else:
    import clients.module.Surface as Surface

def get_version():
    return __version__

def get_author():
    return __author__

BLACK = ((0,0,0))
WHITE = ((255,255,255))
RED = (250, 0, 0)
GREEN = (0, 255, 0)
LIME = (100, 250, 100)

init()

def vie(): 
    pass

STANDART_TEXT = pygame.font.SysFont('Georgia', round(21 * Surface.procent), 0, 0) #Arial
BIG_TEXT = pygame.font.SysFont('Georgia', round(36 * Surface.procent))
VERS_GAME = pygame.font.SysFont('Segou UI', round(20 * Surface.procent))
GAME_TEXT = pygame.font.SysFont("Consolas", round(30 * Surface.procent))

click_open_2 = ('library/effect/click_open2.mp3')
click_open_1 = ('library/effect/click_open1.mp3')
click_exit = ('library/effect/click_exit1.mp3')
effect_game = ('library/effect/sound3.mp3')
click_aim = ("library/effect/nice click aim.mp3")
sound_menu = ('library/music/Menu1 - peace.mp3')
sound_game = ('library/music/01897.mp3')

def click_cursor(): 
    pygame.mouse.set_system_cursor(11)

def standart_curs():
    pygame.mouse.set_system_cursor(0)

def invisible_cursor():
    pygame.mouse.set_visible(0)

def visible_cursor():
    pygame.mouse.set_visible(1)

def clicks(): 
    mus.Sound().create_channel(click_open_2)

def return_exit(): 
    mus.Sound().create_channel(click_exit)

def scroll():
    mus.Sound().create_channel(click_aim, 0.05) 

bg = pygame.transform.scale(pygame.image.load('library/pictures/background.png').convert(), Surface.screen)
bgX = 0
bgX2 = bg.get_width()  
bg_speed = 1
bg_speed1 = 2 

def version_game():
    Surface.d.blit(
        VERS_GAME.render(str(get_version()), True, BLACK), 
        (Surface.width - (33 * Surface.procent), Surface.height - (14 * Surface.procent))
    )
