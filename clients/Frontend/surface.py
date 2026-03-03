import pygame.display
import screeninfo
from abc import abstractmethod


class _ClassSurface:
    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height
        self.screen = self.width, self.height
    
    @abstractmethod
    def surface(self) -> pygame.Surface:
        pass

    def get_size_surface(self) -> tuple[int, int]:
        return self.screen

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height


class StandartSurface(_ClassSurface):
    def __init__(self, width: int = 0, height: int = 0):
        super().__init__(width, height)
        self.screen = self.width, self.height
    
    def set_surface(self, mode = pygame.WINDOWMAXIMIZED) -> pygame.Surface:
        return pygame.display.set_mode(self.screen, mode)


class AdjustmentSurface(_ClassSurface):
    def __init__(self):
        pass
    
    def surface(self, mode = pygame.WINDOWMAXIMIZED):
        screen = screeninfo.get_monitors()
        for s in screen:
            self.width = s.width
            self.height = s.height
            self.screen = self.width, self.height

        flags = pygame.DOUBLEBUF | pygame.HWSURFACE 
        mode_work = pygame.display.mode_ok((self.width, self.height), flags)
        print("Mode:", mode_work)
        print("Display driver:", pygame.display.get_driver())
        print("Video info:", pygame.display.Info())
        if mode_work == 0:
            return pygame.display.set_mode(self.screen, mode)
        else:
            return pygame.display.set_mode(self.screen, flags)


class SubSurface(_ClassSurface):
    def __init__(self, width: int = 0, height: int = 0):
        super().__init__(width, height)

    def surface(self, surface: pygame.Surface, left, top):
        return surface.subsurface(left, top, self.width, self.height)


class AdjustmentSubSurface(_ClassSurface):
    def __init__(self, width: int = 0, height: int = 0):
        super().__init__(width, height)
    
    def surface(self, surface: pygame.Surface):
        if surface.get_width() - self.width <= 0:
            procent = (surface.get_width() / self.width)
            size_width = surface.get_width()
        procent_height = (self.height * procent)
        conf_height = (surface.get_height() - self.height) / 2
        
        self.width = size_width
        self.__procent_height = procent_height
        self._conf_height = conf_height

        return surface.subsurface(0, 0 + conf_height, size_width, self.height)
    
    def get_procent_height(self) -> float:
        return self.__procent_height
    
    def get_conf_height(self) -> float:
        return self._conf_height


class ScrollingBG:
    def __init__(self, image: pygame.Surface, speed: int):
        self.image = image
        self.width = self.image.get_width()
        self.speed = speed
        self.x = 0

    def update(self):
        self.x = (self.x - self.speed) % self.image.get_width()
        self.width = self.x - self.image.get_width()

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, (self.x, 0))
        surface.blit(self.image, (self.width, 0))
 
main_surface = AdjustmentSurface().surface()
e = AdjustmentSubSurface(1373, 761)
d = e.surface(main_surface)
main_surface.fill((0, 0, 0))
d.fill((255, 255, 255))

screen = e.get_size_surface()
conf_height = e.get_conf_height()
height = e.get_height()
width =  e.get_width()