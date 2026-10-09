import sys

import pygame as py

from module.UI import AnimationMove, Rectangle, Text

class ButtonInfo:
    x, y = 0, 0
    size_x, size_y = 0, 0
    size = size_x, size_y
    b_radius = 0
    id = None


class ButtonBase:
    def __init__(self, button: "ButtonInfo" = None):
        if button is None:
            self.button = ButtonInfo()
        else:
            self.button = button

        self.id = self.button.__hash__()

    @property
    def x(self):
        return self.button.x

    @x.setter
    def x(self, x):
        self.button.x = x

    @property
    def y(self):
        return self.button.y

    @y.setter
    def y(self, y):
        self.button.y = y

    @property
    def size(self):
        return self.button.size

    @size.setter
    def size(self, size: tuple):
        self.button.size = size

    @property
    def size_x(self):
        return self.button.size_x

    @size_x.setter
    def size_x(self, x):
        self.button.size_x = x

    @property
    def size_y(self):
        return self.button.size_y

    @size_y.setter
    def size_y(self, y):
        self.button.size_y = y

    @property
    def button_radius(self):
        return self.button.b_radius

    @button_radius.setter
    def button_radius(self, radius):
        self.button.b_radius = radius

    @property
    def id(self):
        return self.button.id

    @id.setter
    def id(self, new_id):
        self.button.id = new_id

    def return_self(self):
        return self


class ButtonModify(ButtonBase, AnimationMove):
    def __init__(
            self, event, window: py.surface.Surface, class_text: "Text", size_config: tuple[int, int] | float = 0
    ):
        self.event = event
        self.surface = window
        self.size_config = size_config
        self.text = class_text
        ButtonBase.__init__(self)
        AnimationMove.__init__(self, size_config, self)

    def copy(self):
        return ButtonModify(
            self.event, self.surface, self.text.copy_text(), self.size_config
        )

    def set_object(self, x, y, size: tuple = (float, float)):
        self.button.x, self.button.y = round(x), round(y)
        self.button.size = size
        self.button.size_x, self.button.size_y = size
        self.button.size_x *= self.size_config[0]
        self.button.size_y *= self.size_config[1]
        self.button.button_radius = round(self.size_y * 0.5)

        if self.button.size_y <= (self.button.button_radius * 2):
            self.button.size_y = self.button.button_radius * 2
        self.button.size = self.button.size_x, self.button.size_y
        self.__rect__update__()
        return self

    def callback(self, function, bool_custom: bool = True):
        if self.button_rect.get_rect().collidepoint((self.event.mouse.mx, self.event.mouse.my)) == bool_custom:
            self.button_rect.draw_object((205, 200, 200), 0, round(self.button.button_radius))
            self.event.mouse.set_choose_mouse(True)

            if self.event.mouse.mouse_button_down():
                self.button_rect.draw_object((205, 200, 200), 3, 10)
                function()

        self.button_rect.draw_object((205, 200, 200), 3, 10)

    def get_text(self, text, color: tuple = (0, 0, 0)):
        self.text.draw_text(text, self.button.x + 15, self.button.y + 2, color)

    def set_surface(self, surface):
        self.surface = surface
        self.text.surface = surface
        self.__rect__update__()

    def __rect__update__(self):
        self.button_rect = Rectangle(
            self.button.x, self.button.y, self.button.size, self.surface
        )

    def add_coord(self, width=0, height=0):
        self.button.x, self.button.y = round(self.button.x) + width, round(self.button.y) + height
        self.__rect__update__()


class ButtonMod(ButtonBase):
    def __init__(
            self, event, window: py.surface.Surface#, size_config: tuple[int, int] | float = 0
    ):
        self.event = event
        self.surface = window
        self.size_config = 0
        ButtonBase.__init__(self)

    def copy(self):
        return ButtonMod(
            self.event, self.surface
        )

    def __rect__update__(self):
        self.button_rect = Rectangle(
            self.button.x, self.button.y, self.button.size, self.surface
        )

    def add_coord(self, width=0, height=0):
        self.button.x, self.button.y = round(self.button.x) + width, round(self.button.y) + height
        self.__rect__update__()


