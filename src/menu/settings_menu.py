import sys
sys.path.append("..")

from module.UI.button import CanvasButton

from module import (
    log, py, sys, ImageLoader
)
from cached.bootstrap import boot

_fon = ImageLoader("pictures/fon_.png", boot.screen).show()

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

x_size = 0.8#0.255
y_size = 0.8#0.33

_surfM_ = CanvasButton(boot.GLOBAL_EVENT, boot.main_surface, (boot.width, boot.height))
_surfM_.set_object(
    canvas_conf.get_x() * boot.width,
    canvas_conf.get_y() * boot.height,
    (x_size, y_size)
)

_button1_ = boot.button_modified.copy()
_button1_.set_object(
    _surfM_.x + (0.0168 * boot.width),
    _surfM_.y + (0.112 * boot.height),
    (0.22, 0.041)
)

_button2_ = boot.button_modified.copy()
_button2_.set_object(
    _button1_.x,
    (_button1_.y + _button1_.size_y + (0.0132 * boot.height)),
    (0.22, 0.041),
)

_button3_ = boot.button_modified.copy()
_button3_.set_object(
    _button2_.x,
    (_button2_.y + _button2_.size_y + (0.0132 * boot.height)),
    (0.22, 0.041),
)

_button4_ = boot.button_modified.copy()
_button4_.set_object(
    _button3_.x,
    (_button3_.y + _button3_.size_y + (0.026 * boot.height)),
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
    
    if canvas_conf.get_x() != x_coord or canvas_conf.get_y() != y_coord:
        x_coord, y_coord = canvas_conf.get_x(), canvas_conf.get_y()

        _surfM_.set_object(
            x_coord * boot.width,
            y_coord * boot.height,
            (x_size, y_size)
        )

        _button1_.set_object(
            _surfM_.x + (0.0168 * boot.width),
            _surfM_.y + (0.112 * boot.height),
            (0.22, 0.041)
        )

        _button2_.set_object(
            _button1_.x,
            (_button1_.y + _button1_.size_y + (0.0132 * boot.height)),
            (0.22, 0.041),
        )

        _button3_.set_object(
            _button2_.x,
            (_button2_.y + _button2_.size_y + (0.0132 * boot.height)),
            (0.22, 0.041),
        )

        _button4_.set_object(
            _button3_.x,
            (_button3_.y + _button3_.size_y + (0.026 * boot.height)),
            (0.22, 0.041),
        )

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

        _button1_.callback(_button1_callback)
        text = boot.standard_text.set_base_text("12")
        check = boot.standard_text.set_change_text({"effect": "True"}, "8", "9")
        _button1_.get_text("{} {}".format(text, check))

        _button2_.callback(_button2_callback)
        text = boot.standard_text.set_base_text("10")
        check = boot.standard_text.set_change_text({"music": "True"}, "8", "9")
        _button2_.get_text("{} {}".format(text, check))

        _button3_.callback(_button3_callback)
        text = boot.standard_text.set_base_text("13")
        check = boot.standard_text.set_change_text({"animation": "True"}, "8", "9")
        _button3_.get_text("{} {}".format(text, check))

        _button4_.callback(_button4_callback)
        _button4_.get_text(boot.standard_text.set_base_text("6"))

        boot.GLOBAL_EVENT.mouse.event_button_check(
            boot.standard_curs, boot.click_cursor, boot.sound_scroll
        )
        text = boot.standard_text.set_base_text("1")
        boot.big_text.draw_text(
            text, _surfM_.x + (0.035 * boot.width), _surfM_.y + (0.04 * boot.height)
        )

        #boot.get_fps(coordinate=(3, boot.height - (20 * boot.procent)))
        boot.tick_fps()
        boot.update_display()


    try:
        while _work:
            if anim_time_fon <= 180:
                anim_time_fon += 20
                boot.auto_resize_surface.blit(_fon, (0 + boot.conf_width, 0 + boot.conf_height))
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
