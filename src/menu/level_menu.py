import sys
sys.path.append("..")

from menu.game import source, ENEMY_EVENT
from module import log, py, sys
from cached.bootstrap import boot

_work = True

def exit_level():
    global _work
    _work = False

_button1_ = boot.button_modified.copy()
_button1_.set_object((-0.22 * boot.width), (0.289 * boot.height), (0.22, 0.041))

_button2_ = boot.button_modified.copy()
_button2_.set_object(
    (-0.22 * boot.width),
    (_button1_.y + _button1_.size_y + (0.0132 * boot.height)),
    (0.22, 0.041),
)

_button3_ = boot.button_modified.copy()
_button3_.set_object(
    (-0.22 * boot.width),
    (_button2_.y + _button2_.size_y + (0.0132 * boot.height)),
    (0.22, 0.041),
)

_button4_ = boot.button_modified.copy()
_button4_.set_object(
    (-0.22 * boot.width),
    (_button3_.y + _button3_.size_y + (0.033 * boot.height)),
    (0.22, 0.041),
)

def _button_get():
    _button1_.moved(0.032, None, 0.5)
    _button2_.moved(0.032, None, 0.5)
    _button3_.moved(0.032, None, 0.5)
    _button4_.moved(0.032, None, 0.5)

def _button_hide():
    _button1_.moved(-0.22, None, 0.5)
    _button2_.moved(-0.22, None, 0.5)
    _button3_.moved(-0.22, None, 0.5)
    _button4_.moved(-0.22, None, 0.5)

def _button_1_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not _button1_.move_status:
        source(1, 3, ENEMY_EVENT, 30, {"level": 2})
        boot.set_fps(60)

def _button_2_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if boot.config.get_value("level", 0) >= 2 and  not _button2_.move_status:
        source(2, 5, ENEMY_EVENT, 300, {"level": 3}, enemy_timer_spawn= 3000)
        boot.set_fps(60)

def _button_3_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if boot.config.get_value("level", 0) >= 3 and not _button3_.move_status:
        source(3, 7, ENEMY_EVENT, 1500, {"level": 3.1}, enemy_timer_spawn= 2000)
        boot.set_fps(60)

def _button_4_callback_():
    boot.config.check({"effect": "True"}, boot.return_exit)
    if not _button4_.move_status:
        _button4_.set_func(exit_level, _button_get)
        _button_hide()

_buttons = (
    (_button1_, _button_1_callback_, "3"),
    (_button2_, _button_2_callback_, "4"),
    (_button3_, _button_3_callback_, "5"),
    (_button4_, _button_4_callback_, "6"),
)

def draw_menu_buttons():
    for button, callback, text_key in _buttons:
        button.animation()
        button.callback(callback)
        button.get_text(boot.standard_text.set_base_text(text_key))

_button_get()

def level():
    global _work

    boot.set_fps(60)

    def initialize():
        for event in boot.GLOBAL_EVENT.event_pool():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                boot.config.check({"effect": "True"}, boot.return_exit)
                if not _button4_.move_status:
                    _button3_.set_func(exit_level, _button_get)
                    _button_hide()

        boot.GLOBAL_EVENT.mouse.mouse_get()
        boot.background()

        draw_menu_buttons()
        boot.GLOBAL_EVENT.task.get_tasks()

        boot.version_game()
        boot.GLOBAL_EVENT.mouse.event_button_check(
            boot.standard_curs, boot.click_cursor, boot.sound_scroll
        )
        text = boot.standard_text.set_base_text("11")
        boot.big_text.draw_text(text, 0.05 * boot.width, 0.20 * boot.height)

        boot.get_fps(coordinate=(0.0022*boot.width, boot.height))
        boot.tick_fps()
        boot.update_display()

    try:
        while _work:
            initialize()
    except Exception as e:
        log.exception("Unhandled error in level: %s", e)
        raise

    _work = True


if __name__ == "__main__":
    boot.set_fps(60)
    level()
