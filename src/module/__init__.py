import pygame
from pygame import init

from module.correct_start import fix_import

try:
    from logged import log
    from music import Music

    from language import LanguageCreater, LanguageSetter
    from FileWorker import JsonReader, JsonWorker

    from Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
    from event import EventControl

    from Text import Text, ModuleText
    from UI import ModuleButton

except ImportError:
    from module.logged import log
    from module.music import Music

    from module.language import LanguageCreater, LanguageSetter
    from module.FileWorker import JsonReader, JsonWorker

    from module.Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
    from module.event import EventControl

    from module.Text import Text, ModuleText
    from module.UI import ModuleButton


init()

game_work = True
work = True


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


config = JsonWorker(
    "config",
    fix_import + "library/data",
    {"level": 1, "effect": "True", "music": "True", "language": "EN"},
    "config.json",
)
config.reader()

temp = JsonWorker("temp", "none", {"musicID": "None"})
log.debug({"INITIALIAZE_TEMP": temp.get_data()})


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
STANDART_TEXT = pygame.font.SysFont("Georgia", round(21 * procent), 0, 0)  # Arial
BIG_TEXT = pygame.font.SysFont("Georgia", round(36 * procent))
VERS_GAME = pygame.font.SysFont(None, round(20 * procent))
BASE_FONT = pygame.font.SysFont("Calibri", round(20 * procent))
GAME_TEXT = pygame.font.SysFont("Consolas", round(30 * procent))
log.info("Font (4) successfully loaded.")

text = Text(VERS_GAME, language, d, config, (0, 0, 0))
big_text = ModuleText(text.copy())
big_text.create_font("Georgia", round(36 * procent))

standart_text = ModuleText(text.copy())
standart_text.create_font("Georgia", round(21 * procent))


button_modified = ModuleButton(GLOBAL_EVENT, d, config, standart_text, procent)


try:
    from menu_client import sound_menu, scroll, bg, bg_speed
except ImportError:
    from module.menu_client import sound_menu, scroll, bg, bg_speed


def on_music() -> bool:
    if config.check({"effect": "True"}):
        return True
    else:
        return False


is_music = on_music()


def sound_scroll():
    if is_music:
        scroll()


fon_background = ScrollingBG(bg, bg_speed)


def update_display():
    pygame.display.update(conf_width, conf_height, width, height)


music = Music(config, temp, sound_menu, 0.1)
music.music_all(sound_menu)


def background():
    fon_background.update()
    fon_background.draw(d)
