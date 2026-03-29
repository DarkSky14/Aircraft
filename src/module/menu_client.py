__version__ = "0.2.7"
__author__ = "Chinho"

if __name__ == "__main__":
    import music as mus
    from module import (
        procent, width, d, height, screen, log, fix_import, 
        VERS_GAME, pygame
    )
else:
    import module.music as mus
    from module import (
        procent, width, d, height, screen, log, fix_import,
        VERS_GAME, pygame
    )


def get_version():
    return __version__


def get_author():
    return __author__


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (250, 0, 0)
GREEN = (0, 255, 0)
LIME = (100, 250, 100)

click_open_2 = fix_import + "library/effect/click_open2.mp3"
click_open_1 = fix_import + "library/effect/click_open1.mp3"
click_exit = fix_import + "library/effect/click_exit1.mp3"
effect_game = fix_import + "library/effect/sound3.mp3"
click_aim = fix_import + "library/effect/nice click aim.mp3"
sound_menu = fix_import + "library/music/Menu1 - peace.mp3"
sound_game = fix_import + "library/music/01897.mp3"


def click_cursor():
    pygame.mouse.set_cursor(11)


def standart_curs():
    pygame.mouse.set_cursor(0)


def invisible_cursor():
    pygame.mouse.set_visible(False)


def visible_cursor():
    pygame.mouse.set_visible(True)


log.info("Load sounds...")
clicks_used = mus.Sound(click_open_2)


def clicks():
    clicks_used.create_channel()


return_exit_used = mus.Sound(click_exit)


def return_exit():
    return_exit_used.create_channel()


scroll_used = mus.Sound(click_aim)


def scroll():
    scroll_used.create_channel(volume=0.05)


log.info("Sounds (3) successfully loaded.")

log.info("Start load background image...")
bg = pygame.transform.scale(
    pygame.image.load(fix_import + "library/pictures/background.png").convert(), screen
)
log.info("Background image successfully loaded.")
bgX = 0
bgX2 = bg.get_width()
bg_speed = 1
bg_speed1 = 2


def version_game():
    d.blit(
        VERS_GAME.render(str(get_version()), True, BLACK),
        (width - (33 * procent), height - (14 * procent)),
    )
