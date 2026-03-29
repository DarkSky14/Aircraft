from module import (
    button_modified, standart_text, GLOBAL_EVENT, background, work,
    update_display, big_text, sound_scroll, procent, height, config,
    pygame,
)

from module.menu_client import (
    clicks, return_exit, version_game, standart_curs, click_cursor,
)

from game import sourse

from pygame import QUIT, K_ESCAPE, KEYDOWN

from module.game_client import set_fps, get_fps, tick_fps


def level():
    global work
    from module.game_client import sw1, sh1, CREATE_ENEMY1, max_score1
    from module.game_client import sw2, sh2, CREATE_ENEMY2, max_score2
    from module.game_client import sw3, sh3, CREATE_ENEMY3, max_score3

    def exitLEVEL():
        global work
        work = False

    button1 = button_modified.copy()
    button1.set_object(-300 * procent, 220 * procent, (300, 30))
    button1.moved(50, None, 300)

    button2 = button_modified.copy()
    button2.set_object(
        button1.get_x_pos(),
        (button1.get_y_pos() + button1.get_size_y() + (10 * procent)),
        (300, 30),
    )
    button2.moved(50, None, 300)

    button3 = button_modified.copy()
    button3.set_object(
        button2.get_x_pos(),
        (button2.get_y_pos() + button2.get_size_y() + (10 * procent)),
        (300, 30),
    )
    button3.moved(50, None, 300)

    button4 = button_modified.copy()
    button4.set_object(
        button3.get_x_pos(),
        (button3.get_y_pos() + button3.get_size_y() + (30 * procent)),
        (300, 30),
    )
    button4.moved(50, None, 300)

    def button_1():
        def lvl1():
            sourse(sw1, sh1, CREATE_ENEMY1, max_score1, {"level": 2})

        def button():
            button1.check_config({"effect": "True"}, clicks)
            lvl1()
            set_fps(60)

        button1.animation()
        button1.Button(button)
        button1.get_text(standart_text, "3")

    def button_2():
        def l2():
            def lvl2():
                sourse(sw2, sh2, CREATE_ENEMY2, max_score2, {"level": 3})

            if config.get_value("level") >= 2:
                lvl2()

        def button():
            button2.check_config({"effect": "True"}, clicks)
            l2()
            set_fps(60)

        button2.animation()
        button2.Button(button)
        button2.get_text(standart_text, "4")

    def button_3():
        def l3():
            def lvl3():
                sourse(sw3, sh3, CREATE_ENEMY3, max_score3, {"level": 3.1})

            if config.get_value("level") >= 3:
                lvl3()

        def button():
            button3.check_config({"effect": "True"}, clicks)
            l3()
            set_fps(60)

        button3.animation()
        button3.Button(button)
        button3.get_text(standart_text, "5")

    def button_4():
        def button():
            button4.check_config({"effect": "True"}, return_exit)
            exitLEVEL()

        button4.animation()
        button4.Button(button)
        button4.get_text(standart_text, "6")

    set_fps(60)

    def initialiaze():
        for event in pygame.event.get():
            GLOBAL_EVENT.event = event
            if GLOBAL_EVENT.event.type == QUIT:
                pygame.quit()
                exit()

            GLOBAL_EVENT.mouse_get()
            GLOBAL_EVENT.MOUSEBUTTONDOWN()

            if GLOBAL_EVENT.comparison_type(KEYDOWN) and GLOBAL_EVENT.comparison_key(
                K_ESCAPE
            ):
                config.check({"effect": "True"}, return_exit)
                GLOBAL_EVENT.set_key(0)
                exitLEVEL()

        background()

        button_1()
        button_2()
        button_3()
        button_4()

        version_game()
        GLOBAL_EVENT.MOUSEBUTTONDOWN()
        GLOBAL_EVENT.event_button_check(standart_curs, click_cursor, sound_scroll)
        big_text.get_set_text("11", 70 * procent, 150 * procent)

        get_fps(coordinate=(3, height - (20 * procent)))
        tick_fps()
        update_display()

    while work:
        initialiaze()

    work = True


if __name__ == "__main__":
    set_fps(60)
    level()
