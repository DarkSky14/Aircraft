import pygame
from pygame import rect
from abc import ABC

from pygame import Surface, DOUBLEBUF, WINDOWMAXIMIZED, HWSURFACE, display, surface

from module.logged import log


class _ClassSurface(ABC):
    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height

    @property
    def screen(self) -> tuple[int, int]:
        return self.width, self.height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height


class StandardSurface(_ClassSurface):
    def __init__(self, width: int = 0, height: int = 0):
        _ClassSurface.__init__(self, width, height)

    def surface(self, mode=WINDOWMAXIMIZED) -> Surface:
        flags = DOUBLEBUF | HWSURFACE
        supported = display.mode_ok(self.screen, flags)

        log.debug("Mode ok: %s", supported)
        log.debug("Display driver: %s", display.get_driver())
        log.debug("Video info: %s", str(display.Info()))

        if supported:
            return display.set_mode(self.screen, flags | mode)
        log.warning("Requested display mode not supported, falling back to defaults")
        return display.set_mode(self.screen, mode)


class AdjustmentSurface(_ClassSurface):
    def __init__(self):
        _ClassSurface.__init__(self)

    def surface(self, mode=WINDOWMAXIMIZED) -> Surface:
        info = display.Info()
        self.width, self.height = info.current_w, info.current_h

        flags = DOUBLEBUF | HWSURFACE
        supported = display.mode_ok(self.screen, flags)

        log.debug("Mode ok: %s", supported)
        log.debug("Display driver: %s", display.get_driver())
        log.debug("Video info: %s", str(display.Info()))

        if supported:
            return display.set_mode(self.screen, flags | mode)
        log.warning("Requested display mode not supported, falling back to defaults")
        return display.set_mode(self.screen, mode)


class SubSurface(_ClassSurface):
    def __init__(self, width: int = 0, height: int = 0):
        _ClassSurface.__init__(self, width, height)

    def surface(self, sub_surface: Surface, left: int, top: int) -> Surface:
        return sub_surface.subsurface(pygame.rect.Rect(left, top, self.width, self.height))


class AdjustmentSubSurface(_ClassSurface):
    def __init__(self, width: int = 1, height: int = 1):
        _ClassSurface.__init__(self, width, height)
        if width <= 0 or height <= 0:
            text_error = f"width/height мають бути додатні, отримано ({width}, {height})"
            log.critical(text_error)
            raise ValueError(text_error)
            ...
        self.proponent = 1
        self._conf_width = 0
        self._conf_height = 0

    def surface(self, window: surface.Surface):
        proponent_width = window.get_width() / self.width
        proponent_height = window.get_height() / self.height

        if proponent_width > proponent_height:
            self.proponent = proponent_height
            self.width = self.width * proponent_height
            self.height = window.get_height()
            self._conf_width = (window.get_width() - self.width) * 0.5

        elif proponent_width < proponent_height:
            self.proponent = proponent_width
            self.width = window.get_width()
            self.height = self.height * proponent_width
            self._conf_height = (window.get_height() - self.height) * 0.5

        else:
            self.proponent = proponent_width
            self.width = window.get_width()
            self.height = window.get_height()

        log.debug("Proponent: %s", self.proponent)
        log.debug("Size width: %s", self.width)
        log.debug("Size height: %s", self.height)
        log.debug("Conf width: %s", self._conf_width)
        log.debug("Conf height: %s", self._conf_height)

        return window.subsurface(
            pygame.rect.Rect(self._conf_width, self._conf_height, self.width, self.height)
        )

    def get_conf_height(self) -> float:
        return self._conf_height

    def get_conf_width(self) -> float:
        return self._conf_width

    def get_proponent(self) -> float:
        return self.proponent


class ScrollingBG:
    def __init__(self, image: Surface, speed: int):
        self.image = image
        self.width = self.image.get_width()
        self.speed = speed
        self.moved_width = 1
        self.x = 0
        log.debug("Image size: %s", self.image.get_size())

    def update(self):
        self.x = (self.x - self.speed) % self.image.get_width()
        self.moved_width = self.x - self.image.get_width()

    def draw(self, window: Surface):
        window.blit(self.image, (self.x, 0))
        window.blit(self.image, (self.moved_width, 0))
