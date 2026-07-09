from pygame import font, Surface

class Font:
    def __init__(self, name_font, size_font, bold=False, italic=False):
        self._name_font = name_font
        self._size_font = size_font
        self.bold = bold
        self.italic = italic
        self.font = None
        self.__initial_font__()

    def __initial_font__(self):
        self.font = font.SysFont(
            self._name_font, self._size_font, self.bold, self.italic
        )

    def get_font(self) -> Font:
        return Font(self._name_font, self._size_font, self.bold, self.italic)

    def render_font(self)  -> font.Font:
        return self.font

    def copy_font(self, new_font: Font):
        self.font = new_font.get_font()
        self._name_font = self.font.get_name()
        self._size_font = self.font.get_size()
        self.bold = self.font.get_bold()
        self.italic = self.font.get_italic()
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


class Text:  # Correct
    def __init__(self,
        font_name: font.Font,
        lang: dict,
        surface: Surface,
        config,
        color: tuple = (0, 0, 0)):
        self.font = font_name
        self.lang = lang
        self.surface = surface
        self.config = config
        self.color = color

    def draw_text(self, text, x, y, color: tuple = (0, 0, 0)):
        text_obj = self.font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.surface.blit(text_obj, text_rect)
        return text_rect

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

    def set_surface(self, surface: Surface):
        self.surface = surface

    def copy(self):
        return Text(self.font, self.lang, self.surface, self.config, self.color)


class ModuleText(Text, Font):
    def __init__(self, class_text: Text):
        super().__init__(
            class_text.font,
            class_text.lang,
            class_text.surface,
            class_text.config,
            class_text.color,
        )
        self.class_text = class_text
        self.lang = self.class_text.get_language()
        self.config = class_text.get_config()
        self.chosen = ""
        self.text = ""

    def update_lang(self):
        self.lang = self.class_text.get_language()

    def set_change_text(self, inspection, change_x, change_y):
        if self.config.check(inspection):
            self.chosen = self.lang.get(change_x, f"{change_x}")

        elif not self.config.check(inspection):
            self.chosen = self.lang.get(change_y, f"{change_y}")

    def get_set_text(self, base_key, x_text, y_text, color: tuple = (0, 0, 0)):
        self.text = self.lang.get(base_key, f"{base_key}")
        self.draw_text("{} {}".format(self.text, self.chosen), x_text, y_text, color)

