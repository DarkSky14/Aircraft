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


class SurfaceM(animation.AnimationMove, animation.Resizable):
    def __init__(self, event, surface: pygame.surface.Surface, x_move = 0, y_move = 0, size_config = 0):
        self.event = event
        self.surface = surface
        self.x_move = x_move
        self.y_move = y_move
        self.size_config = size_config
        animation.AnimationMove.__init__(self, size_config)
        animation.Resizable.__init__(self, size_config)

    def __copy_object__(self):
        return self.x, self.y, self.size
        
    def set_object_size(self, x, y, size):
        self.x, self.y = x * self.size_config, y * self.size_config
        self.size_x, self.size_y = size   
        self.size_x *= self.size_config
        self.size_y *= self.size_config
        self.size = self.size_x, self.size_y
        #self.x_true, self.y_true, self.size_true = self.__copy_object__()
        #self.size_x_true, self.size_y_true = self.size_true
        self.b_radius = self.size_y / 2
        self.sub_surface = MyDrawObject(self.x, self.y, self.size, self.surface)#25 90
        return self.x, self.y, self.size
    
    def get_position(self):
        return self.x, self.y
    
    def get_x_pos(self):
        return self.x
    
    def get_y_pos(self):
        return self.y
    
    def get_size(self):
        return self.size_x, self.size_y 
    
    def get_size_x(self):
        return self.size_x
    
    def get_size_y(self):
        return self.size_y
    
    def update_pos(self):
        self.sub_surface = MyDrawObject(self.x, self.y, self.size, self.surface)
        self.b_radius = self.size_y / 2

    def surface_wait(self, exit): 
        mx, my = pygame.mouse.get_pos()
        surface = self.sub_surface.draw_object((100, 100, 100), round(self.b_radius), 30)

        if surface.collidepoint((mx - Surface.conf_width, my - Surface.conf_height)) == False:
            if self.event.click:
                exit()    
            else:
                pass
