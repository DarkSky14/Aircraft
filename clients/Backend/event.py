import pygame.event, pygame.time
import sys
from pygame import (
    QUIT, KEYDOWN, K_ESCAPE,
    MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_UP, K_DOWN
)

if __name__ == "__main__":
    import _lib_
else:
    import clients.Backend._lib_ as _lib_


class EventControl:
    def __init__(self, debounce_ms = 200):
        self.debounce_ms = debounce_ms
        self._last_click_time = 0
        click = False
        self.click = click

    def event_pool(self):         
        for event in pygame.event.get():
            self.event = event
            if self.event.type == QUIT:
                pygame.quit()
                sys.exit()

    def K_ESCAPE(self, exit, exit_effect=None):
        if self.event.type == KEYDOWN and self.event.key == K_ESCAPE:
            _lib_.config.check({"effect": "True"}, exit_effect)
            self.event.key = 0
            return exit()

    def MOUSEBUTTONDOWN(self):
            self.click = False
            if self.event.type == MOUSEBUTTONDOWN and self.event.button == 1:
                now = pygame.time.get_ticks()
                if now > self.debounce_ms + self._last_click_time:
                    self.event.button = 0
                    self._last_click_time = now
                    self.click = True             
    
    def add_event_waiter(self, event_type, handler, *args):
        if self.event.type == event_type:
            return handler(args)

    def add_key_event_waiter(self, event_type, event_key, handler):
        if self.event.type == event_type:
            if self.event.key == event_key:
                self.event.key = 0
                return handler()
    
    def create_event(self, nons):
        return pygame.event.event_name(nons)
    