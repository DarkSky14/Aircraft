from module import (
    button_modified, standart_text, GLOBAL_EVENT, background,
    update_display, big_text, sound_scroll, procent, height, config,
    clicks, return_exit, version_game, standart_curs, click_cursor,
    set_fps, get_fps, tick_fps,
)

from game import source
from pygame import QUIT, K_ESCAPE, KEYDOWN, quit, event, USEREVENT

_work = True

def exit_level():
    global _work
    _work = False

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

def _button1_callback_():
    _button1_.check_config({"effect": "True"}, clicks)
    source(1, 3, USEREVENT + 2, 30, {"level": 2})
    set_fps(60)

def _button_2_callback_():
    _button2_.check_config({"effect": "True"}, clicks)
    if config.get_value("level") >= 2:
        source(2, 5, USEREVENT + 3, 300, {"level": 3}, enemy_timer_spawn= 3000)
        set_fps(60)

def _button_3_callback_():
    _button3_.check_config({"effect": "True"}, clicks)
    if config.get_value("level") >= 3:
        source(3, 7, USEREVENT + 4, 1500, {"level": 3.1}, enemy_timer_spawn= 2000)
        set_fps(60)

def _button_4_callback_():
    _button4_.check_config({"effect": "True"}, return_exit)
    exit_level()

def button_1():
    _button1_.animation()
    _button1_.Button(_button1_callback_)
    _button1_.get_text(standart_text, "3")

def button_2():
    _button2_.animation()
    _button2_.Button(_button_2_callback_)
    _button2_.get_text(standart_text, "4")

def button_3():
    _button3_.animation()
    _button3_.Button(_button_3_callback_)
    _button3_.get_text(standart_text, "5")

def button_4():
    _button4_.animation()
    _button4_.Button(_button_4_callback_)
    _button4_.get_text(standart_text, "6")


def level():
    global _work

    _button1_.moved(50, None, 300)
    _button2_.moved(50, None, 300)
    _button3_.moved(50, None, 300)
    _button4_.moved(50, None, 300)

    set_fps(60)

    def initialize():
        for event_ in event.get():
            GLOBAL_EVENT.event = event_
            if GLOBAL_EVENT.event.type == QUIT:
                quit()
                exit()

            if GLOBAL_EVENT.comparison_type(KEYDOWN) and GLOBAL_EVENT.comparison_key(
                K_ESCAPE
            ):
                config.check({"effect": "True"}, return_exit)
                GLOBAL_EVENT.set_key(0)
                exit_level()

        GLOBAL_EVENT.mouse_get()
        GLOBAL_EVENT.mouse_button_down()
        background()

        button_1()
        button_2()
        button_3()
        button_4()

        version_game()
        GLOBAL_EVENT.mouse_button_down()
        GLOBAL_EVENT.event_button_check(standart_curs, click_cursor, sound_scroll)
        big_text.get_set_text("11", 70 * procent, 150 * procent)

        get_fps(coordinate=(3, height - (20 * procent)))
        tick_fps()
        update_display()

    while _work:
        initialize()

    _work = True


if __name__ == "__main__":
    set_fps(60)
    level()
