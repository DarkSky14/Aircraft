import sys
import pygame as py
sys.path.append("..\\..")

from Aircraft.module.UI.button import CanvasButton, ButtonCollector
from Aircraft.module.UI.render import Line

from Aircraft.module import (
    log, ImageLoader
)
from Aircraft.core.bootstrap import boot

_fon = ImageLoader("assets/pictures/fon_.png", boot.screen).show()

_work = True
_runner = True

def quit_options():
    global _work
    _work = False

def exit_options():
    global _runner
    _runner = False
    quit_options()

def sound():
    boot.music.music_all(boot.sound_menu)

class CoordinateOptions:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def get_x(self):
        return self.x_coord

    def get_y(self):
        return self.y_coord

    def set_x(self, x):
        self.x_coord = x

    def set_y(self, y):
        self.y_coord = y

canvas_conf = CoordinateOptions(0.1, 0.1) #0.390, 0.336
x_coord, y_coord = 0,0

x_size = 0.8
y_size = 0.8

_surfM_ = CanvasButton(boot.GLOBAL_EVENT, boot.main_surface, (boot.width, boot.height))
_surfM_.set_object(
    canvas_conf.get_x() * boot.width,
    canvas_conf.get_y() * boot.height,
    (x_size, y_size)
)

lines = Line(boot.main_surface)

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
    _surfM_.x + (0.0168 * boot.width),
    _surfM_.y + (0.112 * boot.height),
    (0.22, 0.041)
)

button_p.set_object(
    "button_2",
    button_p.get("button_1").x,
    (button_p.get("button_1").y + button_p.get("button_1").size_y + (0.0132 * boot.height)),
    (0.22, 0.041),
)

button_p.set_object(
    "button_3",
    button_p.get("button_2").x,
    (button_p.get("button_2").y + button_p.get("button_2").size_y + (0.0132 * boot.height)),
    (0.22, 0.041),
)

button_p.set_object(
    "button_4",
    button_p.get("button_3").x,
    (button_p.get("button_3").y + button_p.get("button_3").size_y + (0.033 * boot.height)),
    (0.22, 0.041),
)

def _button1_callback():
    if boot.config.check({"effect": "True"}):
        boot.clicks()
        boot.config.writer({"effect": "False"})
    else:
        boot.config.writer({"effect": "True"})

def _button2_callback():
    boot.config.check({"effect": "True"}, boot.clicks)
    if boot.config.check({"music": "True"}):
        boot.config.writer({"music": "False"})
    else:
        boot.config.writer({"music": "True"})
    sound()

def _button3_callback():
    boot.config.check({"effect": "True"}, boot.clicks)
    if boot.config.check({"animation": "True"}):
        boot.config.writer({"animation": "False"})
    else:
        boot.config.writer({"animation": "True"})
    sound()

def _button4_callback():
    boot.config.check({"effect": "True"}, boot.return_exit)
    exit_options()

def options():
    global x_coord, y_coord, _runner, _work
    #button_p.set_region("settings")

    _fon.set_alpha(20)
    anim_time_fon = 0

    boot.version_game()
    sound()
    boot.visible_cursor()

    def initialize():
        for event in boot.GLOBAL_EVENT.event_pool():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    quit_options()

        boot.GLOBAL_EVENT.mouse.mouse_get()
        _surfM_.callback(quit_options)

        button_p.callback("button_1", _button1_callback)
        text = boot.standard_text.set_base_text("12")
        check = boot.standard_text.set_change_text({"effect": "True"}, "8", "9")
        button_p.get_text("button_1","{} {}".format(text, check))

        button_p.callback("button_2",_button2_callback)
        text = boot.standard_text.set_base_text("10")
        check = boot.standard_text.set_change_text({"music": "True"}, "8", "9")
        button_p.get_text("button_2","{} {}".format(text, check))

        button_p.callback("button_3", _button3_callback)
        text = boot.standard_text.set_base_text("13")
        check = boot.standard_text.set_change_text({"animation": "True"}, "8", "9")
        button_p.get_text("button_3","{} {}".format(text, check))

        button_p.callback("button_4", _button4_callback)
        button_p.get_text("button_4", boot.standard_text.set_base_text("6"))

        boot.GLOBAL_EVENT.mouse.event_button_check(
            boot.standard_curs, boot.click_cursor, boot.sound_scroll
        )
        text = boot.standard_text.set_base_text("1")
        boot.big_text.draw_text(
            text, (0.5 * boot.width), (0.12 * boot.height), rect="centerx"
        )

        lines.draw_object(
            (0,0,0),
            ((0.11 * boot.width), 0.2 * boot.height),
            ((0.89 * boot.width), 0.2 * boot.height),
            round(0.001 * boot.width)
        )

        lines.draw_object(
            (0, 0, 0),
            ((0.11 * boot.width), 0.85 * boot.height),
            ((0.89 * boot.width), 0.85 * boot.height),
            round(0.001 * boot.width)
        )

        boot.get_fps(coordinate=((0.12 * boot.width), (0.895 * boot.height)))
        boot.version_game()
        boot.tick_fps()
        #boot.auto_resize_surface.blit(boot.main_surface)
        boot.update_display()


    try:
        while _work:
            if anim_time_fon <= 180:
                if boot.config.check({"animation": "True"}):
                    anim_time_fon += 20
                    boot.main_surface.blit(
                        _fon, (0 + boot.conf_width, 0 + boot.conf_height)
                    )

                else:
                    anim_time_fon = 181
                    _fon.set_alpha(180)
                    boot.main_surface.blit(
                         _fon, (0 + boot.conf_width, 0 + boot.conf_height)
                    )
            initialize()
    except Exception as e:
        log.exception("Unhandled error in settings: %s", e)
        raise

    else:
        _work = True
        if not _runner:
            _runner = True
            return False
        return True


if __name__ == "__main__":
    boot.set_fps(60)
    options()
