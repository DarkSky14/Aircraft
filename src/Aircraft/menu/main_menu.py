import sys

from Aircraft.module import (
    log, base_absolute_import, py, CanvasButton, ButtonCollector,
)
from Aircraft.module.bootstrap import boot

from Aircraft.menu.settings_menu import options, canvas_conf
from Aircraft.menu.language_menu import language_get
from Aircraft.menu.level_menu import level

# Setup pygame/window -----------------------------

log.info("Setup icon window...")
icon_obj = py.image.load(base_absolute_import("Aircraft.ico")).convert()
icon = py.transform.scale(icon_obj, (32, 32))
log.info("Icon window setup complete.")
log.info("Setup background image options...")

py.display.set_caption("Aircraft", "Aircraft")
py.display.set_icon(icon)

def exit_game():
    py.quit()
    log.delete_log()
    sys.exit()

_button1_ = boot.button_modified.copy()
_button1_.set_object(
    (-300 * boot.procent),
    (220 * boot.procent),
    (300, 30)
)

_button2_ = boot.button_modified.copy()
_button2_.set_object(
    (-300 * boot.procent),
    (_button1_.y + _button1_.size_y + (10 * boot.procent)),
    (300, 30),
)

_button3_ = boot.button_modified.copy()
_button3_.set_object(
    (-300 * boot.procent),
    (_button2_.y + _button2_.size_y + (10 * boot.procent)),
    (300, 30),
)

_button4_ = boot.button_modified.copy()
_button4_.set_object(
    (-300 * boot.procent),
    (_button3_.y + _button3_.size_y + (25 * boot.procent)),
    (300, 30),
)


def _button_hide():
    _button1_.moved(-300, None, 0.5)
    _button2_.moved(-300, None, 0.5)
    _button3_.moved(-300, None, 0.5)
    _button4_.moved(-300, None, 0.5)


def _button_get():
    _button1_.moved(50, None, 0.5)
    _button2_.moved(50, None, 0.5)
    _button3_.moved(50, None, 0.5)
    _button4_.moved(50, None, 0.5)


def _button_1_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not _button1_.move_status:
        _button1_.set_func(level, _button_get)
        _button_hide()

def _button_2_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not _button2_.move_status:
        canvas_conf.set_x(25), canvas_conf.set_y(150)
        _button2_.set_func(options, _button_get)
        _button_hide()

def _button_3_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not _button3_.move_status:
        _button3_.set_func(language_get, _button_get)
        _button_hide()

def _button_4_callback_():
    boot.config.check({"effect": "True"}, boot.return_exit)
    if not _button4_.move_status:
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
        button.animation()
        button.callback(callback)
        button.get_text(boot.standard_text, boot.standard_text.set_base_text(text_key))


def main_menu():
    work = True

    boot.set_fps(60)

    try:
        while work:
            boot.GLOBAL_EVENT.event_pool()
            if boot.GLOBAL_EVENT.comparison_type(py.QUIT):
                work = False

            boot.GLOBAL_EVENT.mouse.mouse_get()
            boot.background()

            draw_menu_buttons()
            boot.GLOBAL_EVENT.task.get_tasks()

            boot.version_game()
            boot.GLOBAL_EVENT.mouse.event_button_check(
                boot.standard_curs, boot.click_cursor, boot.sound_scroll
            )
            boot.big_text.draw_text(
                boot.big_text.set_base_text("7"), 70 * boot.procent, 150 * boot.procent
            )

            boot.get_fps(coordinate=(3, boot.height))
            boot.tick_fps()
            boot.update_display()

    except Exception as e:
        log.exception("Unhandled error in main: %s", e)
        raise

if __name__ == "__main__":
    log.info("Successful start...")
    main_menu()
