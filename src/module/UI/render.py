import pygame as py


class MyDrawObject:
    def __init__(
        self, left: float, top: float, size: tuple, window: py.surface.Surface
    ) -> None:
        self.top = top
        self.left = left
        self.size = size
        self.surface = window
        self.rect = py.Rect((self.left, self.top), self.size)

    def draw_object(
        self, color: tuple, border: int = 0, border_radius: int = 0, radius: int = 50
    ) -> py.Rect:
        #max_safe = min(self.rect.width, self.rect.height) // 2
        #border = min(border, max_safe)
        #border_radius = min(border_radius, max_safe)
        #radius = min(radius, max_safe)

        return py.draw.rect(
            self.surface, color, self.rect, border, border_radius,
            radius, radius, radius, radius,
        )

    def get_rect(self) -> py.Rect:
        return self.rect


class DrawText:
    def __init__(self, font, surface: py.surface.Surface):
        self.font = font
        self.surface = surface

    def set_font(self, font: "Font"):
        self.font = font

    def draw_text(self, text, x, y, color: tuple = (0, 0, 0), rect:str = "topleft"):
        cache_key = (text, color, x, y, id(self.font))
        if getattr(self, "_cache_key", None) != cache_key:
            self.text = text
            self._cache_key = cache_key
            self.text_obj = self.font.render_font().render(str(self.text), True, color)
            self.text_rect = self.text_obj.get_rect()
            if rect == "topleft":
                self.text_rect.topleft = (x, y)
            elif rect == "bottomright":
                self.text_rect.bottomright = (x, y)
            elif rect == "bottomleft":
                self.text_rect.bottomleft = (x, y)

        self.surface.blit(self.text_obj, self.text_rect)
        return self.text_rect