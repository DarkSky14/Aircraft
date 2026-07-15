import sys
from sys import exit
from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parent
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import module
from module import (
    log, absolute_import, boot
)

from pygame import QUIT, image, transform, display, quit, event
from options import options
from languageUI import language_get
from level import level

# Setup pygame/window -----------------------------
#boot = module

log.info("Setup icon window...")
icon_obj = image.load(absolute_import("Aircraft.ico")).convert()
icon = transform.scale(icon_obj, boot.screen)
log.info("Icon window setup complete.")
log.info("Setup background image options...")

display.set_caption("Aircraft", "Aircraft")
display.set_icon(icon)

def exit_game():
    log.info("Successful stop.")
    quit()
    exit()

_button1_ = boot.button_modified.copy()
_button1_.set_object((-300 * boot.procent), (220 * boot.procent), (300, 30))

_button2_ = boot.button_modified.copy()
_button2_.set_object(
    (-300 * boot.procent),
    (_button1_.get_y_pos() + _button1_.get_size_y() + (10 * boot.procent)),
    (300, 30),
)

_button3_ = boot.button_modified.copy()
_button3_.set_object(
    (-300 * boot.procent),
    (_button2_.get_y_pos() + _button2_.get_size_y() + (10 * boot.procent)),
    (300, 30),
)

_button4_ = boot.button_modified.copy()
_button4_.set_object(
    (-300 * boot.procent),
    (_button3_.get_y_pos() + _button3_.get_size_y() + (25 * boot.procent)),
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
    _button1_.check_config({"effect": "True"}, boot.clicks)
    level()

def _button_2_callback_():
    _button2_.check_config({"effect": "True"}, boot.clicks)
    options(25, 150)

def _button_3_callback_():
    _button3_.check_config({"effect": "True"}, boot.clicks)
    language_get()

def _button_4_callback_():
    _button4_.check_config({"effect": "True"}, boot.return_exit)
    exit_game()

_button_get()


def main_menu():
    work = True

    boot.set_fps(60)

    def button_call1():
        _button1_.Button(_button_1_callback_)
        _button1_.animation()
        text = boot.standard_text.set_base_text("0")
        _button1_.get_text(text)
    
    def button_call2():
        _button2_.Button(_button_2_callback_)
        _button2_.animation()
        text = boot.standard_text.set_base_text("1")
        _button2_.get_text(text)

    def button_call3():
        _button3_.Button(_button_3_callback_)
        _button3_.animation()
        text = boot.standard_text.set_base_text("2")
        _button3_.get_text(text)

    def button_call4():
        _button4_.Button(_button_4_callback_)
        _button4_.animation()
        text = boot.standard_text.set_base_text("6")
        _button4_.get_text(text)

    def initialize():
        for event_ in event.get():
            boot.GLOBAL_EVENT.event = event_

            if boot.GLOBAL_EVENT.comparison_type(QUIT):
                quit()
                exit()

        boot.GLOBAL_EVENT.mouse_get()
        boot.GLOBAL_EVENT.mouse_button_down()

        boot.background()

        button_call1()
        button_call2()
        button_call3()
        button_call4()

        boot.version_game()
        boot.GLOBAL_EVENT.event_button_check(
            boot.standard_curs, boot.click_cursor, boot.sound_scroll
        )
        text = boot.big_text.set_base_text("7")
        boot.big_text.get_set_text(text, 70 * boot.procent, 150 * boot.procent)

        boot.get_fps(coordinate=(3, boot.height - (20 * boot.procent)))
        boot.tick_fps()
        boot.update_display()

    while work:
        initialize()


if __name__ == "__main__":
    log.info("Successful start...")
    main_menu()
