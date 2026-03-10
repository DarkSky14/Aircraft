import pygame.font

if __name__ == "__main__": #or __name__.find("clients.Frontend.Text") != -1:
    import Surface as Surface
    import FileWorker as FileWorker
    import language as language

else:
    try:
        import Surface as Surface
        import FileWorker as FileWorker
        import language as language
    except ImportError:
        import clients.module.Surface as Surface
        import clients.module.FileWorker as FileWorker
        import clients.module.language as language


class Font:
    def __init__(self) -> None:
        pass

    def create_font(self, name_font, size_font, bold = False, italic = False) -> pygame.font.Font:
        self._name_font = name_font
        self._size_font = size_font
        self.bold = bold
        self.italic = italic
        self.font = pygame.font.SysFont(self._name_font, self._size_font, self.bold, self.italic)
        return self.font
        
    def set_font(self, new_font: pygame.font.Font):
        self.font = new_font
    
    def set_size_font(self, new_size):
        self._size_font = new_size

    def update_font(self):
        self.font = pygame.font.SysFont(self._name_font, self._size_font, self.bold, self.italic)

    def get_font(self):
        return self.font


class Text(Font): #Correct
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

    def draw_text_full_topleft(self, font: pygame.font.Font,  text,  x, y, antialias = True, color: tuple = (0,0,0), special_flags: int = 0):
        textobj = font.render(str(int(text)), antialias, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.surface.blit(textobj, textrect, special_flags=special_flags)
    
    def draw_text(self, text, x, y, color: tuple = (0,0,0)):
        textobj = self.font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.surface.blit(textobj, textrect)   
        return textrect

    def get_language(self):
        return self.lang
    
    def get_color(self):
        return self.color

    def get_config(self):
        return self.config
    
    def set_color(self, new_color: tuple):
        self.color = new_color

    def set_language(self, new_language: dict):
        self.lang = new_language
    
    def set_surface(self, surface: pygame.Surface):
        self.surface = surface
    
    def copy(self):
        return Text(self.font, self.lang, self.surface, self.config, self.color)


class ModuleText(Text):
    def __init__(self, class_text: Text):
        super().__init__(class_text.font, class_text.lang, class_text.surface, class_text.config, class_text.color)
        self.class_text = class_text
        self.lang = self.class_text.get_language()
        self.config = class_text.get_config()
        self.chosen = ""
    
    def update_lang(self):
        self.lang = self.class_text.get_language()
    
    def set_change_text(self, change, change_x, change_y):
        if self.config.check(change) == True:
            self.chosen = self.lang.get(change_x, f"{change_x}")

        elif self.config.check(change) == False:
            self.chosen = self.lang.get(change_y, f"{change_y}")

    def get_set_text(self, base_key, x_text, y_text, color: tuple = (0, 0, 0)):
        self.text = self.lang.get(base_key, f"{base_key}")
        self.draw_text("{} {}".format(self.text, self.chosen), x_text, y_text, color)

VERS_GAME = pygame.font.SysFont(None, round(20 * Surface.procent))

text = Text(VERS_GAME, language.language, Surface.d, FileWorker.config, (0,0,0))
big_text = text.copy()
big_text.create_font('Georgia', round(36 * Surface.procent))

standart_text = text.copy()
standart_text.create_font('Georgia', round(21 * Surface.procent))
