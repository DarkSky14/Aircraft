from Aircraft.module.file_manager.config import url_fixer, LIBRARY_ROOT
from Aircraft.module.file_manager.logger import log
from Aircraft.module.file_manager.loader import ImageLoader
from Aircraft.module.music import Music, Sound

from Aircraft.module.language import LanguageCreated, LanguageSetter
from Aircraft.module.file_manager.json_handler import JsonWorker

from Aircraft.module.Surface import AdjustmentSubSurface, AdjustmentSurface, ScrollingBG
from Aircraft.module.event import EventManager, Mouse

from Aircraft.module.UI import CanvasButton, ButtonCollector, Text, DrawText

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

click_open_2 = url_fixer("assets/effect/click_open2.mp3")
click_open_1 = url_fixer("assets/effect/click_open1.mp3")
click_exit = url_fixer("assets/effect/click_exit1.mp3")
effect_game = url_fixer("assets/effect/sound3.mp3")
click_aim = url_fixer("assets/effect/nice click aim.mp3")
sound_menu = url_fixer("assets/music/Menu1 - peace.mp3")
sound_game = url_fixer("assets/music/01897.mp3")
