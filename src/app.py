import sys

from module import (
    log, absolute_import, py
)
from module.bootstrap import boot

from options import options
from languageUI import language_get
from level import level

# Setup pygame/window -----------------------------

log.info("Setup icon window...")
icon_obj = py.image.load(absolute_import("Aircraft.ico")).convert()
icon = py.transform.scale(icon_obj, (32, 32))
log.info("Icon window setup complete.")
log.info("Setup background image options...")

py.display.set_caption("Aircraft", "Aircraft")
py.display.set_icon(icon)

def exit_game():
    log.info("Successful stop.")
    py.quit()
    sys.exit()

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

_buttons = (
    (_button1_, _button_1_callback_, "0"),
    (_button2_, _button_2_callback_, "1"),
    (_button3_, _button_3_callback_, "2"),
    (_button4_, _button_4_callback_, "6"),
)

def draw_menu_buttons():
    for button, callback, text_key in _buttons:
        button.Button(callback)
        button.animation()
        button.get_text(boot.standard_text.set_base_text(text_key))


def main_menu():
    work = True

    boot.set_fps(60)

    def initialize():
        boot.GLOBAL_EVENT.event_pool()
        if boot.GLOBAL_EVENT.comparison_type(py.QUIT):
            py.quit()
            sys.exit()

        boot.GLOBAL_EVENT.mouse_get()
        boot.GLOBAL_EVENT.mouse_button_down()
        boot.background()

        draw_menu_buttons()

        boot.version_game()
        boot.GLOBAL_EVENT.event_button_check(
            boot.standard_curs, boot.click_cursor, boot.sound_scroll
        )
        boot.big_text.get_set_text(
            boot.big_text.set_base_text("7"), 70 * boot.procent, 150 * boot.procent
        )

        boot.get_fps(coordinate=(3, boot.height - (20 * boot.procent)))
        boot.tick_fps()
        boot.update_display()

    while work:
        try:
            initialize()
        except Exception:
            log.exception("Unhandled error in main")
            raise

if __name__ == "__main__":
    log.info("Successful start...")
    main_menu()
