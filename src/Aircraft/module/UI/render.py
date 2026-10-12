import pygame as py


class Rectangle:
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

        return py.draw.rect(
            self.surface, color, self.rect, border, border_radius,
            radius, radius, radius, radius,
        )

    def get_rect(self) -> py.Rect:
        return self.rect


class Line:
    def __init__(
        self, window: py.surface.Surface
    ) -> None:
        self.surface = window

    def draw_object(self, color, pos1:tuple, pos2:tuple, width):
        return py.draw.aaline(self.surface, color, pos1, pos2, width)


class DrawText:
    def __init__(self, surface: py.surface.Surface):
        self.surface = surface

    def draw_text(self, text, x, y, font, color: tuple = (0, 0, 0), rect:str = "topleft"):
        cache_key = (text, color, x, y, id(font))
        if getattr(self, "_cache_key", None) != cache_key:
            self._cache_key = cache_key
            self.text_obj = font.render_font().render(str(text), True, color)
            self.text_rect = self.text_obj.get_rect()
            if rect == "topleft":
                self.text_rect.topleft = (x, y)
            elif rect == "bottomright":
                self.text_rect.bottomright = (x, y)
            elif rect == "bottomleft":
                self.text_rect.bottomleft = (x, y)
            elif rect == "centerx":
                self.text_rect.centerx, self.text_rect.y = (x, y)

        self.surface.blit(self.text_obj, self.text_rect)
        return self.text_rect


class DrawTextExp:
    def __init__(self, surface: py.surface.Surface):
        self.surface = surface
        self.text = None

    def draw_text(self, button, text, x, y, font, color: tuple = (0, 0, 0), rect:str = "topleft"):
        cache_key = (text, color, x, y, id(font))
        if button._cache_key != cache_key:
            button._cache_key = cache_key
            button.text_obj = self.text.font.render_font().render(str(text), True, color)
            button.text_rect = button.text_obj.get_rect()
            if rect == "topleft":
                button.text_rect.topleft = (x, y)
            elif rect == "bottomright":
                button.text_rect.bottomright = (x, y)
            elif rect == "bottomleft":
                button.text_rect.bottomleft = (x, y)
            elif rect == "centerx":
                button.text_rect.centerx, button.text_rect.y = (x, y)

        self.surface.blit(button.text_obj, button.text_rect)
        return button.text_rect