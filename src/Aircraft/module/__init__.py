import pygame as py
import sys

from Aircraft import base_absolute_import
from Aircraft.module.logger import log
from Aircraft.module.music import Music, Sound

from Aircraft.module.language import LanguageCreated, LanguageSetter
from Aircraft.module.FileWorker import JsonWorker

from Aircraft.module.Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
from Aircraft.module.event import EventManager, Mouse

from Aircraft.module.UI import ButtonModify, CanvasButton, ButtonCollector, Text, DrawText

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
