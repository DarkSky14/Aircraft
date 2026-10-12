import sys
import pygame as py
sys.path.append("..\\..")

from Aircraft.core.bootstrap import boot
from Aircraft.module import log
from Aircraft.module.UI import ButtonCollector

_work = True

def exit_language():
    global _work
    _work = False

#surf_m = SubSurface(500, 400)
#s = surf_m.surface(boot.d, 0, 200)

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

def _button1_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not boot.config.check({"language": "EN"}):
        boot.config.writer({"language": "EN"})
        boot.active_language.set_language(boot.ENGLISH.language)

def _button2_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not boot.config.check({"language": "UA"}):
        boot.config.writer({"language": "UA"})
        boot.active_language.set_language(boot.UKRAINIAN.language)

def _button3_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not boot.config.check({"language": "RU"}):
        boot.config.writer({"language": "RU"})
        boot.active_language.set_language(boot.RUSSIAN.language)

def _button_4_callback_():
    boot.config.check({"effect": "True"}, boot.return_exit)
    if not button_p.move_status:
        button_p.set_func(button_p.get("button_4"),exit_language)
        _button_hide()

_buttons = (
    ("button_1", _button1_callback_, "English"),
    ("button_2", _button2_callback_, "Українська"),
    ("button_3", _button3_callback_, "Русский"),
    ("button_4", _button_4_callback_, "6"),
)

def draw_menu_buttons():
    for button, callback, text_key in _buttons:
        button_p.animation(button_p.get(button))
        button_p.callback(button, callback)
        button_p.get_text(button, boot.standard_text.set_base_text(text_key))

def language_get():
    global _work
    #button_p.set_region("language")

    _button_get()

    boot.set_fps(60)
    #boot.GLOBAL_EVENT.mouse.set_config(0,200)
    sf = 0

    try:
        while _work:
            scroll_y = 0
            for event in boot.GLOBAL_EVENT.event_pool():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

                if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                    boot.config.check({"effect": "True"}, boot.return_exit)
                    if not button_p.move_status:
                        button_p.set_func(button_p.get("button_4"),exit_language)
                        _button_hide()

                elif event.type == py.MOUSEWHEEL:
                    scroll_y += event.y * 50
                    if -0 <= (sf+scroll_y) <= 200:
                        sf += scroll_y
                    else:
                        scroll_y = 0

                    #button_p.add_coord(height=scroll_y)
                    #button_p.add_coord(height=scroll_y)
                    #button_p.add_coord(height=scroll_y)
                    #button_p.add_coord(height=scroll_y)

            boot.GLOBAL_EVENT.mouse.mouse_get()
            boot.background()
            #s.fill((255, 255, 255))

            draw_menu_buttons()
            boot.GLOBAL_EVENT.task.get_tasks()

            #boot.version_game()
            boot.GLOBAL_EVENT.mouse.event_button_check(
                boot.standard_curs, boot.click_cursor, boot.sound_scroll
            )
            text = boot.big_text.set_base_text("2")
            boot.big_text.draw_text(text, 0.05 * boot.width, 0.20 * boot.height)

            boot.get_fps(coordinate=(0.0022*boot.width, boot.height))
            boot.tick_fps()
            boot.update_display()
    except Exception as e:
        log.exception("Unhandled error in language: %s", e)
        raise

    #boot.GLOBAL_EVENT.mouse.set_config(0, -100)
    _work = True


if __name__ == "__main__":
    boot.set_fps(60)
    language_get()
