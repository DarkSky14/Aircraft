import pygame.event, pygame.time
import sys
from pygame import (
    QUIT, KEYDOWN, K_ESCAPE,
    MOUSEBUTTONDOWN
)

if __name__ == "__main__":
    import _lib_
else:
    import clients.Backend._lib_ as _lib_


class EventControl:
    def __init__(self, debounce_ms = 200):
        self.debounce_ms = debounce_ms
        self._last_click_time = 0

    def __event_pool__(self, exit, exit_effect=None): 
        click = False
        self.click = click
        for event in pygame.event.get():
            self.event = event

            if self.event.type == QUIT:
                pygame.quit()
                sys.exit()

            if self.event.type == KEYDOWN:
                if self.event.key == K_ESCAPE:
                    _lib_.config.check({"effect": "True"}, exit_effect)
                    return exit()
        
            if self.event.type == MOUSEBUTTONDOWN:
                if self.event.button == 1:
                    now = pygame.time.get_ticks()
                    print("{} > {} + {}".format(now, self.debounce_ms, self._last_click_time))
                    if now > self.debounce_ms + self._last_click_time:
                        self._last_click_time = now
                        self.click = True
    