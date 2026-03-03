import pygame.draw, pygame.surface, pygame.mouse
from abc import abstractmethod

if __name__ == "__main__":
    import surface as Surface
    import button as butt
    import animation
else:
    import clients.Frontend.surface as Surface
    import clients.Frontend.button as butt
    import clients.Frontend.animation as animation


class DrawingMy():
    def __init__(self, left: float, top: float, size: tuple, surface: pygame.surface.Surface) -> None:
        self.top = top
        self.left = left
        self.size = size
        self.surface = surface
        self.rect = pygame.Rect((self.left, self.top), self.size)

    @abstractmethod
    def draw_object(self):
        pass

    def get_rect(self) -> pygame.Rect:
        return self.rect
     

class MyDrawObject(DrawingMy): #Correct
    def __init__(self, left: float, top: float, size: tuple, surface: pygame.surface.Surface) -> None:
        super().__init__(left, top, size, surface)
 
    def draw_object(self, color: tuple, border: int = 0, border_radius: int = 0, radius: int = 50) -> pygame.Rect:
        return pygame.draw.rect(self.surface, color, self.rect, border, border_radius, radius, radius, radius, radius)


class SurfaceM(animation.AnimationMove):
    def __init__(self, event, surface: pygame.surface.Surface, x_move = 0, y_move = 0):
        self.event = event
        self.surface = surface
        self.x_move = x_move
        self.y_move = y_move

    def __copy_object__(self):
        return self.x, self.y, self.size
        
    def set_object(self, x, y, size):
        self.x, self.y = x, y
        self.size = size
        self.x_true, self.y_true, self.size_true = self.__copy_object__()
        self.sub_surface = MyDrawObject(self.x - 25, self.y - 90, self.size, self.surface)
        return self.x, self.y, self.size
    
    def update_pos(self):
        self.sub_surface = MyDrawObject(self.x - 25, self.y - 90, self.size, self.surface)

    def surface_wait(self, exit): 
        mx, my = pygame.mouse.get_pos()
        self.sub_surface.draw_object((100, 100, 100), 300, 10)

        if self.sub_surface.get_rect().collidepoint((mx, my - Surface.conf_height)) == False:
            if self.event.click:
                exit()    
            else:
                pass
