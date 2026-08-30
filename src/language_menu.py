from module.bootstrap import boot, SubSurface
from module import log, py, sys

_work = True

def exit_language():
    global _work
    _work = False

#surf_m = SubSurface(500, 400)
#s = surf_m.surface(boot.d, 0, 200)

_button1_ = boot.button_modified.copy()
_button1_.set_object(
    (-300 * boot.procent),
    (220 * boot.procent),
    (300, 30)
)#.set_surface(s)

_button2_ = boot.button_modified.copy()
_button2_.set_object(
    (-300 * boot.procent),
    (_button1_.y + _button1_.size_y + (10 * boot.procent)),
    (300, 30),
)#.set_surface(s)

_button4_ = boot.button_modified.copy()
_button4_.set_object(
    (-300 * boot.procent),
    (_button2_.y + _button2_.size_y + (30 * boot.procent)),
    (300, 30),
)#.set_surface(s)

def _button_get():
    _button1_.moved(50, None, 300)
    _button2_.moved(50, None, 300)
    #_button3_.moved(50, None, 300)
    _button4_.moved(50, None, 300)

def _button_hide():
    _button1_.moved(-300, None, 300)
    _button2_.moved(-300, None, 300)
    # _button3_.moved(-300, None, 300)
    _button4_.moved(-300, None, 300)

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

def _button_4_callback_():
    boot.config.check({"effect": "True"}, boot.return_exit)
    _button4_.set_func(exit_language, _button_get)
    _button_hide()

_buttons = (
    (_button1_, _button1_callback_, "English"),
    (_button2_, _button2_callback_, "Українська"),
    (_button4_, _button_4_callback_, "6"),
)

def draw_menu_buttons():
    for button, callback, text_key in _buttons:
        button.animation()
        button.callback(callback)
        button.get_text(boot.standard_text, boot.standard_text.set_base_text(text_key))

_button_get()

def language_get():
    global _work

    #def button_3():
        # surfM.callback(50, (220 + s*2), (300, 30), 75, (221 + s*2), 13, clicks, Русский, "Language", {"language": "RU"})
        #standart_text.draw_text("Русский", 75, (221 * 2), (0, 0, 0))

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
                    if not _button4_.move_status:
                        _button4_.set_func(exit_language, _button_get)
                        _button_hide()

                elif event.type == py.MOUSEWHEEL:
                    scroll_y += event.y * 50
                    if -0 <= (sf+scroll_y) <= 200:
                        sf += scroll_y
                    else:
                        scroll_y = 0

                    _button1_.add_coord(height=scroll_y)
                    _button2_.add_coord(height=scroll_y)
                    _button4_.add_coord(height=scroll_y)

            boot.GLOBAL_EVENT.mouse.mouse_get()
            boot.background()
            #s.fill((255, 255, 255))

            draw_menu_buttons()
            boot.GLOBAL_EVENT.task.get_tasks()

            boot.version_game()
            boot.GLOBAL_EVENT.mouse.event_button_check(
                boot.standard_curs, boot.click_cursor, boot.sound_scroll
            )
            text = boot.big_text.set_base_text("2")
            boot.big_text.draw_text(text, 70 * boot.procent, 150 * boot.procent)

            boot.get_fps(coordinate=(3, boot.height))
            boot.tick_fps()
            boot.update_display()
    except Exception:
        log.exception("Unhandled error in language")
        raise

    #boot.GLOBAL_EVENT.mouse.set_config(0, -100)
    _work = True


if __name__ == "__main__":
    boot.set_fps(60)
    language_get()
