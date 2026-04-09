from module import (
    ScrollingBG, music, config, GAME_TEXT, bg, update_display, d, log,
    height, width, BASE_FONT, version_game, standart_curs,
    sound_game, sound_menu, BLACK, RED, invisible_cursor, visible_cursor,
    fix_import, procent, set_fps, get_fps, tick_fps
)


from pygame import (
    QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_ESCAPE, KEYDOWN, event, key,
    USEREVENT, time, image, transform, Rect
)

from options import options
from random import randint
from os import listdir

_bg_speed_ = 2 * procent
_game_work = True

IMGS_PATH = fix_import + "library/player"

log.info("Start load player images...")
_player_img = [
    image.load(IMGS_PATH + "/" + file).convert_alpha()
    for file in listdir(IMGS_PATH)
]
_player_imgs = [
    transform.scale(
        player_img,
        ((player_img.get_width() * procent), (player_img.get_height() * procent)),
    )
    for player_img in _player_img
]
log.info("Player images successfully load.")
_player = _player_imgs[0]
_player_rect = _player.get_rect()
_player_speed = 2.5 * procent


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
_bonus_jpg = image.load(fix_import + "library/pictures/bonus.jpg")
_bonus = transform.scale(
    _bonus_jpg, ((_bonus_jpg.get_width() * procent), (_bonus_jpg.get_height() * procent))
)
def _create_bonus():
    global _bonus
    bonus_rect = Rect(randint(0, int(width)), -1000, *_bonus.get_size())
    bonus_speed = 0
    return [_bonus, bonus_rect, bonus_speed]
log.info("Bonus image successfully loaded.")


def source(
        speed_w1, speed_w2, enemy_spawn, max_score, level: dict,
        change_img = (USEREVENT + 3), create_bonus = (USEREVENT + 1),
        enemy_timer_spawn = 3500
    ):
    global _game_work,  _player, _player_rect, _player_imgs, _player_speed

    fon_background = ScrollingBG(bg, _bg_speed_)

    def background():
        fon_background.update()
        fon_background.draw(d)

    set_fps(90)

    img_index = 0
    scores = 0
    bonuses = []
    enemies = []

    last_score_render = -1
    score_text_cache = BASE_FONT.render("0", True, BLACK)

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
                    music.music_pause()
                    music.music_load(sound_menu)
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

        d.blit(_player, _player_rect)

        enemies_to_keep = []
        for enemy in enemies:
            enemy[1].x -= enemy[2]
            d.blit(enemy[0], enemy[1])

            if enemy[1].left >= -200: 
                if _player_rect.colliderect(enemy[1]):
                    _game_work = False
                    music.music_pause()
                    music.music_load(sound_menu)
                else:
                    enemies_to_keep.append(enemy)
        enemies.clear()
        enemies.extend(enemies_to_keep)

        bonuses_to_keep = []
        for bonus in bonuses:
            bonus[1].x -= bonus[2]
            bonus[1].y += 2
            d.blit(bonus[0], bonus[1])

            if bonus[1].bottom <= (height + 300):  # Keep if visible
                if _player_rect.colliderect(bonus[1]):
                    scores += 1
                else:
                    bonuses_to_keep.append(bonus)
        bonuses.clear()
        bonuses.extend(bonuses_to_keep)

        if pressed_keys[K_DOWN] and not _player_rect.bottom >= height:
            _player_rect.y += _player_speed

        if pressed_keys[K_UP] and not _player_rect.top <= 0:
            _player_rect.y -= _player_speed

        if pressed_keys[K_RIGHT] and not _player_rect.right >= width:
            _player_rect.x += _player_speed

        if pressed_keys[K_LEFT] and not _player_rect.left <= 0:
            _player_rect.x -= _player_speed

        if scores >= max_score:
            if not config.check(level, invisible_cursor):
                config.write(level)
            _game_work = False

        if check_first_while == 0 and _game_work:
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

    _game_work = True
    clean_bon_and_en()
    music.set_position()
    music.music_all(sound_menu)
    standart_curs()
    visible_cursor()


if __name__ == "__main__":
    source(1, 3, USEREVENT + 2, 30, {"level": 1})
