import sys
sys.path.append("..")

from module import (
    log, py, ImageLoader
)
from module.UI import ButtonCollector
from cached.bootstrap import boot

from menu.settings_menu import options, canvas_conf
from menu.language_menu import language_get
from menu.level_menu import level

# Setup pygame/window -----------------------------
icon = ImageLoader("Aircraft.ico", (32,32)).show()

py.display.set_caption("Aircraft", "Aircraft")
py.display.set_icon(icon)

work = True

def exit_game():
    global work
    work = False

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


def _button_1_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not button_p.move_status:
        button_p.set_func(button_p.get("button_1"), level, _button_get)
        _button_hide()

def _button_2_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not button_p.move_status:
        #canvas_conf.set_x(0.018), canvas_conf.set_y(0.20)
        button_p.set_func(button_p.get("button_2"), options, _button_get)
        _button_hide()

def _button_3_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not button_p.move_status:
        button_p.set_func(button_p.get("button_3"), language_get, _button_get)
        _button_hide()

def _button_4_callback_():
    boot.config.check({"effect": "True"}, boot.return_exit)
    if not button_p.move_status:
        exit_game()

_buttons = (
    ("button_1", _button_1_callback_, "0"),
    ("button_2", _button_2_callback_, "1"),
    ("button_3", _button_3_callback_, "2"),
    ("button_4", _button_4_callback_, "6"),
)

def draw_menu_buttons():
    for button, callback, text_key in _buttons:
        button_p.animation(button_p.get(button))
        button_p.callback(button, callback)
        button_p.get_text(button, boot.standard_text.set_base_text(text_key))


def main_menu():
    global work

    _button_get()

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

            #boot.version_game()
            boot.GLOBAL_EVENT.mouse.event_button_check(
                boot.standard_curs, boot.click_cursor, boot.sound_scroll
            )
            boot.big_text.draw_text(
                boot.big_text.set_base_text("7"), 0.05 * boot.width, 0.20 * boot.height
            )

            #boot.get_fps(coordinate=(0.0022*boot.width, boot.height))
            boot.tick_fps()
            boot.update_display()

    except Exception as e:
        log.exception("Unhandled error in main: %s", e)
        raise

if __name__ == "__main__":
    log.info("Successful start...")
    main_menu()
