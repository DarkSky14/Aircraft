__version__ = '0.1.1'
__author__ = 'Chinho'

import pygame
from pygame import init

if __name__ == '__main__':
    from _lib_ import MusicConf, d, width, screen, height
else:
    from clients._lib_ import MusicConf, d, width, screen, height


BLACK = ((0,0,0))
WHITE = ((255,255,255))
RED = (250, 0, 0)
GREEN = (0, 255, 0)
LIME = (100, 250, 100)

init()

STANDART_TEXT = pygame.font.SysFont('Georgia', 21, 0, 0) #Arial
BIG_TEXT = pygame.font.SysFont('Georgia', 36)
VERS_GAME = pygame.font.SysFont('Segou UI', 20)
GAME_TEXT = pygame.font.SysFont("Consolas", 30)

click_open_2 = ('library/effect/click_open2.mp3')
click_open_1 = ('library/effect/click_open1.mp3')
click_exit = ('library/effect/click_exit1.mp3')
effect_game = ('library/effect/sound3.mp3')
sound_menu = ('library/music/Menu1 - peace.mp3')
sound_game = ('library/music/01897.mp3')

def clicks(): 
    MusicConf.create_channel(click_open_2, 0.01)

def return_exit(): 
    MusicConf.create_channel(click_exit, 0.01)

def version_game():
    d.blit(VERS_GAME.render(str(__version__), True, BLACK), (width - 33, height - 11))

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

bg = pygame.transform.scale(pygame.image.load('library/pictures/background.png').convert(), screen)

bgX = 0
bgX2 = bg.get_width()  
bg_speed = 1
bg_speed1 = 2 