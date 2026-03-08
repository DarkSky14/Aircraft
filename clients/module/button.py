#import clients.Backend.language as Language
import pygame.surface
from abc import abstractmethod

if __name__ == "__main__":
    import UI
    import Text
    import UI_module.animation as animation
    import Surface as Surface
else:   
    try:
        import UI
        import Text
        import UI_module.animation as animation
        import Surface as Surface
    except ImportError:
        import clients.module.UI as UI
        import clients.module.Text as Text
        import clients.module.UI_module.animation as animation
        import clients.module.Surface as Surface

class Button(animation.AnimationMove):
    def __init__(self, event, surface: pygame.surface.Surface, size_config:int|float = 0):       
        self.event = event
        self.surface = surface
        self.size_config = size_config
        self.draw_button = UI.MyDrawObject
        animation.AnimationMove.__init__(self, self.size_config)
    
    @abstractmethod
    def button(self):
        pass
    
    @abstractmethod
    def copy(self):
        return Button(self.event, self.surface, self.size_config)

    @abstractmethod
    def get_text(self):
        pass

    def __copy_button__(self):
        return self.x, self.y, self.size
        
    def set_button(self, x, y, size: tuple = (int, int)):
        self.x, self.y = round(x), round(y)
        self.size = size
        self.size_x, self.size_y = size    
        self.size_x *= self.size_config
        self.size_y *= self.size_config
        self.b_radius = round(self.size_y / 2)

        if self.size_y <= (self.b_radius * 2):
            self.size_y = (self.b_radius * 2)

        self.size = self.size_x, self.size_y
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


class ModuleButton(Button, Text.ModuleText):
    def __init__(self, event, surface: pygame.surface.Surface, config, class_text: Text.Text, size_config:int|float = 0):
        Button.__init__(self, event, surface, size_config)
        Text.ModuleText.__init__(self, class_text)
        self.config = config

    def copy(self):
        return ModuleButton(self.event, self.surface, self.config, self.class_text, self.size_config)

    def check_config(self, text, effect_click = None):
        return self.config.check(text, effect_click)
    
    def write_in_config(self, text):
        self.config.write(text)
    
    def button_click(self):
        return self.event.click
    
    def text_change(self, change, change_x, change_y):
        self.set_change_text(change, change_x, change_y)

    def get_text_self(self, base_key, color: tuple = (0, 0, 0)):
        self.get_set_text(base_key, self.x + 15, self.y + 2, color)
    
    def get_text(self, text_class: Text.ModuleText, base_key, color: tuple = (0, 0, 0)):
        text_class.get_set_text(base_key, self.x + 15, self.y + 2, color)

    def Button(self, function1):           
        button = self.draw_button(self.x, self.y, self.size, self.surface)  # type: ignore
        
        if button.rect.collidepoint(self.event.mx - Surface.conf_width, self.event.my - Surface.conf_height) == True:
            button.draw_object((205, 200, 200), self.b_radius, 10)
            self.event.set_choose_button(1)
            self.event.set_choose_fake_button(1)

            if self.event.get_click() == True:
                button.draw_object((205, 200, 200), 3, 10)
                self.event.set_choose_button(0)
                self.event.set_click(False)
                function1()

        button.draw_object((205, 200, 200), 3, 10)
