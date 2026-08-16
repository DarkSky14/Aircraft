from module.bootstrap import boot
from module import log, py, sys

_work = True

def exit_language():
    global _work
    _work = False

def update_text(lang):
    boot.standard_text.set_language(lang)
    boot.big_text.set_language(lang)


_button1_ = boot.button_modified.copy()
_button1_.set_object((-300 * boot.procent), (220 * boot.procent), (300, 30))

_button2_ = boot.button_modified.copy()
_button2_.set_object(
    (-300 * boot.procent),
    (_button1_.y + _button1_.size_y + (10 * boot.procent)),
    (300, 30),
)

_button4_ = boot.button_modified.copy()
_button4_.set_object(
    (-300 * boot.procent),
    (_button2_.y + _button2_.size_y + (30 * boot.procent)),
    (300, 30),
)

def _button1_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not boot.config.check({"language": "EN"}):
        boot.config.writer({"language": "EN"})
        update_text(boot.ENGLISH)

def _button2_callback_():
    boot.config.check({"effect": "True"}, boot.clicks)
    if not boot.config.check({"language": "UA"}):
        boot.config.writer({"language": "UA"})
        update_text(boot.UKRAINIAN)

def _button_4_callback_():
    boot.config.check({"effect": "True"}, boot.return_exit)
    exit_language()

_buttons = (
    (_button1_, _button1_callback_, "English"),
    (_button2_, _button2_callback_, "Українська"),
    (_button4_, _button_4_callback_, "6"),
)

def draw_menu_buttons():
    for button, callback, text_key in _buttons:
        button.callback(callback)
        button.animation()
        button.get_text(boot.standard_text, boot.standard_text.set_base_text(text_key))

def language_get():
    global _work

    # surf_m = UI.SurfaceM(e, Surface.main_surface)

    _button1_.moved(50, None, 300)
    _button2_.moved(50, None, 300)
    _button4_.moved(50, None, 300)

    #def button_3():
        # surfM.callback(50, (220 + s*2), (300, 30), 75, (221 + s*2), 13, clicks, Русский, "Language", {"language": "RU"})
        #standart_text.draw_text("Русский", 75, (221 * 2), (0, 0, 0))

    boot.set_fps(60)

    def initialize():
        boot.GLOBAL_EVENT.event_pool()
        if boot.GLOBAL_EVENT.comparison_type(py.QUIT):
                py.quit()
                sys.exit()

        if boot.GLOBAL_EVENT.comparison_type(py.KEYDOWN) and boot.GLOBAL_EVENT.comparison_key(
                py.K_ESCAPE
            ):
                boot.config.check({"effect": "True"}, boot.return_exit)
                exit_language()

        boot.GLOBAL_EVENT.mouse_get()
        boot.GLOBAL_EVENT.mouse_button_down()
        boot.background()

        draw_menu_buttons()

        boot.version_game()
        boot.GLOBAL_EVENT.event_button_check(
            boot.standard_curs, boot.click_cursor, boot.sound_scroll
        )
        text = boot.big_text.set_base_text("2")
        boot.big_text.get_set_text(text, 70 * boot.procent, 150 * boot.procent)

        boot.get_fps(coordinate=(3, boot.height - (20 * boot.procent)))
        boot.tick_fps()
        boot.update_display()

    while _work:
        try:
            initialize()
        except Exception:
            log.exception("Unhandled error in language")
            raise

    _work = True


if __name__ == "__main__":
    boot.set_fps(60)
    language_get()
