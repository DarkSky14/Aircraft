from module import (
    button_modified, GLOBAL_EVENT, screen, music, update_display, 
    big_text, sound_scroll, procent, main_surface, conf_height,
    conf_width, fix_import, d, log, sound_menu, clicks, 
    return_exit, version_game, visible_cursor, standart_curs, 
    click_cursor, set_fps, tick_fps
)

from module.UI import SurfaceM

from pygame import QUIT, K_ESCAPE, KEYDOWN, image, transform, event, quit

_fon_obj = image.load(fix_import + "library/pictures/fon_.png").convert()
_fon = transform.scale(_fon_obj, screen)
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
    music.music_all(sound_menu)

_x_coord, y_coord = 536.5, 255.5

x_size = 350 * procent
y_size = 250 * procent

_surfM_ = SurfaceM(GLOBAL_EVENT, d, size_config=procent)
_surfM_.set_object(_x_coord * procent, y_coord * procent, (x_size, y_size))

x_c = _surfM_.get_x_pos()
y_c = _surfM_.get_y_pos()

_button1_ = button_modified.copy()
_button1_.set_object(x_c + (23 * procent), y_c + (85 * procent), (300, 30))
_button1_.text_change({"effect": "True"}, "8", "9")

_button2_ = button_modified.copy()
_button2_.set_object(
    _button1_.get_x_pos(),
    (_button1_.get_y_pos() + _button1_.get_size_y() + (10 * procent)),
    (300, 30),
)
_button2_.text_change({"music": "True"}, "8", "9")

_button3_ = button_modified.copy()
_button3_.set_object(
    _button2_.get_x_pos(),
    (_button2_.get_y_pos() + _button2_.get_size_y() + (20 * procent)),
    (300, 30),
)

def _button1_callback():
    _check = _button1_.check_config({"effect": "True"})
    if _check:
        clicks()
        _button1_.write_in_config({"effect": "False"})

    elif not _check:
        _button1_.write_in_config({"effect": "True"})

    else:
        _button1_.write_in_config({"effect": "True"})
        log.error(
            "Error in config file, missing 'effect' key. Default value 'True' was set."
        )

    _button1_.text_change({"effect": "True"}, "8", "9")

def _button2_callback():
    _button2_.check_config({"effect": "True"}, clicks)
    _check = _button2_.check_config({"music": "True"})

    if _check:
        _button2_.write_in_config({"music": "False"})
        sound()

    elif not _check:
        _button2_.write_in_config({"music": "True"})
        sound()

    else:
        _button2_.write_in_config({"music": "True"})
        log.error(
            "Error in config file, missing 'music' key. Default value 'True' was set."
        )
        sound()

    _button2_.text_change({"music": "True"}, "8", "9")

def _button3_callback():
    _button3_.check_config({"effect": "True"}, return_exit)
    exit_options()


def options(x_t=536.5, y_t=255.5):
    global _x_coord, y_coord, x_c, y_c, _runner, _work, _surfM_
    
    if x_t != _x_coord and y_t != y_coord:
        _x_coord, y_coord = x_t, y_t

        _surfM_ = SurfaceM(GLOBAL_EVENT, d, size_config=procent)
        _surfM_.set_object(_x_coord * procent, y_coord * procent, (x_size, y_size))
        x_c = _surfM_.get_x_pos()
        y_c = _surfM_.get_y_pos()

        _button1_.set_object(x_c + (23 * procent), y_c + (85 * procent), (300, 30))

        _button2_.set_object(
            _button1_.get_x_pos(),
            (_button1_.get_y_pos() + _button1_.get_size_y() + (10 * procent)),
            (300, 30),
        )

        _button3_.set_object(
            _button2_.get_x_pos(),
            (_button2_.get_y_pos() + _button2_.get_size_y() + (20 * procent)),
            (300, 30),
        )

    _fon.set_alpha(20)
    anim_time_fon = 0

    version_game()
    sound()
    visible_cursor()

    def initialize():
        for event_ in event.get():
            GLOBAL_EVENT.event = event_
            if GLOBAL_EVENT.event.type == QUIT:
                quit()
                exit()

            if GLOBAL_EVENT.comparison_type(KEYDOWN):
                if GLOBAL_EVENT.comparison_key(K_ESCAPE):
                    GLOBAL_EVENT.set_key(0)
                    quit_options()

        GLOBAL_EVENT.mouse_get()
        GLOBAL_EVENT.mouse_button_down()
        # surfM.update_pos()
        # surfM.animation_resize()
        _surfM_.main_work(quit_options)

        _button1_.Button(_button1_callback)
        _button1_.get_text_self("12")

        _button2_.Button(_button2_callback)
        _button2_.get_text_self("10")

        _button3_.Button(_button3_callback)
        _button3_.get_text_self("6")

        GLOBAL_EVENT.mouse_button_down()
        GLOBAL_EVENT.event_button_check(standart_curs, click_cursor, sound_scroll)
        big_text.get_set_text("1", x_c + (45 * procent), y_c + (25 * procent))

        # get_fps(coordinate=(3, Surface.height - 20))
        tick_fps()
        update_display()

    while _work:
        if anim_time_fon <= 180:
            anim_time_fon += 20
            main_surface.blit(_fon, (0 + conf_width, 0 + conf_height))

        initialize()

    else:
        _work = True
        if not _runner:
            _runner = True
            return False
        return True


if __name__ == "__main__":
    set_fps(60)
    options()
