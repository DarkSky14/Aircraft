from dataclasses import dataclass
import pygame

from module.correct_start import absolute_import
from module.logged import log
from module.music import Music, Sound
from module.language import LanguageCreated, LanguageSetter
from module.FileWorker import JsonReader, JsonWorker
from module.Surface import AdjustmentSurface, AdjustmentSubSurface, ScrollingBG
from module.event import EventControl
from module.Text import Text, Font
from module.UI import ModuleButton


@dataclass
class AppContext:
    d: pygame.Surface
    screen: tuple[int, int]
    procent: float
    conf_width: float
    conf_height: float
    height: int
    width: int
    config: JsonWorker
    GLOBAL_EVENT: EventControl
    standard_text: Text
    big_text: Text
    button_modified: ModuleButton
    fon_background: ScrollingBG
    music: Music
    clicks_used: Sound
    return_exit_used: Sound
    scroll_used: Sound


def bootstrap() -> AppContext:
    """Ініціалізує вікно, звук, конфіг, мову, шрифти — один раз, явно."""
    pygame.init()
    log.info("Setup sounds/config/UI...")

    main_surface = AdjustmentSurface().surface()
    sub_surface = AdjustmentSubSurface(1373, 761)
    d = sub_surface.surface(main_surface)
    main_surface.fill((0, 0, 0))
    d.fill((255, 255, 255))

    screen = sub_surface.get_size_surface()
    procent = sub_surface.get_procent()
    conf_width = sub_surface.get_conf_width()
    conf_height = sub_surface.get_conf_height()

    config = JsonWorker(
        "config",
        absolute_import("data"),
        {"level": 1, "effect": "True", "music": "True", "language": "EN"},
        "config.json",
    )
    config.reader()

    GLOBAL_EVENT = EventControl(200, conf_width, conf_height)

    return AppContext(
        d=d, screen=screen, procent=procent,
        conf_width=conf_width, conf_height=conf_height,
        height=d.get_height(), width=d.get_width(),
        config=config, GLOBAL_EVENT=GLOBAL_EVENT,
        standard_text=standard_text, big_text=big_text,
        button_modified=button_modified,
        fon_background=fon_background,
        music=music_obj, clicks_used=clicks_used,
        return_exit_used=return_exit_used, scroll_used=scroll_used,
    )