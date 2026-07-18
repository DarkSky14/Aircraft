import pygame as py


class Font:
    def __init__(self, name_font, size_font, bold=False, italic=False):
        self._name_font = name_font
        self._size_font = size_font
        self.bold = bold
        self.italic = italic
        self.font = None
        self.__initial_font__()

    def __initial_font__(self):
        self.font = py.font.SysFont(
            self._name_font, self._size_font, self.bold, self.italic
        )

    def copy_font(self) -> "Font":
        return Font(self._name_font, self._size_font, self.bold, self.italic)

    def render_font(self)  -> py.font.Font:
        return self.font

    def set_font(self, new_font: Font):
        self._name_font = new_font.get_name()
        self._size_font = new_font.get_size()
        self.bold = new_font.get_bold()
        self.italic = new_font.get_italic()
        self.__initial_font__()

    def set_size(self, size):
        self._size_font = size
        self.__initial_font__()

    def get_size(self):
        return self._size_font

    def get_name(self):
        return self._name_font

    def get_bold(self):
        return self.bold

    def get_italic(self):
        return self.italic


class DrawText:
    def __init__(self):
        self.font = py.font.Font()
        self.surface = py.surface.Surface

    def draw_text(self, text: str, x, y, color: tuple = (0, 0, 0)):
        cache_key = (text, color, id(self.font))
        if getattr(self, "_cache_key", None) != cache_key:
            self._cache_key = cache_key
            self.text_obj = self.font.render(text, True, color)
            self.text_rect = self.text_obj.get_rect()

        self.text_rect.topleft = (x, y)
        self.surface.blit(self.text_obj, self.text_rect)
        return self.text_rect


class TriggerText:
    def __init__(self):
        self.config = None
        self.lang = {}

    def set_change_text(self, inspection, change_x, change_y):
        matched = self.config.check(inspection)
        return self.lang.get(change_x if matched else change_y, change_x if matched else change_y)

class StandardText:
    def __init__(self):
        self.lang = {}

    def set_base_text(self, base_key):
        return self.lang.get(base_key, base_key)


class DrawingText(DrawText):
    def __init__(self):
        DrawText.__init__(self)

    def get_set_text(self, text, x_text, y_text, color: tuple = (0, 0, 0)):
        self.draw_text(text, x_text, y_text, color)


class Text(DrawingText, Font, StandardText, TriggerText):  # Correct
    def __init__(self,
        font_name: py.font.Font,
        lang: dict,
        surface: py.surface.Surface,
        config,
        color: tuple = (0, 0, 0)):
        self.font = font_name
        self.lang = lang
        self.surface = surface
        self.config = config
        self.color = color

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

    def set_surface(self, surface: py.surface.Surface):
        self.surface = surface

    def set_settings_text(self, obj: Text):
        self.font = obj.copy_font()
        self.lang = obj.get_language()
        self.surface = obj.surface
        self.config = obj.config
        self.color = obj.get_color()

    def copy_text(self):
        return Text(self.font, self.lang, self.surface, self.config, self.color)

    def __iter__(self):
        return iter((self.font, self.lang, self.surface, self.config, self.color))