import sys
sys.path.append("..")

from module import (
    ScrollingBG, log, url_fixer, py, sys, ImageLoader
)

from random import randint
from os import listdir
from menu.settings_menu import options, canvas_conf
from cached.bootstrap import boot


_bg_speed_ = 0.0015 * boot.width
_game_work = True

IMGS_PATH = url_fixer("player")

log.info("Start load player images...")
_player_img = [
    py.image.load(IMGS_PATH + "/" + file).convert_alpha()
    for file in sorted(listdir(IMGS_PATH))
]
_player_imgs = [
    py.transform.scale(
        player_img,
        ((player_img.get_width() * boot.procent), (player_img.get_height() * boot.procent)),
    )
    for player_img in _player_img
]
CHANGED_IMG = boot.GLOBAL_EVENT.custom_type()
log.info("Player images successfully load.")
_player = _player_imgs[0]
_player_rect = _player.get_rect()
_player_speed = 0.0018 * boot.width


_enemy = ImageLoader("pictures/enemy.png", ((0.0677 * boot.width), (0.0329 * boot.height)))
def _create_enemy(speed_w1, speed_w2):
    global _enemy
    enemy_rect = py.Rect(boot.width, randint(0, int(boot.height)), *_enemy.get_size())
    enemy_speed = randint(speed_w1, speed_w2)
    return [_enemy.show(), enemy_rect, enemy_speed]
ENEMY_EVENT = boot.GLOBAL_EVENT.custom_type()


_bonus = ImageLoader("pictures/bonus.jpg", (0.031* boot.width,0.0565* boot.height))
def _create_bonus():
    global _bonus
    bonus_rect = py.Rect(randint(0, int(boot.width)), -1000, *_bonus.get_size())
    bonus_speed = 0
    return [_bonus.show(), bonus_rect, bonus_speed]
BONUS_EVENT = boot.GLOBAL_EVENT.custom_type()


def source(
        speed_w1, speed_w2, enemy_spawn, max_score, level: dict,
        change_img = CHANGED_IMG, create_bonus = BONUS_EVENT,
        enemy_timer_spawn = 3500
    ):
    global _game_work, _player, _player_rect, _player_imgs, _player_speed

    fon_background = ScrollingBG(boot.bg, _bg_speed_)

    boot.GLOBAL_EVENT.mouse.event_button_check(
        boot.standard_curs, boot.click_cursor, boot.sound_scroll
    )

    def background():
        fon_background.update()
        fon_background.draw(boot.main_surface)

    boot.set_fps(90)

    img_index = 0
    scores = 0
    bonuses = []
    enemies = []

    last_score_render = -1
    score_text_cache = boot.BASE_FONT.render_font().render("0", True, boot.BLACK)

    py.time.set_timer(enemy_spawn, enemy_timer_spawn)
    py.time.set_timer(change_img, 125)
    py.time.set_timer(create_bonus, 2500)

    def clean_bon_and_en():
        """Delete all bonuses and enemies"""
        bonuses.clear()
        enemies.clear()

    settings_open = False
    #canvas_conf.set_x(0.390), canvas_conf.set_y(0.336)

    while _game_work:
        pressed_keys = py.key.get_pressed()
        for event_ in boot.GLOBAL_EVENT.event_pool():
            if event_.type == py.QUIT:
                py.quit()
                sys.exit()
            if event_.type == py.KEYDOWN:
                if event_.key == py.K_ESCAPE:
                    settings_open = False
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

        boot.main_surface.blit(_player, _player_rect)

        enemies_to_keep = []
        for enemy in enemies:
            enemy[1].x -= enemy[2]
            boot.main_surface.blit(enemy[0], enemy[1])

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
            boot.main_surface.blit(bonus[0], bonus[1])

            if bonus[1].bottom <= (boot.height + 300):  # Keep if visible
                if _player_rect.colliderect(bonus[1]):
                    scores += 1
                else:
                    bonuses_to_keep.append(bonus)
        bonuses.clear()
        bonuses.extend(bonuses_to_keep)

        if pressed_keys[py.K_DOWN] and not _player_rect.bottom >= boot.height:
            _player_rect.y += _player_speed

        if pressed_keys[py.K_UP] and not _player_rect.top <= 0:
            _player_rect.y -= _player_speed

        if pressed_keys[py.K_RIGHT] and not _player_rect.right >= boot.width:
            _player_rect.x += _player_speed

        if pressed_keys[py.K_LEFT] and not _player_rect.left <= 0:
            _player_rect.x -= _player_speed

        if scores >= max_score:
            if not boot.config.check(level):
                boot.config.writer(level)
            _game_work = False

        if not settings_open and _game_work:
            settings_open = True

            boot.invisible_cursor()
            boot.music.music_load(boot.sound_game)
            boot.music.music_unpause()

        if scores != last_score_render:
            score_text_cache = boot.BASE_FONT.render_font().render(str(scores), True, boot.BLACK)
            last_score_render = scores

        boot.main_surface.blit(score_text_cache, (boot.main_surface.get_width() - 0.029 * boot.width, 0))
        boot.version_game()
        boot.get_fps(
            boot.GAME_TEXT, boot.RED,
            (0.0036*boot.width, 0.0065*boot.height), "topleft"
        )
        boot.tick_fps()
        boot.update_display()

    _game_work = True
    clean_bon_and_en()
    _player_rect.x, _player_rect.y = 0,0
    boot.music.set_position()
    boot.music.music_all(boot.sound_menu)
    boot.standard_curs()
    boot.visible_cursor()


if __name__ == "__main__":
    source(1, 3, ENEMY_EVENT, 30, {"level": 1})
