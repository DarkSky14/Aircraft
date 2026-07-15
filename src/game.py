import pygame
from module import (
    ScrollingBG, log, absolute_import, boot
)
import module

from pygame import (
    QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_ESCAPE, KEYDOWN, event, key,
    USEREVENT, time, image, transform, Rect
)

from options import options
from random import randint
from os import listdir

#boot = module
_bg_speed_ = 2 * boot.procent
_game_work = True

IMGS_PATH = absolute_import("player")

log.info("Start load player images...")
_player_img = [
    image.load(IMGS_PATH + "/" + file).convert_alpha()
    for file in listdir(IMGS_PATH)
]
_player_imgs = [
    transform.scale(
        player_img,
        ((player_img.get_width() * boot.procent), (player_img.get_height() * boot.procent)),
    )
    for player_img in _player_img
]
log.info("Player images successfully load.")
_player = _player_imgs[0]
_player_rect = _player.get_rect()
_player_speed = 2.5 * boot.procent


log.info("Start load enemy image...")
_enemy_png = image.load(absolute_import("pictures/enemy.png"))
_enemy = transform.scale(
    _enemy_png, ((_enemy_png.get_width() * boot.procent), (_enemy_png.get_height() * boot.procent))
)
def _create_enemy(speed_w1, speed_w2):
    global _enemy
    enemy_rect = Rect(boot.width, randint(0, int(boot.height)), *_enemy.get_size())
    enemy_speed = randint(speed_w1, speed_w2)
    return [_enemy, enemy_rect, enemy_speed]
log.info("Enemy image successfully loaded.")


log.info("Start load bonus image...")
_bonus_jpg = image.load(absolute_import("pictures/bonus.jpg"))
_bonus = transform.scale(
    _bonus_jpg, ((_bonus_jpg.get_width() * boot.procent), (_bonus_jpg.get_height() * boot.procent))
)
def _create_bonus():
    global _bonus
    bonus_rect = Rect(randint(0, int(boot.width)), -1000, *_bonus.get_size())
    bonus_speed = 0
    return [_bonus, bonus_rect, bonus_speed]
log.info("Bonus image successfully loaded.")


def source(
        speed_w1, speed_w2, enemy_spawn, max_score, level: dict,
        change_img = (USEREVENT + 3), create_bonus = (USEREVENT + 1),
        enemy_timer_spawn = 3500
    ):
    global _game_work,  _player, _player_rect, _player_imgs, _player_speed

    fon_background = ScrollingBG(boot.bg, _bg_speed_)

    def background():
        fon_background.update()
        fon_background.draw(boot.d)

    boot.set_fps(90)

    img_index = 0
    scores = 0
    bonuses = []
    enemies = []

    last_score_render = -1
    score_text_cache = boot.BASE_FONT.render_font().render("0", True, boot.BLACK)

    time.set_timer(enemy_spawn, enemy_timer_spawn)
    time.set_timer(change_img, 125)
    time.set_timer(create_bonus, 2500)

    def clean_bon_and_en():
        """Delete all bonuses and enemies"""
        bonuses.clear()
        enemies.clear()

    check_first_while = 0

    while _game_work:
        pressed_keys = key.get_pressed()
        for event_ in event.get():
            if event_.type == QUIT:
                quit()
            if event_.type == KEYDOWN:
                if event_.key == K_ESCAPE:
                    check_first_while = 0
                    boot.music.music_pause()
                    boot.music.music_load(boot.sound_menu)
                    _game_work = options()

            if event_.type == create_bonus:
                bonuses.append(_create_bonus())

            if event_.type == enemy_spawn:
                enemies.append(_create_enemy(speed_w1, speed_w2))

            if event_.type == change_img:
                img_index += 1
                if img_index == len(_player_imgs):
                    img_index = 0
                _player = _player_imgs[img_index]

        background()

        boot.d.blit(_player, _player_rect)

        enemies_to_keep = []
        for enemy in enemies:
            enemy[1].x -= enemy[2]
            boot.d.blit(enemy[0], enemy[1])

            if enemy[1].left >= -200: 
                if _player_rect.colliderect(enemy[1]):
                    _game_work = False
                    boot.music.music_pause()
                    boot.music.music_load(boot.sound_menu)
                else:
                    enemies_to_keep.append(enemy)
        enemies.clear()
        enemies.extend(enemies_to_keep)

        bonuses_to_keep = []
        for bonus in bonuses:
            bonus[1].x -= bonus[2]
            bonus[1].y += 2
            boot.d.blit(bonus[0], bonus[1])

            if bonus[1].bottom <= (boot.height + 300):  # Keep if visible
                if _player_rect.colliderect(bonus[1]):
                    scores += 1
                else:
                    bonuses_to_keep.append(bonus)
        bonuses.clear()
        bonuses.extend(bonuses_to_keep)

        if pressed_keys[K_DOWN] and not _player_rect.bottom >= boot.height:
            _player_rect.y += _player_speed

        if pressed_keys[K_UP] and not _player_rect.top <= 0:
            _player_rect.y -= _player_speed

        if pressed_keys[K_RIGHT] and not _player_rect.right >= boot.width:
            _player_rect.x += _player_speed

        if pressed_keys[K_LEFT] and not _player_rect.left <= 0:
            _player_rect.x -= _player_speed

        if scores >= max_score:
            if not boot.config.check(level, boot.invisible_cursor):
                boot.config.write(level)
            _game_work = False

        if check_first_while == 0 and _game_work:
            check_first_while =+ 1

            boot.invisible_cursor()
            boot.music.music_load(boot.sound_game)
            boot.music.music_unpause()

        if scores != last_score_render:
            score_text_cache = boot.BASE_FONT.render_font().render(str(scores), True, boot.BLACK)
            last_score_render = scores

        boot.d.blit(score_text_cache, (boot.d.get_width() - 30, 0))
        boot.version_game()
        boot.get_fps(boot.GAME_TEXT, boot.RED, (10, 10))
        boot.tick_fps()
        boot.update_display()

    _game_work = True
    clean_bon_and_en()
    boot.music.set_position()
    boot.music.music_all(boot.sound_menu)
    boot.standard_curs()
    boot.visible_cursor()


if __name__ == "__main__":
    source(1, 3, USEREVENT + 2, 30, {"level": 1})
