from module import (
    button_modified, standart_text, GLOBAL_EVENT, background, work,
    update_display, big_text, sound_scroll, procent, height, config,
    pygame,
)

from module.menu_client import (
    clicks, return_exit, version_game, standart_curs, click_cursor,
)

from game import sourse
from pygame import QUIT, K_ESCAPE, KEYDOWN
from module.game_client import set_fps, get_fps, tick_fps

from module.game_client import sw1, sh1, CREATE_ENEMY1, max_score1
from module.game_client import sw2, sh2, CREATE_ENEMY2, max_score2
from module.game_client import sw3, sh3, CREATE_ENEMY3, max_score3


def exitLEVEL():
    global work
    work = False

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
    sourse(sw1, sh1, CREATE_ENEMY1, max_score1, {"level": 2})
    set_fps(60)

def _button_2_callback_():
    _button2_.check_config({"effect": "True"}, clicks)
    if config.get_value("level") >= 2:
        sourse(sw2, sh2, CREATE_ENEMY2, max_score2, {"level": 3})
        set_fps(60)

def _button_3_callback_():
    _button3_.check_config({"effect": "True"}, clicks)
    if config.get_value("level") >= 3:
        sourse(sw3, sh3, CREATE_ENEMY3, max_score3, {"level": 3.1})
        set_fps(60)

def _button_4_callback_():
    _button4_.check_config({"effect": "True"}, return_exit)
    exitLEVEL()


def level():
    global work

    _button1_.moved(50, None, 300)
    _button2_.moved(50, None, 300)
    _button3_.moved(50, None, 300)
    _button4_.moved(50, None, 300)

    button1 = button_modified.copy()
    button1.set_object(-300 * procent, 220 * procent, (300, 30))
    button1.moved(50, None, 300)

    button2 = button_modified.copy()
    button2.set_object(
        button1.get_x_pos(),
        (button1.get_y_pos() + button1.get_size_y() + (10 * procent)),
        (300, 30),
    )
    button2.moved(50, None, 300)

    button3 = button_modified.copy()
    button3.set_object(
        button2.get_x_pos(),
        (button2.get_y_pos() + button2.get_size_y() + (10 * procent)),
        (300, 30),
    )
    button3.moved(50, None, 300)

    button4 = button_modified.copy()
    button4.set_object(
        button3.get_x_pos(),
        (button3.get_y_pos() + button3.get_size_y() + (30 * procent)),
        (300, 30),
    )
    button4.moved(50, None, 300)

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

    set_fps(60)

    def initialiaze():
        for event in pygame.event.get():
            GLOBAL_EVENT.event = event
            if GLOBAL_EVENT.event.type == QUIT:
                pygame.quit()
                exit()

            GLOBAL_EVENT.mouse_get()
            GLOBAL_EVENT.MOUSEBUTTONDOWN()

            if GLOBAL_EVENT.comparison_type(KEYDOWN) and GLOBAL_EVENT.comparison_key(
                K_ESCAPE
            ):
                config.check({"effect": "True"}, return_exit)
                GLOBAL_EVENT.set_key(0)
                exitLEVEL()

        background()

        button_1()
        button_2()
        button_3()
        button_4()

        version_game()
        GLOBAL_EVENT.MOUSEBUTTONDOWN()
        GLOBAL_EVENT.event_button_check(standart_curs, click_cursor, sound_scroll)
        big_text.get_set_text("11", 70 * procent, 150 * procent)

        get_fps(coordinate=(3, height - (20 * procent)))
        tick_fps()
        update_display()

    while work:
        initialiaze()

    work = True


if __name__ == "__main__":
    set_fps(60)
    level()
