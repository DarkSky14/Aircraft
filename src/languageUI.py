from module import (
    button_modified, standard_text, GLOBAL_EVENT, background,
    update_display, big_text, sound_scroll, procent, height, ENGLISH,
    UKRAINIAN, config, clicks, return_exit, version_game, standard_curs,
    click_cursor, set_fps, get_fps, tick_fps, active_language
)

from pygame import QUIT, K_ESCAPE, KEYDOWN, event, quit

_work = True

def exit_language():
    global _work
    _work = False

def update_text(lang):
    standard_text.set_language(lang)
    big_text.set_language(lang)
    button_modified.set_language(lang)


_button1_ = button_modified.copy()
_button1_.set_object((-300 * procent), (220 * procent), (300, 30))

_button2_ = button_modified.copy()
_button2_.set_object(
    (-300 * procent),
    (_button1_.get_y_pos() + _button1_.get_size_y() + (10 * procent)),
    (300, 30),
)

_button4_ = button_modified.copy()
_button4_.set_object(
    (-300 * procent),
    (_button2_.get_y_pos() + _button2_.get_size_y() + (30 * procent)),
    (300, 30),
)

def _button1_callback_():
    global language
    _button1_.check_config({"effect": "True"}, clicks)
    if not _button1_.check_config({"language": "EN"}):
        _button1_.write_in_config({"language": "EN"})
        language = ENGLISH
        update_text(language)

def _button2_callback_():
    global language
    _button2_.check_config({"effect": "True"}, clicks)
    if not _button2_.check_config({"language": "UA"}):
        _button2_.write_in_config({"language": "UA"})
        language = UKRAINIAN
        update_text(language)

def _button_4_callback_():
    _button4_.check_config({"effect": "True"}, return_exit)
    exit_language()


def language_get():
    global _work

    # surf_m = UI.SurfaceM(e, Surface.main_surface)

    _button1_.moved(50, None, 300)
    _button2_.moved(50, None, 300)
    _button4_.moved(50, None, 300)

    def button_1():
        _button1_.animation()
        _button1_.Button(_button1_callback_)
        _button1_.get_text("English", (0, 0, 0))

    def button_2():
        _button2_.animation()
        _button2_.Button(_button2_callback_)
        _button2_.get_text("Українська", (0, 0, 0))

    #def button_3():
        # surfM.Button(50, (220 + s*2), (300, 30), 75, (221 + s*2), 13, clicks, Русский, "Language", {"language": "RU"})
        #standart_text.draw_text("Русский", 75, (221 * 2), (0, 0, 0))

    def button_4():
        _button4_.animation()
        _button4_.Button(_button_4_callback_)
        text = standard_text.set_base_text("6")
        _button4_.get_text(text)


    set_fps(60)

    def initialize():
        for event_ in event.get():
            GLOBAL_EVENT.event = event_
            if GLOBAL_EVENT.event.type == QUIT:
                quit()
                exit()

            if GLOBAL_EVENT.comparison_type(KEYDOWN) and GLOBAL_EVENT.comparison_key(
                K_ESCAPE
            ):
                config.check({"effect": "True"}, return_exit)
                GLOBAL_EVENT.set_key(0)
                exit_language()

        GLOBAL_EVENT.mouse_get()
        background()

        button_1()
        button_2()
        button_4()

        version_game()
        GLOBAL_EVENT.mouse_button_down()
        GLOBAL_EVENT.event_button_check(standard_curs, click_cursor, sound_scroll)
        text = big_text.set_base_text("2")
        big_text.get_set_text(text, 70 * procent, 150 * procent)

        get_fps(coordinate=(3, height - (20 * procent)))
        tick_fps()
        update_display()

    while _work:
        initialize()

    _work = True


if __name__ == "__main__":
    set_fps(60)
    language_get()
