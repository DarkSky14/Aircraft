from module import boot
import module
from game import source
from pygame import QUIT, K_ESCAPE, KEYDOWN, quit, event, USEREVENT

#boot = module
_work = True

def exit_level():
    global _work
    _work = False

_button1_ = boot.button_modified.copy()
_button1_.set_object((-300 * boot.procent), (220 * boot.procent), (300, 30))

_button2_ = boot.button_modified.copy()
_button2_.set_object(
    (-300 * boot.procent),
    (_button1_.get_y_pos() + _button1_.get_size_y() + (10 * boot.procent)),
    (300, 30),
)

_button3_ = boot.button_modified.copy()
_button3_.set_object(
    (-300 * boot.procent),
    (_button2_.get_y_pos() + _button2_.get_size_y() + (10 * boot.procent)),
    (300, 30),
)

_button4_ = boot.button_modified.copy()
_button4_.set_object(
    (-300 * boot.procent),
    (_button3_.get_y_pos() + _button3_.get_size_y() + (25 * boot.procent)),
    (300, 30),
)

def _button1_callback_():
    _button1_.check_config({"effect": "True"}, boot.clicks)
    source(1, 3, USEREVENT + 2, 30, {"level": 2})
    boot.set_fps(60)

def _button_2_callback_():
    _button2_.check_config({"effect": "True"}, boot.clicks)
    if boot.config.get_value("level") >= 2:
        source(2, 5, USEREVENT + 3, 300, {"level": 3}, enemy_timer_spawn= 3000)
        boot.set_fps(60)

def _button_3_callback_():
    _button3_.check_config({"effect": "True"}, boot.clicks)
    if boot.config.get_value("level") >= 3:
        source(3, 7, USEREVENT + 4, 1500, {"level": 3.1}, enemy_timer_spawn= 2000)
        boot.set_fps(60)

def _button_4_callback_():
    _button4_.check_config({"effect": "True"}, boot.return_exit)
    exit_level()

def button_1():
    _button1_.animation()
    _button1_.Button(_button1_callback_)
    text = boot.standard_text.set_base_text("3")
    _button1_.get_text(text)

def button_2():
    _button2_.animation()
    _button2_.Button(_button_2_callback_)
    text = boot.standard_text.set_base_text("4")
    _button2_.get_text(text)

def button_3():
    _button3_.animation()
    _button3_.Button(_button_3_callback_)
    text = boot.standard_text.set_base_text("5")
    _button3_.get_text(text)

def button_4():
    _button4_.animation()
    _button4_.Button(_button_4_callback_)
    text = boot.standard_text.set_base_text("6")
    _button4_.get_text(text)


def level():
    global _work

    _button1_.moved(50, None, 300)
    _button2_.moved(50, None, 300)
    _button3_.moved(50, None, 300)
    _button4_.moved(50, None, 300)

    boot.set_fps(60)

    def initialize():
        for event_ in event.get():
            boot.GLOBAL_EVENT.event = event_
            if boot.GLOBAL_EVENT.event.type == QUIT:
                quit()
                exit()

            if boot.GLOBAL_EVENT.comparison_type(KEYDOWN) and boot.GLOBAL_EVENT.comparison_key(
                K_ESCAPE
            ):
                boot.config.check({"effect": "True"}, boot.return_exit)
                boot.GLOBAL_EVENT.set_key(0)
                exit_level()

        boot.GLOBAL_EVENT.mouse_get()
        boot.GLOBAL_EVENT.mouse_button_down()
        boot.background()

        button_1()
        button_2()
        button_3()
        button_4()

        boot.version_game()
        boot.GLOBAL_EVENT.mouse_button_down()
        boot.GLOBAL_EVENT.event_button_check(
            boot.standard_curs, boot.click_cursor, boot.sound_scroll
        )
        text = boot.standard_text.set_base_text("11")
        boot.big_text.get_set_text(text, 70 * boot.procent, 150 * boot.procent)

        boot.get_fps(coordinate=(3, boot.height - (20 * boot.procent)))
        boot.tick_fps()
        boot.update_display()

    while _work:
        initialize()

    _work = True


if __name__ == "__main__":
    boot.set_fps(60)
    level()
