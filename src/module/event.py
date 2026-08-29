import pygame as py


class Mouse:
    def __init__(
        self, event, debounce_ms=200,
        config_width: float = 0, config_height: float = 0
        ):
        self._last_click_time = 0
        self.mouse_choose = False
        self.wait_button = False
        self.debounce_ms = debounce_ms
        self.config_width = config_width
        self.config_height = config_height
        self.mx, self.my = 0, 0
        self.event = event

    def mouse_get(self):
        self.mx, self.my = py.mouse.get_pos()
        self.mx -= self.config_width
        self.my -= self.config_height

    def mouse_button_down(self):
        if self.event.comparison_type(py.MOUSEBUTTONDOWN):
            now = py.time.get_ticks()
            if now > self.debounce_ms + self._last_click_time:
                self._last_click_time = now
                return True
        return False

    def event_button_check(self, base_mouse, nonbase_mouse, sound_and_func):
        if self.mouse_choose and self.wait_button:
            self.mouse_choose = False

        elif self.mouse_choose:
            self.wait_button = True
            nonbase_mouse()
            sound_and_func()

        elif not self.mouse_choose and self.wait_button:
            self.wait_button = False
            self.mouse_choose = False
            base_mouse()

    def set_choose_mouse(self, mouse_choose: bool):
        self.mouse_choose = mouse_choose


class EventControl:
    def __init__(
        self,
        debounce_ms=200,
        config_width: float = 0,
        config_height: float = 0
    ):
        self.events = []
        self.mouse = Mouse(self, debounce_ms, config_width, config_height)

    def event_pool(self):
        self.events = py.event.get()
        return self.events

    def comparison_type(self, event_type) -> bool:
        return any(e.type == event_type for e in self.events)

    def comparison_key(self, event_key) -> bool:
        return any(getattr(e, "key", None) == event_key for e in self.events)

    @staticmethod
    def custom_type():
        return py.event.custom_type()
