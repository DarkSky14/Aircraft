from pygame import Surface, DOUBLEBUF, WINDOWMAXIMIZED, HWSURFACE, display, surface

try:
    from logged import log
except ImportError:
    from module.logged import log


class _ClassSurface:
    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height
        self.screen = self.width, self.height

    def surface(self) -> Surface:
        pass

    def get_size_surface(self) -> tuple[int, int]:
        return self.screen

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height


class StandardSurface(_ClassSurface):
    def __init__(self, width: int = 0, height: int = 0):
        _ClassSurface.__init__(self, width, height)

    def surface(self, mode=WINDOWMAXIMIZED) -> Surface:
        flags = DOUBLEBUF | HWSURFACE
        mode_work = display.mode_ok((self.width, self.height), flags)

        log.debug({"Mode": mode_work})
        log.debug({"Display driver": display.get_driver()})
        log.debug({"Video info": display.Info()})

        if mode_work == 0:
            return display.set_mode(self.screen, mode)
        else:
            return display.set_mode(self.screen, flags)


class AdjustmentSurface(_ClassSurface):
    def __init__(self):
        _ClassSurface.__init__(self)

    def surface(self, mode=WINDOWMAXIMIZED) -> Surface:
        info = display.Info()
        self.width, self.height = info.current_w, info.current_h
        self.screen = self.width, self.height

        flags = DOUBLEBUF | HWSURFACE
        mode_work = display.mode_ok((self.width, self.height), flags)

        log.debug({"Mode": mode_work})
        log.debug({"Display driver": display.get_driver()})
        log.debug({"Video info": display.Info()})

        if mode_work == 0:
            return display.set_mode(self.screen, mode)
        else:
            return display.set_mode(self.screen, flags)


class SubSurface(_ClassSurface):
    def __init__(self, width: int = 0, height: int = 0):
        _ClassSurface.__init__(self, width, height)

    def surface(self, sub_surface: Surface, left, top) -> Surface:
        return sub_surface.subsurface(left, top, self.width, self.height)


class AdjustmentSubSurface(_ClassSurface):
    def __init__(self, width: int = 0, height: int = 0):
        _ClassSurface.__init__(self, width, height)

    def surface(self, surface: surface.Surface):
        proponent_width = surface.get_width() / self.width
        proponent_height = surface.get_height() / self.height

        if proponent_width > proponent_height:
            self.procent = proponent_height
            size_width = self.width * proponent_height
            size_height = surface.get_height()
            self._conf_width = (surface.get_width() - size_width) / 2
            self._conf_height = 0

        elif proponent_width < proponent_height:
            self.procent = proponent_width
            size_width = surface.get_width()
            size_height = self.height * proponent_width
            self._conf_width = 0
            self._conf_height = (surface.get_height() - size_height) / 2

        elif proponent_width == proponent_height:
            self.procent = proponent_width
            size_width = surface.get_width()
            size_height = surface.get_height()
            self._conf_width = 0
            self._conf_height = 0

        self.width = size_width
        self.height = size_height
        self.screen = self.width, self.height

        log.debug({"Proponent:": self.procent})
        log.debug({"Size width": size_width})
        log.debug({"Size height:": size_height})
        log.debug({"Conf width:": self._conf_width})
        log.debug({"Conf height:": self._conf_height})

        return surface.subsurface(
            self._conf_width, self._conf_height, self.width, self.height
        )

    def get_conf_height(self) -> float:
        return self._conf_height

    def get_conf_width(self) -> float:
        return self._conf_width

    def get_procent(self) -> int | float:
        return self.procent


class ScrollingBG:
    def __init__(self, image: Surface, speed: int):
        self.image = image
        self.width = self.image.get_width()
        self.speed = speed
        self.x = 0
        log.debug({"Image size": self.image.get_size()})

    def update(self):
        self.x = (self.x - self.speed) % self.image.get_width()
        self.width = self.x - self.image.get_width()

    def draw(self, surface: Surface):
        surface.blit(self.image, (self.x, 0))
        surface.blit(self.image, (self.width, 0))
