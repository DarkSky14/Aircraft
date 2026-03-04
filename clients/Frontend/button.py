import clients.Backend.language as Language
import pygame.surface
from abc import abstractmethod

if __name__ == "__main__":
    import UI
    import Text
    import animation
    import surface as Surface
else:
    import clients.Frontend.UI as UI
    import clients.Frontend.Text as Text
    import clients.Frontend.animation as animation
    import clients.Frontend.surface as Surface

class Button(animation.AnimationMove):
    def __init__(self, event, button_list: list, surface: pygame.surface.Surface):       
        self.event = event
        self.button_list = button_list
        self.surface = surface
        self.draw_button = UI.MyDrawObject
    
    @abstractmethod
    def button(self):
        pass
    
    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def text_set(self):
        pass

    def __copy_button__(self):
        return self.x, self.y, self.size
        
    def set_button(self, x, y, size):
        self.x, self.y = x, y
        self.size = size
        self.x_true, self.y_true, self.size_true = self.__copy_button__()
        return self.x, self.y, self.size

    def Button(self, x, y, size, function1):      
        mx, my = pygame.mouse.get_pos() 
        
        button = self.draw_button(self.x, self.y, self.size, self.surface)  # type: ignore
                 
        if button.rect.collidepoint(mx - Surface.conf_width, my - Surface.conf_height) == True:
            self.button_list.append(".")
            button.draw_object((205, 200, 200), 15, 10)

            if self.event.click:
                button.draw_object((205, 200, 200), 3, 10)
                function1()

        button.draw_object((205, 200, 200), 3, 10)


class ButtonBased(Button):
    def __init__(self, event, button_list: list, surface: pygame.surface.Surface, config):
        super().__init__(event, button_list, surface)
        self.config = config

    def copy(self):
        return ButtonBased(self.event, self.button_list, self.surface, self.config)
    
    def text_set(self, textm: Text.AllText, base_key, x = None, y = None, color: tuple = (0, 0, 0)):
        textm.text(base_key, self.x + 15, self.y + 2, color)
    
    def button(self, effect_click = None, function_open = None):
        self.config.check({"effect": "True"}, effect_click)
        function_open() # type: ignore


class ButtonChecked(Button):
    def __init__(self, event, button_list: list, surface: pygame.surface.Surface, config):
        super().__init__(event, button_list, surface)
        self.config = config

    def copy(self):
        return ButtonChecked(self.event, self.button_list, self.surface, self.config)
    
    def text_change(self, textm: Text.ModuleText, change, change_x, change_y):
        textm.change_key(change, change_x, change_y)
    
    def text_set(self, textm: Text.ModuleText, change, base_key, change_x, change_y,  color: tuple = (0, 0, 0)):
        textm.text(change, base_key, change_x, change_y, self.x + 15, self.y + 2, color)

    def button(self, text, effect_click = None, function_open = None):
        self.text = text
        self.config.check({"effect": "True"}, effect_click)
        if self.config.check(text[0]) == True:
            self.config.write(text[1])
            function_open() # type: ignore
        elif self.config.check(text[1]) == True:
            self.config.write(text[0])
            function_open()  # type: ignore


class ButtonLang(Button):
    def __init__(self, event, button_list: list, surface: pygame.surface.Surface, config):
        super().__init__(event, button_list, surface)
        self.config = config

    def copy(self):
        return ButtonLang(self.event, self.button_list, self.surface, self.config)
    
    def text_set(self, textm: Text.AllText, base_key, x = None, y = None, color: tuple = (0, 0, 0)):
        textm.text(base_key, self.x + 15, self.y + 2, color)

    def button(self, text: dict, language: dict|None, effect_click = None):
        self.config.check({"effect": "True"}, effect_click)
        if self.config.check(text) == False:
            self.config.write(text)
            Language.language = (language)
        else: pass
    
