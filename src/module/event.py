import pygame as py


class Mouse:
    def __init__(
        self,
        event,
        debounce_ms=200,
        config_width: float = 0,
        config_height: float = 0
        ):
        self._last_click_time = 0
        self.click = False
        self.choose_button = False
        self.mouse_choose = False
        self.wait_button = False
        self.debounce_ms = debounce_ms
        self.config_width = config_width
        self.config_height = config_height
        self.mx, self.my = 0, 0
        self.event = event
        self.mouse_sound = False
        self.sound_fixed = False

    def mouse_get(self):
        self.mx, self.my = py.mouse.get_pos()
        self.mx -= self.config_width
        self.my -= self.config_height

    def mouse_button_down(self):
        self.set_click(False)
        if self.event.comparison_type(py.MOUSEBUTTONDOWN) and self.choose_button:
            self.set_choose_button(False)
            now = py.time.get_ticks()
            if now > self.debounce_ms + self._last_click_time:
                self._last_click_time = now
                self.set_click(True)

    def event_button_check(self, base_mouse, nonbase_mouse, sound_and_func):
        if self.mouse_choose and self.wait_button:
            self.mouse_choose = False
            self.mouse_sound = False

        elif self.mouse_choose or self.sound_fixed:
            self.wait_button = True
            self.sound_fixed = False
            self.mouse_choose = True
            nonbase_mouse()
            if not self.mouse_sound:
                sound_and_func()
            self.mouse_sound = True

        elif not self.mouse_choose and self.wait_button:
            self.wait_button = False
            base_mouse()

    def set_sound_fixed(self, sound_fixed: bool):
        self.sound_fixed = sound_fixed

    def set_click(self, click: bool):
        self.click = click

    def get_click(self):
        return self.click

    def set_choose_button(self, choose: bool):
        self.choose_button = choose

    def set_choose_mouse(self, mouse_choose: bool):
        self.mouse_choose = mouse_choose

    def set_mouse_sound_status(self, mouse_sound: bool):
        self.mouse_sound = mouse_sound


class EventControl(Mouse):
    def __init__(
        self,
        debounce_ms=200,
        config_width: float = 0,
        config_height: float = 0
    ):
        self.events = []
        super().__init__(self, debounce_ms, config_width, config_height)

    def event_pool(self):
        self.events = py.event.get()

    def comparison_type(self, event_type) -> bool:
        return any(e.type == event_type for e in self.events)

    def comparison_key(self, event_key) -> bool:
        return any(getattr(e, "key", None) == event_key for e in self.events)

    @staticmethod
    def custom_type():
        return py.event.custom_type()
