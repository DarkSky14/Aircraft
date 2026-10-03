import sys
sys.path.append("..")

from module.UI.button import CanvasButton

from module import (
    log, py, sys, ImageLoader
)
from module.bootstrap import boot

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

canvas_conf = CoordinateOptions(536.5, 255.5)
x_coord, y_coord = 0,0

x_size = 350 * boot.procent
y_size = 250 * boot.procent

_surfM_ = CanvasButton(boot.GLOBAL_EVENT, boot.d, boot.procent)
_surfM_.set_object(
    canvas_conf.get_x() * boot.procent, canvas_conf.get_y() * boot.procent, (x_size, y_size)
)

_button1_ = boot.button_modified.copy()
_button1_.set_object(_surfM_.x + (23 * boot.procent), _surfM_.y + (85 * boot.procent), (300, 30))

_button2_ = boot.button_modified.copy()
_button2_.set_object(
    _button1_.x,
    (_button1_.y + _button1_.size_y + (10 * boot.procent)),
    (300, 30),
)

_button3_ = boot.button_modified.copy()
_button3_.set_object(
    _button2_.x,
    (_button2_.y + _button2_.size_y + (20 * boot.procent)),
    (300, 30),
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
    boot.config.check({"effect": "True"}, boot.return_exit)
    exit_options()

def options():
    global x_coord, y_coord, _runner, _work
    
    if canvas_conf.get_x() != x_coord or canvas_conf.get_y() != y_coord:
        x_coord, y_coord = canvas_conf.get_x(), canvas_conf.get_y()

        _surfM_.set_object(x_coord * boot.procent, y_coord * boot.procent, (x_size, y_size))

        _button1_.set_object(_surfM_.x + (23 * boot.procent), _surfM_.y + (85 * boot.procent), (300, 30))

        _button2_.set_object(
            _button1_.x,
            (_button1_.y + _button1_.size_y + (10 * boot.procent)),
            (300, 30),
        )

        _button3_.set_object(
            _button2_.x,
            (_button2_.y + _button2_.size_y + (20 * boot.procent)),
            (300, 30),
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
        _button1_.get_text(boot.standard_text, "{} {}".format(text, check))

        _button2_.callback(_button2_callback)
        text = boot.standard_text.set_base_text("10")
        check = boot.standard_text.set_change_text({"music": "True"}, "8", "9")
        _button2_.get_text(boot.standard_text, "{} {}".format(text, check))

        _button3_.callback(_button3_callback)
        text = boot.standard_text.set_base_text("6")
        _button3_.get_text(boot.standard_text, text)

        boot.GLOBAL_EVENT.mouse.event_button_check(
            boot.standard_curs, boot.click_cursor, boot.sound_scroll
        )
        text = boot.standard_text.set_base_text("1")
        boot.big_text.draw_text(
            text, _surfM_.x + (45 * boot.procent), _surfM_.y + (25 * boot.procent)
        )

        #boot.get_fps(coordinate=(3, boot.height - (20 * boot.procent)))
        boot.tick_fps()
        boot.update_display()


    try:
        while _work:
            if anim_time_fon <= 180:
                anim_time_fon += 20
                boot.main_surface.blit(_fon, (0 + boot.conf_width, 0 + boot.conf_height))
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
