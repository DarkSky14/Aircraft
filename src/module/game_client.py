import pygame
from random import randint
from os import listdir

#if __name__ == "__main__":    
from module import procent, width, height, log, fix_import, d, BASE_FONT
    #else:
    #from clients.module import procent, width, height, log, fix_import, d, BASE_FONT

FPS = pygame.time.Clock()

IMGS_PATH = fix_import + 'library/player'

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

log.info("Start load player images...")
player_img = [pygame.image.load(IMGS_PATH + '/' + file).convert_alpha() for file in listdir(IMGS_PATH)]
player_imgs = [pygame.transform.scale(player_img, ((player_img.get_width() * procent), (player_img.get_height() * procent))) for player_img in player_img]
log.info("Player images successfully load.")
player = player_imgs[0]
player_rect = player.get_rect()
player_speed = 2


sw1, sh1 = 0, 3
sw2, sh2 = 1, 4
sw3, sh3 = 3, 7

max_score1=30
max_score2=300
max_score3=1500 


log.info("Start load enemy image...")
enemy_png = pygame.image.load(fix_import + 'library/pictures/enemy.png')
enemy = pygame.transform.scale(enemy_png, ((enemy_png.get_width() * procent), (enemy_png.get_height() * procent)))
def create_enemy(speed_w1, speed_w2):
    global enemy
    enemy_rect = pygame.Rect(width, randint(0, int(height)), *enemy.get_size())
    enemy_speed = randint(speed_w1, speed_w2)
    return[enemy, enemy_rect, enemy_speed]
log.info("Enemy image successfully loaded.")


log.info("Start load bonus image...")
bonus_jpg = pygame.image.load(fix_import + 'library/pictures/bonus.jpg ')
bonus = pygame.transform.scale(bonus_jpg, ((bonus_jpg.get_width() * procent), (bonus_jpg.get_height() * procent)))
def create_bonus():
    global bonus
    bonus_rect = pygame.Rect(randint(0, int(width)), -1000, *bonus.get_size())    
    bonus_speed = (0)
    return [bonus, bonus_rect, bonus_speed]
log.info("Bonus image successfully loaded.")

fps = 0

def set_fps(tick = None):
    global fps
    if tick == None:
        return fps
    else:
        fps = tick
        return fps

def tick_fps():
    global fps
    FPS.tick(fps)

def get_fps(font: pygame.font.Font = BASE_FONT, color: tuple = (200, 200, 200), coordinate: tuple = (3,3)):
    main_surface_fps = font.render(str(int(FPS.get_fps())), True, (color))
    rect_obgect = main_surface_fps.get_rect()
    rect_obgect.topleft = coordinate
    d.blit(main_surface_fps, rect_obgect)