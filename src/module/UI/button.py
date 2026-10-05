import pygame as py

from module.UI import AnimationMove, MyDrawObject, Text

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
        self.x, self.y = round(x), round(y)
        self.size = size
        self.size_x, self.size_y = size
        self.size_x *= self.size_config[0]
        self.size_y *= self.size_config[1]
        self.button_radius = round(self.size_y * 0.5)

        if self.size_y <= (self.button_radius * 2):
            self.size_y = self.button_radius * 2
        self.size = self.size_x, self.size_y
        self.__rect__update__()
        return self

    def callback(self, function, bool_custom: bool = True):
        if self.button_rect.get_rect().collidepoint((self.event.mouse.mx, self.event.mouse.my)) == bool_custom:
            self.button_rect.draw_object((205, 200, 200), 0, round(self.button_radius))
            self.event.mouse.set_choose_mouse(True)

            if self.event.mouse.mouse_button_down():
                self.button_rect.draw_object((205, 200, 200), 3, 10)
                function()

        self.button_rect.draw_object((205, 200, 200), 3, 10)

    def get_text(self, text, color: tuple = (0, 0, 0)):
        self.text.draw_text(text, self.x + 15, self.y + 2, color)

    def set_surface(self, surface):
        self.surface = surface
        self.text.surface = surface
        self.__rect__update__()

    def __rect__update__(self):
        self.button_rect = MyDrawObject(self.x, self.y, self.size, self.surface)

    def add_coord(self, width=0, height=0):
        self.x, self.y = round(self.x) + width, round(self.y) + height
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


class ButtonCollector:
    def __init__(self):
        self._buttons: dict[str, ButtonModify] = {}

    def add(self, button: "ButtonModify"):
        if button.id in self._buttons:
            raise IndexError(
                f"Button id {button.id} already registered"
            )
        self._buttons.update({button.id: button})
        return button.return_self()

    def remove(self, button_id):
        self._buttons.pop(button_id, None)

    def get_button(self, button_id):
        return self._buttons[button_id].return_self()

    def create_button(self, button_class: "ButtonModify"):
        self.add(button_class)
        return button_class.return_self()

    def clear(self):
        self._buttons.clear()

    def get_buttons(self):
        return self._buttons

    @staticmethod
    def controller(button):
        return button.set_font()