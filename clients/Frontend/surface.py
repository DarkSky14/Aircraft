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
        # Якщо висота > 761, то потрібно взяти відсоток на який це збільшилось
        # Якщо ширина > 1373, то потрібно взяти відсоток на який це збільшилось
        # Якщо і ширина і висота більші за оригінал, то потрібно взяти менший відсоток
        # Якщо висота < 761, то потрібно взяти відсоток на який це зменшилось
        # Якщо ширина < 1373, то потрібно взяти відсоток на який це зменшиилось
        # Якщо і ширина і висота меньші за оригінал, то потрібно взяти більший відсоток
        
        procent_width = (surface.get_width() / self.width) 
        procent_height = (surface.get_height() / self.height) 

        if procent_width > procent_height:
            size_width = self.width * procent_height 
            size_height = surface.get_height()        
            self._conf_width = (surface.get_width() - size_width) / 2
            self._conf_height = 0
        elif procent_width < procent_height:
            size_width = surface.get_width()
            size_height = self.height * procent_width
            self._conf_width = 0
            self._conf_height = (surface.get_height() - size_height) / 2

        elif procent_width == procent_height:
            size_width = surface.get_width()
            size_height = surface.get_height()
            self._conf_width = 0
            self._conf_height = 0
        
        print("Size width:", size_width)
        print("Size height:", size_height)
        print("Conf width:", self._conf_width)
        print("Conf height:", self._conf_height)

        self.screen = size_width, size_height
        self.width = size_width     
        self.height = size_height

        return surface.subsurface(0 + self._conf_width, 0 + self._conf_height, self.width, self.height)
    
    def get_conf_height(self) -> float:
        return self._conf_height
    
    def get_conf_width(self) -> float:
        return self._conf_width


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
 
pygame.init()

main_surface = AdjustmentSurface().surface()
e = AdjustmentSubSurface(300, 168) # Original size 1373x761
d = e.surface(main_surface)
main_surface.fill((0, 0, 0))
d.fill((255, 255, 255))

screen = e.get_size_surface()
conf_width = e.get_conf_width()
conf_height = e.get_conf_height()
height = e.get_height()
width =  e.get_width()