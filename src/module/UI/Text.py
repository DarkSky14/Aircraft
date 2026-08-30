import pygame as py
from module.UI import DrawText


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

    def set_font(self, new_font: "Font"):
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


class TriggerText:
    def __init__(self, lang, config = None):
        self.config = config
        self.lang = lang

    def set_change_text(self, inspection, change_x, change_y):
        matched = self.config.check(inspection)
        return self.lang.get_language().get(change_x if matched else change_y, change_x if matched else change_y)


class StandardText:
    def __init__(self, lang):
        self.lang = lang

    def set_base_text(self, base_key):
        return self.lang.get_language().get(base_key, base_key)


class Text(StandardText, TriggerText):
    def __init__(self,
        font_name: "Font",
        lang,
        surface: py.surface.Surface,
        config,
        color: tuple = (0, 0, 0)):
        self.font = font_name
        self.lang = lang
        self.surface = surface
        self.config = config
        self.color = color

    def draw_text(self, text, x, y, color: tuple = (0, 0, 0), rect:str = "topleft"):
        DrawText.draw_text(self, text, x, y, color, rect)

    def set_language(self, new_language: dict):
        self.lang = new_language

    def set_settings_text(self, obj: "Text"):
        self.font = obj.font
        self.lang = obj.lang
        self.surface = obj.surface
        self.config = obj.config
        self.color = obj.color

    def copy_text(self):
        return Text(self.font, self.lang, self.surface, self.config, self.color)

    def set_font(self, font):
        self.font = font