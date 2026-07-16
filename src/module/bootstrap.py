from dataclasses import dataclass
from module import init, display, mouse, transform, image, time, surface
#import pygame

from module.correct_start import absolute_import
from module.logged import log
from module.music import Music, Sound
from module.language import LanguageCreated, LanguageSetter
from module.FileWorker import JsonReader, JsonWorker
from module.Surface import AdjustmentSurface, AdjustmentSubSurface, ScrollingBG
from module.event import EventControl
from module.Text import Text, Font
from module.UI import ModuleButton
from module import get_author, get_version

@dataclass
class AppContext:
    d: surface.Surface
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
    set_fps: None
    background: None
    version_game: None
    sound_scroll: None
    click_cursor: None
    standard_curs: None
    visible_cursor: None
    invisible_cursor: None
    tick_fps: None
    clicks: None
    return_exit: None
    get_fps: None
    update_display: None
    click_open_1: str
    effect_game: str
    sound_game: str
    ENGLISH: dict
    UKRAINIAN: dict
    GAME_TEXT: None
    sound_menu: str
    main_surface: None
    bg: None
    bgX: int
    bgX2: int
    BASE_FONT: None
    BLACK: tuple
    RED: tuple
    WHITE: tuple
    GREEN: tuple
    LIME: tuple


def bootstrap() -> AppContext:
    init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (250, 0, 0)
    GREEN = (0, 255, 0)
    LIME = (100, 250, 100)

    click_open_2 = absolute_import("effect/click_open2.mp3")
    click_open_1 = absolute_import("effect/click_open1.mp3")
    click_exit = absolute_import("effect/click_exit1.mp3")
    effect_game = absolute_import("effect/sound3.mp3")
    click_aim = absolute_import("effect/nice click aim.mp3")
    sound_menu = absolute_import("music/Menu1 - peace.mp3")
    sound_game = absolute_import("music/01897.mp3")

    def click_cursor():
        mouse.set_cursor(11)

    def standard_curs():
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

    log.info("Setup sounds/config/UI...")

    main_surface = AdjustmentSurface().surface()
    sub_surface = AdjustmentSubSurface(1373, 761)
    d = sub_surface.surface(main_surface)
    main_surface.fill((0, 0, 0))
    d.fill((255, 255, 255))

    screen = sub_surface.screen
    conf_width = sub_surface.get_conf_width()
    conf_height = sub_surface.get_conf_height()
    procent = sub_surface.get_proponent()
    height = d.get_height()
    width = d.get_width()

    log.debug({"Main surface size": screen})

    log.info("Start load background image...")
    bg = transform.scale(
        image.load(absolute_import("pictures/background.png")).convert(), screen
    )
    log.info("Background image successfully loaded.")
    bgX = 0
    bgX2 = bg.get_width()
    bg_speed = 1

    config = JsonWorker(
        "config",
        absolute_import("data"),
        {"level": 1, "effect": "True", "music": "True", "language": "EN"},
        "config.json",
    )
    config.reader()

    GLOBAL_EVENT = EventControl(200, conf_width, conf_height)

    ENG = LanguageCreated("EN", absolute_import("language"), "english.json")
    ENG.set_language(JsonReader)
    ENGLISH = ENG.language

    UKR = LanguageCreated("UA", absolute_import("language"), "ukrainian.json")
    UKR.set_language(JsonReader)
    UKRAINIAN = UKR.language

    active_language = LanguageSetter(config).language_set(ENG, UKR)
    log.info("LANGUAGE LOADED...")

    log.info("Load font...")

    BIG_TEXT = Font("Georgia", round(36 * procent))  # Arial
    VERS_GAME = Font(None, round(20 * procent))
    BASE_FONT = Font("Georgia", round(21 * procent))
    GAME_TEXT = Font("Georgia", round(30 * procent))
    log.info("Font (4) successfully loaded.")

    text = Text(VERS_GAME.render_font(), active_language, d, config, (0, 0, 0))
    big_text = text.copy_text()
    big_text.set_font(BIG_TEXT.copy_font())

    standard_text = text.copy_text()
    standard_text.set_font(BASE_FONT.copy_font())

    button_modified = ModuleButton(GLOBAL_EVENT, d, config, standard_text, procent)

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
            VERS_GAME.render_font().render(str(get_version()), True, BLACK),
            (width - (50 * procent), height - (14 * procent)),
        )

    def get_fps(
            font_text: Font = BASE_FONT,
            color: tuple = (200, 200, 200),
            coordinate: tuple = (3, 3),
    ):
        main_surface_fps = font_text.render_font().render(str(int(FPS.get_fps())), True, color)
        rect_object = main_surface_fps.get_rect()
        rect_object.topleft = coordinate
        d.blit(main_surface_fps, rect_object)

    return AppContext(
        d=d, screen=screen, procent=procent,
        conf_width=conf_width, conf_height=conf_height,
        height=height, width=width,
        config=config, GLOBAL_EVENT=GLOBAL_EVENT,
        standard_text=standard_text, big_text=big_text,
        button_modified=button_modified,
        fon_background=fon_background,
        music=music, clicks_used=clicks_used,
        return_exit_used=return_exit_used, scroll_used=scroll_used,
        set_fps=set_fps, background=background,
        version_game=version_game, sound_scroll=sound_scroll,
        click_cursor=click_cursor, standard_curs=standard_curs,
        visible_cursor=visible_cursor, invisible_cursor=invisible_cursor,
        tick_fps=tick_fps, clicks=clicks, return_exit=return_exit,
        get_fps=get_fps, update_display=update_display,
        click_open_1=click_open_1, effect_game=effect_game,
        sound_game=sound_game, ENGLISH=ENGLISH, UKRAINIAN=UKRAINIAN,
        GAME_TEXT=GAME_TEXT, sound_menu=sound_menu,
        main_surface=main_surface, bg=bg, bgX=bgX, bgX2=bgX2,
        BASE_FONT=BASE_FONT,BLACK=BLACK,LIME=LIME, WHITE=WHITE,
        RED=RED, GREEN=GREEN
    )

boot = bootstrap()