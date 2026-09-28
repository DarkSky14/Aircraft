__version__ = "0.2.9"
__author__ = "Chinho/DarkSky14"

import pygame as py
import sys

from module.loader import base_absolute_import
from module.logger import log
from module.music import Music, Sound

from module.language import LanguageCreated, LanguageSetter
from module.FileWorker import JsonReader, JsonWorker

from module.Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
from module.event import EventManager, Mouse

from module.UI import ButtonModify, CanvasButton, ButtonCollector, Text, DrawText

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

click_open_2 = base_absolute_import("effect/click_open2.mp3")
click_open_1 = base_absolute_import("effect/click_open1.mp3")
click_exit = base_absolute_import("effect/click_exit1.mp3")
effect_game = base_absolute_import("effect/sound3.mp3")
click_aim = base_absolute_import("effect/nice click aim.mp3")
sound_menu = base_absolute_import("music/Menu1 - peace.mp3")
sound_game = base_absolute_import("music/01897.mp3")
