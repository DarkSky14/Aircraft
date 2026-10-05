import pygame as py
import sys


from config import url_fixer, LIBRARY_ROOT
from project_info import get_version
from module.logger import log
from module.loader import ImageLoader
from module.music import Music, Sound

from module.language import LanguageCreated, LanguageSetter
from module.FileWorker import JsonWorker

from module.Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
from module.event import EventManager, Mouse

from module.UI import ButtonModify, CanvasButton, ButtonCollector, Text, DrawText

log.debug(LIBRARY_ROOT.debug())

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

click_open_2 = url_fixer("effect/click_open2.mp3")
click_open_1 = url_fixer("effect/click_open1.mp3")
click_exit = url_fixer("effect/click_exit1.mp3")
effect_game = url_fixer("effect/sound3.mp3")
click_aim = url_fixer("effect/nice click aim.mp3")
sound_menu = url_fixer("music/Menu1 - peace.mp3")
sound_game = url_fixer("music/01897.mp3")
