from module import (
    ScrollingBG, music, config, GAME_TEXT, bg, update_display, d,
    pygame, height, width, BASE_FONT, GLOBAL_EVENT
)

import module

from module.menu_client import version_game, standart_curs


from pygame import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_ESCAPE, KEYDOWN

from module.menu_client import (
    sound_game, sound_menu, bg_speed1, BLACK, RED,
    invisible_cursor, visible_cursor,
)
from module.game_client import (
    set_fps, CREATE_BONUS, CHANGE_IMG, create_bonus, create_enemy,
    get_fps, tick_fps,
)

from options import options


def sourse(speed_w1, speed_w2, ENEMY, max_score, level={str: int}):
    global game_work, work
    from module.game_client import player_imgs, player_speed
    from module.game_client import player, player_rect

    fon_background = ScrollingBG(bg, bg_speed1)

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

    def clean_bon_and_en():
        """Delete all bonusies and enemies"""
        bonusies.clear()
        enemies.clear()

    check_first_while = 0
    module.game_work = True

    while module.game_work:
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    check_first_while = 0
                    music.music_pause()
                    music.music_load(sound_menu)
                    work = True
                    options()

            if event.type == CREATE_BONUS:
                bonusies.append(create_bonus())

            if event.type == ENEMY:
                enemies.append(create_enemy(speed_w1, speed_w2))

            if event.type == CHANGE_IMG:
                img_index += 1
                if img_index == len(player_imgs):
                    img_index = 0
                player = player_imgs[img_index]

        background()

        if scores != last_score_render:
            score_text_cache = BASE_FONT.render(str(scores), True, BLACK)
            last_score_render = scores
        d.blit(score_text_cache, (d.get_width() - 30, 0))

        d.blit(player, (player_rect))
        version_game()

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
            check_first_while = +1

            invisible_cursor()
            music.music_load(sound_game)
            music.music_unpause()

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
    from module.game_client import sw1, sh1, CREATE_ENEMY1, max_score1

    sourse(sw1, sh1, CREATE_ENEMY1, max_score1, {"level": 2})
