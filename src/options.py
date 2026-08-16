from module.UI import CanvasButton

from module import (
    absolute_import, log, py, sys
)
from module.bootstrap import boot

_fon_obj = py.image.load(absolute_import("pictures/fon_.png")).convert()
_fon = py.transform.scale(_fon_obj, boot.screen)
log.info("Background image options setup complete.")

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

_x_coord, y_coord = 536.5, 255.5

x_size = 350 * boot.procent
y_size = 250 * boot.procent

_surfM_ = CanvasButton(boot.GLOBAL_EVENT, boot.d, boot.procent)
_surfM_.set_object(_x_coord * boot.procent, y_coord * boot.procent, (x_size, y_size))

x_c = _surfM_.x
y_c = _surfM_.y

_button1_ = boot.button_modified.copy()
_button1_.set_object(x_c + (23 * boot.procent), y_c + (85 * boot.procent), (300, 30))

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

def options(x_t=536.5, y_t=255.5):
    global _x_coord, y_coord, x_c, y_c, _runner, _work, _surfM_
    
    if x_t != _x_coord or y_t != y_coord:
        _x_coord, y_coord = x_t, y_t

        _surfM_.set_object(_x_coord * boot.procent, y_coord * boot.procent, (x_size, y_size))
        x_c = _surfM_.x
        y_c = _surfM_.y

        _button1_.set_object(x_c + (23 * boot.procent), y_c + (85 * boot.procent), (300, 30))

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
        boot.GLOBAL_EVENT.event_pool()
        if boot.GLOBAL_EVENT.comparison_type(py.QUIT):
            py.quit()
            sys.exit()

        if boot.GLOBAL_EVENT.comparison_type(py.KEYDOWN):
                if boot.GLOBAL_EVENT.comparison_key(py.K_ESCAPE):
                    quit_options()

        boot.GLOBAL_EVENT.mouse_get()
        boot.GLOBAL_EVENT.mouse_button_down()
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

        boot.GLOBAL_EVENT.event_button_check(
            boot.standard_curs, boot.click_cursor, boot.sound_scroll
        )
        text = boot.standard_text.set_base_text("1")
        boot.big_text.get_set_text(
            text, x_c + (45 * boot.procent), y_c + (25 * boot.procent)
        )

        # get_fps(coordinate=(3, Surface.height - 20))
        boot.tick_fps()
        boot.update_display()

    while _work:
        try:
            if anim_time_fon <= 180:
                anim_time_fon += 20
                boot.main_surface.blit(_fon, (0 + boot.conf_width, 0 + boot.conf_height))
            initialize()
        except Exception:
            log.exception("Unhandled error in main")
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
