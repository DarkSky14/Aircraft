import pygame
import random
from os import listdir

FPS = pygame.time.Clock()

IMGS_PATH = 'library/player'

CREATE_ENEMY1 = pygame.USEREVENT + 2
CREATE_ENEMY2 = pygame.USEREVENT + 2
CREATE_ENEMY3 = pygame.USEREVENT + 4
CHANGE_IMG = pygame.USEREVENT + 3
CREATE_BONUS = pygame.USEREVENT + 1


pygame.time.set_timer(CREATE_ENEMY1, 3500)
pygame.time.set_timer(CREATE_ENEMY2, 3000)
pygame.time.set_timer(CREATE_ENEMY3, 2000)
pygame.time.set_timer(CHANGE_IMG, 125)
pygame.time.set_timer(CREATE_BONUS, 2500)


width, height = 1373, 767
screen = width, height

pygame.init()

player_imgs = [pygame.image.load(IMGS_PATH + '/' + file).convert_alpha() for file in listdir(IMGS_PATH)]
player = player_imgs[0]
player_rect = player.get_rect()
player_speed = 2

img_index = 0
scores = 0 
bonusies = []
enemies = []

sw1, sh1 = 0, 3
sw2, sh2 = 1, 4
sw3, sh3 = 3, 7

max_score1=30
max_score2=300
max_score3=1500 

bg = pygame.transform.scale(pygame.image.load('library/pictures/background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()


enemy = pygame.image.load('library/pictures/enemy.png')
def create_enemy(speed_w1, speed_w2):
    global enemy
    enemy_rect = pygame.Rect(width, random.randint(0,height), *enemy.get_size())
    enemy_speed = random.randint(speed_w1, speed_w2)
    return[enemy, enemy_rect, enemy_speed]


bonus = pygame.image.load('library/pictures/bonus.jpg ')
def create_bonus():
    global bonus
    bonus_rect = pygame.Rect(random.randint(0, width), -1000, *bonus.get_size())    
    bonus_speed = (0)
    return [bonus, bonus_rect, bonus_speed]


def clean_bon_and_en():
    """Delete all bonusies and enemies"""
    enemies.clear()
    bonusies.clear()

fps = 0

def set_fps(tick = None):
    global fps
    if tick == None:
        #fps = fps
        return fps
    else:
        fps = tick
        return fps

def tick_fps():
    global fps
    FPS.tick(fps)