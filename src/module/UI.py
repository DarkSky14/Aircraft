import pygame as py
from module.UI_module.animation import is_move #AnimationMove

class MyDrawObject:  # Correct
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


class ButtonUtility:
    def __init__(self):
        pass

    def __rect__update__(self):
        self.button_rect = MyDrawObject(self.x, self.y, self.size, self.surface)


class AnimationMove(ButtonUtility):
    def __init__(self, size_config) -> None:
        self.size_config = size_config
        self.x = getattr(self, "x", 0)
        self.y = getattr(self, "y", 0)

    def moved(self, pixel_x=None, pixel_y=None, milliseconds: int = 0):  # type: ignore #
        global is_move
        self._pixel_x = pixel_x
        self._pixel_y = pixel_y

        if is_move:
            if milliseconds == 0:
                times = 1000
            else:
                times = milliseconds / 10

            if pixel_x is None:
                self._move_to_x = 0
                self._pixel_x = round(self.x)
            else:
                self._pixel_x = round(self._pixel_x * self.size_config)
                self._move_to_x = (self._pixel_x - self.x) / times

            if pixel_y is None:
                self._move_to_y = 0
                self._pixel_y = round(self.y)
            else:
                self._pixel_y = round(self._pixel_y * self.size_config)
                self._move_to_y = (self._pixel_y - self.y) / times

        else:
            if pixel_x is None:
                self._pixel_x = self.x
            else:
                self.x = round(self._pixel_x * self.size_config)

            if pixel_y is None:
                self._pixel_y = self.y
            else:
                self.y = round(self._pixel_y * self.size_config)

            self._move_to_x = 0
            self._move_to_y = 0

    def animation(self, func=None):
        self.x += self._move_to_x
        self.y += self._move_to_y
        self.__rect__update__()
        if round(self.x) == self._pixel_x and round(self.y) == self._pixel_y:
            self._move_to_x = 0
            self._move_to_y = 0
            self.x_true = self.x
            self.y_true = self.y
            if func is not None:
                func()
                del func


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
            self, event, window: py.surface.Surface, size_config: int | float = 0
    ):
        self.event = event
        self.surface = window
        self.size_config = size_config
        super().__init__()

    def copy(self):
        return ButtonModify(
            self.event, self.surface, self.size_config
        )

    def set_object(self, x, y, size: tuple = (int, int)):
        self.x, self.y = round(x), round(y)
        self.size = size
        self.size_x, self.size_y = size
        self.size_x *= self.size_config
        self.size_y *= self.size_config
        self.button_radius = round(self.size_y * 0.5)

        if self.size_y <= (self.button_radius * 2):
            self.size_y = self.button_radius * 2
        self.size = self.size_x, self.size_y
        self.__rect__update__()
        return self

    def callback(self, function1, bools: bool = True, this_is_button: bool = True):
        if self.button_rect.get_rect().collidepoint((self.event.mx, self.event.my)) == bools:
            self.button_rect.draw_object((205, 200, 200), 0, round(self.button_radius))
            self.event.set_choose_button(True)
            self.event.set_choose_fake_button(this_is_button)

            if self.event.comparison_type(py.MOUSEBUTTONDOWN) and self.event.get_click():
                self.button_rect.draw_object((205, 200, 200), 3, 10)
                #self.event.set_choose_fake_button(False)
                self.event.set_click(False)
                function1()

        self.button_rect.draw_object((205, 200, 200), 3, 10)

    def get_text(self, class_text, text, color: tuple = (0, 0, 0)):
        class_text.get_set_text(text, self.x + 15, self.y + 2, color)


class CanvasButton(ButtonModify):
    def __init__(
            self, event, window: py.surface.Surface, size_config: int | float = 0
    ):
        ButtonModify.__init__(self, event, window, size_config)

    def set_object(self, x, y, size: tuple = (int, int)):
        self.x, self.y = round(x), round(y)
        self.size_x, self.size_y = size
        self.size = size
        self.button_radius = self.size_y * 0.5
        self.__rect__update__()
        return self

    def callback(self, exit, ):
        if not self.button_rect.get_rect().collidepoint((self.event.mx, self.event.my)):
            self.event.set_choose_button(True)
            if self.event.comparison_type(py.MOUSEBUTTONDOWN) and self.event.get_click():
                self.event.set_choose_button(False)
                self.event.set_click(False)
                exit()

        self.button_rect.draw_object(
            (100, 100, 100),
            0,
            round(self.button_radius),
            round(40 * self.size_config),
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
        return button.return_self()