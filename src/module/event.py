from pygame import event, time, mouse, MOUSEBUTTONDOWN


class EventControl:
    def __init__(
        self, debounce_ms=200, config_width: float = 0, config_height: float = 0
    ):
        self.debounce_ms = debounce_ms
        self._last_click_time = 0
        self.click = False
        self.choose_button = 0
        self.fake_choose_button = 0
        self.wait_button = 0
        self.config_width = config_width
        self.config_height = config_height
        self.mx, self.my = 0, 0
        self.event = event.Event

    def event_pool(self):
        for eventful in event.get():
            self.event = eventful

    def mouse_get(self):
        self.mx, self.my = mouse.get_pos()
        self.mx -= self.config_width
        self.my -= self.config_height

    def mouse_button_down(self):
        self.set_click(False)
        if self.comparison_type(MOUSEBUTTONDOWN) and self.choose_button == 1:
            self.set_choose_button(0)
            now = time.get_ticks()
            if now > self.debounce_ms + self._last_click_time:
                self._last_click_time = now
                self.set_click(True)

    def event_button_check(self, base_mouse, nonbase_mouse, sound_and_func):
        if self.fake_choose_button == 1 and self.wait_button == 1:
            self.fake_choose_button = 0
        elif self.fake_choose_button == 1:
            self.wait_button = 1
            self.fake_choose_button = 0
            nonbase_mouse()
            sound_and_func()
        else:
            self.wait_button = 0
            base_mouse()

    def set_click(self, click: bool):
        self.click = click

    def get_click(self):
        return self.click

    def set_choose_button(self, choose: int):
        self.choose_button = choose

    def set_choose_fake_button(self, fake_choose: int):
        self.fake_choose_button = fake_choose

    def comparison_type(self, event_type):
        return self.event.type == event_type

    def comparison_key(self, event_key):
        return self.event.key == event_key

    def set_key(self, event_key):
        self.event.key = event_key