class CanvasButton(ButtonModify):
    def __init__(
            self, event, window: py.surface.Surface, size_config: tuple[float, float] = (0,0)
    ):
        ButtonModify.__init__(self, event, window, "Text", size_config)

    def set_object(self, x, y, size: tuple = (float, float)):
        self.x, self.y = round(x), round(y)
        self.size_x, self.size_y = size
        self.size_x *= self.size_config[0]
        self.size_y *= self.size_config[1]
        self.size = self.size_x, self.size_y
        self.button_radius = self.size_y * 0.5
        self.__rect__update__()
        return self

    def callback(self, function, bool_custom: bool = False):
        if self.button_rect.get_rect().collidepoint((self.event.mouse.mx, self.event.mouse.my)) == bool_custom:
            if self.event.mouse.mouse_button_down():
                function()

        self.button_rect.draw_object(
            (100, 100, 100),
            0,
            round(self.button_radius),
            round(0.0526 * self.size_config[1]),
        )

from module.UI.animation import AnimationMoveExp
from module.UI.render import DrawTextExp
class ButtonCollector(AnimationMoveExp, ButtonModify, DrawTextExp):
    def __init__(self, event, surface: py.surface.Surface, class_text: "Text", size_config: tuple[int, int] | float = 0):
        self._buttons: dict[str, ButtonMod] = {}
        self.event = event
        self.text = class_text
        self.size_config = size_config
        self.surface = surface

    def add(self, name: str):
        if self._buttons.get(name):
            print(f"Button id {name} already registered")
            #raise IndexError()
        else:
            self._buttons[name] = ButtonMod(self.event, self.surface)

    def get(self, name: str):
        #print(sys.getsizeof(self._buttons[name]))
        return self._buttons[name]

    def set_object(self, name, x, y, size: tuple = (float, float)):
        self._buttons[name].x, self._buttons[name].y = round(x), round(y)
        self._buttons[name]._cache_key = None
        self._buttons[name]._move_to_x = 0
        self._buttons[name]._move_to_y = 0
        self._buttons[name].func1 = None
        self._buttons[name].func2 = None
        self._buttons[name].size = size
        self._buttons[name].size_x, self._buttons[name].size_y = size
        self._buttons[name].size_x *= self.size_config[0]
        self._buttons[name].size_y *= self.size_config[1]
        self._buttons[name].button_radius = round(self._buttons[name].size_y * 0.5)

        if self._buttons[name].size_y <= (self._buttons[name].button_radius * 2):
            self._buttons[name].size_y = self._buttons[name].button_radius * 2
        self._buttons[name].size = self._buttons[name].size_x, self._buttons[name].size_y
        self._buttons[name].__rect__update__()
        return self

    def callback(self, name, function, bool_custom: bool = True):
        if self._buttons[name].button_rect.get_rect().collidepoint((self.event.mouse.mx, self.event.mouse.my)) == bool_custom:
            self._buttons[name].button_rect.draw_object((205, 200, 200), 0, round(self._buttons[name].button_radius))
            self.event.mouse.set_choose_mouse(True)

            if self.event.mouse.mouse_button_down():
                self._buttons[name].button_rect.draw_object((205, 200, 200), 3, 10)
                function()

        self._buttons[name].button_rect.draw_object((205, 200, 200), 3, 10)

    def get_text(self, name, text, color: tuple = (0, 0, 0)):
        self.draw_text(
            self._buttons[name],
            text,
            self._buttons[name].x + 0.0125*self.size_config[0],
            self._buttons[name].y + 0.003*self.size_config[1],
            color
        )

    def remove(self, button_id):
        self._buttons.pop(button_id, None)

    def clear(self):
        self._buttons.clear()

    def get_buttons(self):
        return self._buttons

    @staticmethod
    def controller(button):
        return button.set_font()