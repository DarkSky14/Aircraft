import sys
import pygame as py
sys.path.append("..\\..")

from Aircraft.menu.game import source, ENEMY_EVENT
from Aircraft.module import log
from Aircraft.core.bootstrap import boot
from Aircraft.module.UI import ButtonCollector

_work = True

def exit_level():
    global _work
    _work = False

button_p = ButtonCollector(
    boot.GLOBAL_EVENT, boot.main_surface,
    boot.standard_text.copy_text(), (boot.width,boot.height)
)

button_p.add("button_1")
button_p.add("button_2")
button_p.add("button_3")
button_p.add("button_4")

button_p.set_object(
"button_1",
    (-0.22 * boot.width),
    (0.289 * boot.height),
    (0.22, 0.041)
)

button_p.set_object(
    "button_2",
    (-0.22 * boot.width),
    (button_p.get("button_1").y + button_p.get("button_1").size_y + (0.0132 * boot.height)),
    (0.22, 0.041),
)

button_p.set_object(
    "button_3",
    (-0.22 * boot.width),
    (button_p.get("button_2").y + button_p.get("button_2").size_y + (0.0132 * boot.height)),
    (0.22, 0.041),
)

button_p.set_object(
    "button_4",
    (-0.22 * boot.width),
    (button_p.get("button_3").y + button_p.get("button_3").size_y + (0.033 * boot.height)),
    (0.22, 0.041),
)

def _button_get():
    button_p.moved(
        button_p.get("button_1"), 0.032, None, 0.5
    )
    button_p.moved(
        button_p.get("button_2"), 0.032, None, 0.5
    )
    button_p.moved(
        button_p.get("button_3"), 0.032, None, 0.5
    )
    button_p.moved(
        button_p.get("button_4"), 0.032, None, 0.5
    )

def _button_hide():
    button_p.moved(
        button_p.get("button_1"), -0.22, None, 0.5
    )
    button_p.moved(
        button_p.get("button_2"), -0.22, None, 0.5
    )
    button_p.moved(
        button_p.get("button_3"), -0.22, None, 0.5
    )
    button_p.moved(
        button_p.get("button_4"), -0.22, None, 0.5
    )

def _button_1_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not button_p.move_status:
        source(1, 3, ENEMY_EVENT, 30, {"level": 2})
        boot.set_fps(60)

def _button_2_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if boot.config.get_value("level", 0) >= 2 and  not button_p.move_status:
        source(2, 5, ENEMY_EVENT, 300, {"level": 3}, enemy_timer_spawn= 3000)
        boot.set_fps(60)

def _button_3_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if boot.config.get_value("level", 0) >= 3 and not button_p.move_status:
        source(3, 7, ENEMY_EVENT, 1500, {"level": 3.1}, enemy_timer_spawn= 2000)
        boot.set_fps(60)

def _button_4_callback_():
    boot.config.check({"effect": "True"}, boot.return_exit)
    if not button_p.move_status:
        button_p.set_func(button_p.get("button_4"), exit_level)
        _button_hide()

_buttons = (
    ("button_1", _button_1_callback_, "3"),
    ("button_2", _button_2_callback_, "4"),
    ("button_3", _button_3_callback_, "5"),
    ("button_4", _button_4_callback_, "6"),
)

def draw_menu_buttons():
    for button, callback, text_key in _buttons:
        button_p.animation(button_p.get(button))
        button_p.callback(button, callback)
        button_p.get_text(button, boot.standard_text.set_base_text(text_key))

def level():
    global _work
    #button_p.set_region("level")

    _button_get()

    boot.set_fps(60)

    def initialize():
        for event in boot.GLOBAL_EVENT.event_pool():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                boot.config.check({"effect": "True"}, boot.return_exit)
                if not button_p.move_status:
                    button_p.set_func(button_p.get("button_4"), exit_level)
                    _button_hide()

        boot.GLOBAL_EVENT.mouse.mouse_get()
        boot.background()

        draw_menu_buttons()
        boot.GLOBAL_EVENT.task.get_tasks()

        #boot.version_game()
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
