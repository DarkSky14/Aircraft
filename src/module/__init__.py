__version__ = "0.2.8-b"
__author__ = "Chinho"

from pygame import init, font, display, mouse, transform, image, time

from module.correct_start import fix_import

try:
    from logged import log
    from music import Music, Sound

    from language import LanguageCreater, LanguageSetter
    from FileWorker import JsonReader, JsonWorker

    from Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
    from event import EventControl

    from Text import Text, ModuleText
    from UI import ModuleButton

except ImportError:
    from module.logged import log
    from module.music import Music, Sound

    from module.language import LanguageCreater, LanguageSetter
    from module.FileWorker import JsonReader, JsonWorker

    from module.Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
    from module.event import EventControl

    from module.Text import Text, ModuleText
    from module.UI import ModuleButton


def get_version():
    return __version__

def get_author():
    return __author__


init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (250, 0, 0)
GREEN = (0, 255, 0)
LIME = (100, 250, 100)
COLOR_CASE = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (250, 0, 0),
    "GREEN": (0, 255, 0),
    "LIME": (100, 250, 100),
}

click_open_2 = fix_import + "library/effect/click_open2.mp3"
click_open_1 = fix_import + "library/effect/click_open1.mp3"
click_exit = fix_import + "library/effect/click_exit1.mp3"
effect_game = fix_import + "library/effect/sound3.mp3"
click_aim = fix_import + "library/effect/nice click aim.mp3"
sound_menu = fix_import + "library/music/Menu1 - peace.mp3"
sound_game = fix_import + "library/music/01897.mp3"


def click_cursor():
    mouse.set_cursor(11)


def standart_curs():
    mouse.set_cursor(0)


def invisible_cursor():
    mouse.set_visible(False)


def visible_cursor():
    mouse.set_visible(True)

FPS = time.Clock()

fps = 0


def set_fps(tick=None):
    global fps
    if tick is None:
        return fps
    fps = tick
    return fps


def tick_fps():
    global fps
    FPS.tick(fps)


log.info("Load sounds...")
clicks_used = Sound(click_open_2)


def clicks():
    clicks_used.create_channel()


return_exit_used = Sound(click_exit)


def return_exit():
    return_exit_used.create_channel()


scroll_used = Sound(click_aim)


def scroll():
    scroll_used.create_channel(volume=0.05)


log.info("Sounds (3) successfully loaded.")


main_surface = AdjustmentSurface().surface()  # 960, 544 StandartSurface(960, 544) #
sub_surface = AdjustmentSubSurface(1373, 761)  # Original size 300x168
d = sub_surface.surface(main_surface)
main_surface.fill((0, 0, 0))
d.fill((255, 255, 255))

screen = sub_surface.get_size_surface()
conf_width = sub_surface.get_conf_width()
conf_height = sub_surface.get_conf_height()
procent = sub_surface.get_procent()
height = d.get_height()
width = d.get_width()

log.debug({"Main surface size": screen})


log.info("Start load background image...")
bg = transform.scale(
    image.load(fix_import + "library/pictures/background.png").convert(), screen
)
log.info("Background image successfully loaded.")
bgX = 0
bgX2 = bg.get_width()
bg_speed = 1


config = JsonWorker(
    "config",
    fix_import + "library/data",
    {"level": 1, "effect": "True", "music": "True", "language": "EN"},
    "config.json",
)
config.reader()


GLOBAL_EVENT = EventControl(200, conf_width, conf_height)


ENG = LanguageCreater("EN", fix_import + "library/language", "english.json")
ENG.set_lang(JsonReader)
ENGLISH = ENG.get_lang()

UKR = LanguageCreater("UA", fix_import + "library/language", "ukrainian.json")
UKR.set_lang(JsonReader)
UKRAINIAN = UKR.get_lang()

language = LanguageSetter(config).language_set(ENG, UKR)
log.info("LANGUAGE LOADED...")


log.info("Load font...")
STANDART_TEXT = font.SysFont("Georgia", round(21 * procent), 0, 0)  # Arial
BIG_TEXT = font.SysFont("Georgia", round(36 * procent))
VERS_GAME = font.SysFont(None, round(20 * procent))
BASE_FONT = font.SysFont("Calibri", round(20 * procent))
GAME_TEXT = font.SysFont("Consolas", round(30 * procent))
log.info("Font (4) successfully loaded.")

text = Text(VERS_GAME, language, d, config, (0, 0, 0))
big_text = ModuleText(text.copy())
big_text.create_font("Georgia", round(36 * procent))

standart_text = ModuleText(text.copy())
standart_text.create_font("Georgia", round(21 * procent))


button_modified = ModuleButton(GLOBAL_EVENT, d, config, standart_text, procent)


def sound_scroll():
    if config.check({"effect": "True"}):
        scroll()


fon_background = ScrollingBG(bg, bg_speed)


def update_display():
    display.update(conf_width, conf_height, width, height)


music = Music(config, sound_menu, 0.1)
music.music_all(sound_menu)


def background():
    fon_background.update()
    fon_background.draw(d)


def version_game():
    d.blit(
        VERS_GAME.render(str(get_version()), True, BLACK),
        (width - (44 * procent), height - (14 * procent)),
    )

def get_fps(
    font: font.Font = BASE_FONT,
    color: tuple = (200, 200, 200),
    coordinate: tuple = (3, 3),
):
    main_surface_fps = font.render(str(int(FPS.get_fps())), True, (color))
    rect_obgect = main_surface_fps.get_rect()
    rect_obgect.topleft = coordinate
    d.blit(main_surface_fps, rect_obgect)