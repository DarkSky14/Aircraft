import pygame.font

if __name__ == "__main__":
    import surface as Surface
    import clients.Backend._lib_ as _lib_
    import clients.Backend.language as language
    from menu_client import VERS_GAME, BLACK, BIG_TEXT, STANDART_TEXT

else:
    import clients.Frontend.surface as Surface
    import clients.Backend.language as language
    import clients.Backend._lib_ as _lib_
    from clients.menu_client import VERS_GAME, BLACK, BIG_TEXT, STANDART_TEXT

class Text: #Correct
    def __init__(
            self, 
            font: pygame.font.Font, 
            lang: dict,
            surface: pygame.Surface,
            config,
            color: tuple = (0,0,0)
        ):
        self.font = font
        self.lang = lang 
        self.surface = surface
        self.config = config
        self.color = color
    
    def e(self, text_obj):
        self.font, self.lang, self.surface, self.config, self.color = text_obj.copy()
        return self


    def draw_text(self, text, x, y, color: tuple):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.surface.blit(textobj, textrect)   
        return textrect

    def get_language(self):
        return self.lang
    
    def get_config(self):
        return self.config

    def set_font(self, new_font: pygame.font.Font):
        self.font = new_font
    
    def set_color(self, new_color: tuple):
        self.color = new_color

    def set_language(self, new_language: dict):
        self.lang = new_language
    
    def set_surface(self, surface: pygame.Surface):
        self.surface = surface
    
    def copy(self):
        return Text(self.font, self.lang, self.surface, self.config, self.color)


class AllText(Text):
    def __init__(self, class_text: Text):
        self.class_text = class_text
        self.lang = self.class_text.get_language()

    def update_lang(self):
        self.lang = self.class_text.get_language()

    def text(self, base_key, x, y, color: tuple = (0, 0, 0)):
        text = self.lang.get(base_key, f"{base_key}")
        return Text.copy(self.class_text).draw_text(text, x, y, color)


class ModuleText(Text):
    def __init__(self, class_text: Text):
        self.class_text = class_text
        self.lang = self.class_text.get_language()
        self.config = class_text.get_config()
        self.chosen = "None"
    
    def update_lang(self):
        self.lang = self.class_text.get_language()
    
    def change_key(self, change, change_x, change_y):
        if self.config.check(change) == True:
            self.chosen = self.lang.get(change_x, f"{change_x}")

        elif self.config.check(change) == False:
            self.chosen = self.lang.get(change_y, f"{change_y}")

    def text(self, change, base_key, change_x, change_y, x_text, y_text, color: tuple = (0, 0, 0)):
        if self.config.check(change) == True:
            self.chosen = self.lang.get(change_x, f"{change_x}")

        elif self.config.check(change) == False:
            self.chosen = self.lang.get(change_y, f"{change_y}")
        text = self.lang.get(base_key, f"{base_key}")
        return Text.copy(self.class_text).draw_text("{} {}".format(text, self.chosen), x_text, y_text, color)


text = Text(VERS_GAME, language.language, Surface.d, _lib_.config, BLACK)
big_text = text.copy()
big_text.set_font(BIG_TEXT)
standart_text = big_text.copy()
standart_text.set_font(STANDART_TEXT)