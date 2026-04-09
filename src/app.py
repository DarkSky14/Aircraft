from sys import exit

from module import (
    button_modified, standart_text, GLOBAL_EVENT, background,
    update_display, big_text, sound_scroll, log, fix_import,
    procent, height, screen, version_game, clicks, return_exit, 
    standart_curs, click_cursor, set_fps, get_fps, tick_fps,
)

from pygame import QUIT, image, transform, display, quit, event

from level import level
from options import options
from languageUI import language_get


# Setup pygame/window -----------------------------
log.info("Setup icon window...")
icon_obj = image.load(fix_import + "library/Aircraft.ico").convert()
icon = transform.scale(icon_obj, screen)
log.info("Icon window setup complete.")
log.info("Setup background image options...")

display.set_caption("Aircraft", "Aircraft")
display.set_icon(icon)

def exitGame():
    log.info("Successful stop.")
    quit()
    exit()


_button1_ = button_modified.copy()
_button1_.set_object((-300 * procent), (220 * procent), (300, 30))

_button2_ = button_modified.copy()
_button2_.set_object(
    (-300 * procent),
    (_button1_.get_y_pos() + _button1_.get_size_y() + (10 * procent)),
    (300, 30),
)

_button3_ = button_modified.copy()
_button3_.set_object(
    (-300 * procent),
    (_button2_.get_y_pos() + _button2_.get_size_y() + (10 * procent)),
    (300, 30),
)

_button4_ = button_modified.copy()
_button4_.set_object(
    (-300 * procent),
    (_button3_.get_y_pos() + _button3_.get_size_y() + (25 * procent)),
    (300, 30),
)


def _button_hide():
    _button1_.moved(-300, None, 0)
    _button2_.moved(-300, None, 0)
    _button3_.moved(-300, None, 0)
    _button4_.moved(-300, None, 0)


def _button_get():
    _button1_.moved(50, None, 300)
    _button2_.moved(50, None, 300)
    _button3_.moved(50, None, 300)
    _button4_.moved(50, None, 300)


def _button_1_callback_():
    _button1_.check_config({"effect": "True"}, clicks)
    level()

def _button_2_callback_():
    _button2_.check_config({"effect": "True"}, clicks)
    options(25, 150)

def _button_3_callback_():
    _button3_.check_config({"effect": "True"}, clicks)
    language_get()

def _button_4_callback_():
    _button4_.check_config({"effect": "True"}, return_exit)
    exitGame()

_button_get()


def main_menu():
    global work
    work = True

    set_fps(60)

    def button_call1():
        _button1_.Button(_button_1_callback_)
        _button1_.animation()
        _button1_.get_text(standart_text, "0")
    
    def button_call2():
        _button2_.Button(_button_2_callback_)
        _button2_.animation()
        _button2_.get_text(standart_text, "1")

    def button_call3():
        _button3_.Button(_button_3_callback_)
        _button3_.animation()
        _button3_.get_text(standart_text, "2")

    def button_call4():
        _button4_.Button(_button_4_callback_)
        _button4_.animation()
        _button4_.get_text(standart_text, "6")

    def initialize():
        for event_ in event.get():
            GLOBAL_EVENT.event = event_

            if GLOBAL_EVENT.comparison_type(QUIT):
                quit()
                exit()

            GLOBAL_EVENT.mouse_get()
            GLOBAL_EVENT.MOUSEBUTTONDOWN()

        background()

        button_call1()
        button_call2()
        button_call3()
        button_call4()

        version_game()
        GLOBAL_EVENT.event_button_check(standart_curs, click_cursor, sound_scroll)
        big_text.get_set_text("7", 70 * procent, 150 * procent)

        get_fps(coordinate=(3, height - (20 * procent)))
        tick_fps()
        update_display()

    while work:
        initialize()

    work = True


if __name__ == "__main__":
    log.info("Successful start...")
    main_menu()
