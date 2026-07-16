__version__ = "0.2.8-dev"
__author__ = "Chinho/DarkSky14"

from pygame import init, display, mouse, transform, image, time, surface

from module.correct_start import absolute_import
from module.logged import log
from module.music import Music, Sound

from module.language import LanguageCreated, LanguageSetter
from module.FileWorker import JsonReader, JsonWorker

from module.Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
from module.event import EventControl

from module.Text import *
from module.UI import ModuleButton

def get_version():
    return __version__


def get_author():
    return __author__

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

click_open_2 = absolute_import("effect/click_open2.mp3")
click_open_1 = absolute_import("effect/click_open1.mp3")
click_exit = absolute_import("effect/click_exit1.mp3")
effect_game = absolute_import("effect/sound3.mp3")
click_aim = absolute_import("effect/nice click aim.mp3")
sound_menu = absolute_import("music/Menu1 - peace.mp3")
sound_game = absolute_import("music/01897.mp3")
