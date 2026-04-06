from module import (
    ScrollingBG, music, config, GAME_TEXT, bg, update_display, d, log,
    height, width, BASE_FONT, version_game, standart_curs,
    sound_game, sound_menu, BLACK, RED, invisible_cursor, visible_cursor,
    fix_import, procent, set_fps, get_fps, tick_fps, GLOBAL_EVENT
)

import module

from pygame import (
    QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_ESCAPE, KEYDOWN, event, key,
    USEREVENT, time, image, transform, Rect
)

from options import options
from random import randint
from os import listdir

_bg_speed_ = 2

IMGS_PATH = fix_import + "library/player"

log.info("Start load player images...")
player_img = [
    image.load(IMGS_PATH + "/" + file).convert_alpha()
    for file in listdir(IMGS_PATH)
]
player_imgs = [
    transform.scale(
        player_img,
        ((player_img.get_width() * procent), (player_img.get_height() * procent)),
    )
    for player_img in player_img
]
log.info("Player images successfully load.")
player = player_imgs[0]
player_rect = player.get_rect()
player_speed = 2


log.info("Start load enemy image...")
_enemy_png = image.load(fix_import + "library/pictures/enemy.png")
_enemy = transform.scale(
    _enemy_png, ((_enemy_png.get_width() * procent), (_enemy_png.get_height() * procent))
)
def _create_enemy(speed_w1, speed_w2):
    global _enemy
    enemy_rect = Rect(width, randint(0, int(height)), *_enemy.get_size())
    enemy_speed = randint(speed_w1, speed_w2)
    return [_enemy, enemy_rect, enemy_speed]
log.info("Enemy image successfully loaded.")


log.info("Start load bonus image...")
_bonus_jpg = image.load(fix_import + "library/pictures/bonus.jpg ")
_bonus = transform.scale(
    _bonus_jpg, ((_bonus_jpg.get_width() * procent), (_bonus_jpg.get_height() * procent))
)
def _create_bonus():
    global _bonus
    bonus_rect = Rect(randint(0, int(width)), -1000, *_bonus.get_size())
    bonus_speed = 0
    return [_bonus, bonus_rect, bonus_speed]
log.info("Bonus image successfully loaded.")


def sourse(
        speed_w1, speed_w2, ENEMY, max_score, level={str: int}, 
        CHANGE_IMG = (USEREVENT + 3), CREATE_BONUS = (USEREVENT + 1),
        ENEMY_TIMER = 3500
    ):
    global game_work, work, player, player_rect, player_imgs, player_speed
    global GLOBAL_EVENT

    fon_background = ScrollingBG(bg, _bg_speed_)

    def background():
        fon_background.update()
        fon_background.draw(d)

    set_fps(90)

    img_index = 0
    scores = 0
    bonusies = []
    enemies = []

    last_score_render = -1
    score_text_cache = BASE_FONT.render("0", True, BLACK)

    time.set_timer(ENEMY, ENEMY_TIMER)
    time.set_timer(CHANGE_IMG, 125)
    time.set_timer(CREATE_BONUS, 2500)

    def clean_bon_and_en():
        """Delete all bonusies and enemies"""
        bonusies.clear()
        enemies.clear()

    check_first_while = 0
    module.game_work = True

    while module.game_work:
        pressed_keys = key.get_pressed()
        for event_ in event.get():
            if event_.type == QUIT:
                quit()
                exit()
            if event_.type == KEYDOWN:
                if event_.key == K_ESCAPE:
                    check_first_while = 0
                    music.music_pause()
                    music.music_load(sound_menu)
                    work = True
                    options()

            if event_.type == CREATE_BONUS:
                bonusies.append(_create_bonus())

            if event_.type == ENEMY:
                enemies.append(_create_enemy(speed_w1, speed_w2))

            if event_.type == CHANGE_IMG:
                img_index += 1
                if img_index == len(player_imgs):
                    img_index = 0
                player = player_imgs[img_index]

        background()

        d.blit(player, (player_rect))

        enemies_to_keep = []
        for enemy in enemies:
            enemy[1].x -= enemy[2]
            d.blit(enemy[0], enemy[1])

            if enemy[1].left >= -200: 
                if player_rect.colliderect(enemy[1]):
                    module.game_work = False
                    music.music_pause()
                    music.music_load(sound_menu)
                else:
                    enemies_to_keep.append(enemy)
        enemies.clear()
        enemies.extend(enemies_to_keep)

        bonuses_to_keep = []
        for bonus in bonusies:
            bonus[1].x -= bonus[2]
            bonus[1].y += 2
            d.blit(bonus[0], bonus[1])

            if bonus[1].bottom <= (height + 300):  # Keep if visible
                if player_rect.colliderect(bonus[1]):
                    scores += 1
                else:
                    bonuses_to_keep.append(bonus)
        bonusies.clear()
        bonusies.extend(bonuses_to_keep)

        if pressed_keys[K_DOWN] and not player_rect.bottom >= height:
            player_rect.y += player_speed

        if pressed_keys[K_UP] and not player_rect.top <= 0:
            player_rect.y -= player_speed

        if pressed_keys[K_RIGHT] and not player_rect.right >= width:
            player_rect.x += player_speed

        if pressed_keys[K_LEFT] and not player_rect.left <= 0:
            player_rect.x -= player_speed

        if scores >= max_score:
            if not config.check(level, invisible_cursor):
                config.write(level)
            module.game_work = False

        if check_first_while == 0 and module.game_work:
            check_first_while =+ 1

            invisible_cursor()
            music.music_load(sound_game)
            music.music_unpause()

        if scores != last_score_render:
            score_text_cache = BASE_FONT.render(str(scores), True, BLACK)
            last_score_render = scores

        d.blit(score_text_cache, (d.get_width() - 30, 0))
        version_game()
        get_fps(GAME_TEXT, RED, (10, 10))
        tick_fps()
        update_display()

    module.game_work = True
    clean_bon_and_en()
    music.set_position()
    music.music_all(sound_menu)
    standart_curs()
    visible_cursor()


if __name__ == "__main__":
    sourse(1, 3, USEREVENT + 2, 30, {"level": 2})
