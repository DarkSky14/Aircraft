import pygame.draw, pygame.surface

if __name__ == "__main__":
    import Surface as Surface
    import button as butt
    import UI_module.animation as animation
else:
    try:
        import Surface as Surface
        import button as butt
        import UI_module.animation as animation
    except ImportError:
        import clients.module.Surface as Surface
        import clients.module.button as butt
        import clients.module.UI_module.animation as animation
     

class MyDrawObject: #Correct
    def __init__(self, left: float, top: float, size: tuple, surface: pygame.surface.Surface) -> None:
        self.top = top
        self.left = left
        self.size = size
        self.surface = surface
        self.rect = pygame.Rect((self.left, self.top), self.size)
 
    def draw_object(self, color: tuple, border: int = 0, border_radius: int = 0, radius: int = 50) -> pygame.Rect:
        return pygame.draw.rect(self.surface, color, self.rect, border, border_radius, radius, radius, radius, radius)

    def get_rect(self) -> pygame.Rect:
        return self.rect

class SurfaceM(animation.AnimationMove, animation.Resizable):
    def __init__(self, event, surface: pygame.surface.Surface, x_move = 0, y_move = 0, size_config: float = 0):
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
        surface = self.sub_surface.draw_object((100, 100, 100), round(self.b_radius), round(30*self.size_config), round(40*self.size_config))

        #if surface.collidepoint((self.event.mx - Surface.conf_width, self.event.my - Surface.conf_height)) == False:
         #   self.event.set_choose_button(1)
          #  if self.event.comparison_type(pygame.MOUSEBUTTONDOWN) == True and self.event.get_click() == True:
           #     self.event.set_choose_button(0)
            #    self.event.set_click(False)
             #   exit()   
    
    def set_click(self, click):
        self.event.set_click(click)
