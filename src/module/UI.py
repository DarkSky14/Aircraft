from pygame import MOUSEBUTTONDOWN, draw, surface, Rect

try:
    from Text import Text, ModuleText
    from UI_module.animation import AnimationMove
except ImportError:
    from module.Text import Text, ModuleText
    from module.UI_module.animation import AnimationMove


class MyDrawObject:  # Correct
    def __init__(
        self, left: float, top: float, size: tuple, surface: surface.Surface
    ) -> None:
        self.top = top
        self.left = left
        self.size = size
        self.surface = surface
        self.rect = Rect((self.left, self.top), self.size)

    def draw_object(
        self, color: tuple, border: int = 0, border_radius: int = 0, radius: int = 50
    ) -> Rect:
        return draw.rect(
            self.surface, color, self.rect, border, border_radius, 
            radius, radius, radius, radius,
        )

    def get_rect(self) -> Rect:
        return self.rect


class Button(AnimationMove):
    def __init__(
        self, event, surface: surface.Surface, size_config: int | float = 0
    ):
        self.event = event
        self.surface = surface
        self.size_config = size_config
        self.x, self.y= 0, 0
        self.size = 0, 0
        self.size_x, self.size_y = self.size
        self.b_radius = 0
        self.draw_button = MyDrawObject
        AnimationMove.__init__(self, self.size_config)

    # @abstractmethod
    def copy(self):
        return Button(self.event, self.surface, self.size_config)

    def __copy_object__(self):
        return self.x, self.y, self.size

    def set_object(self, x, y, size: tuple = (int, int)):
        self.x, self.y = round(x), round(y)
        self.size = size
        self.size_x, self.size_y = size
        self.size_x *= self.size_config
        self.size_y *= self.size_config
        self.b_radius = round(self.size_y * 0.5)

        if self.size_y <= (self.b_radius * 2):
            self.size_y = self.b_radius * 2
        self.size = self.size_x, self.size_y
        return self.x, self.y, self.size

    def get_position(self):
        return self.x, self.y

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def get_size(self):
        return self.size_x, self.size_y

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y


class ModuleButton(Button, ModuleText):
    def __init__(
        self, event, surface: surface.Surface, config,
        class_text: Text, size_config: int | float = 0,
    ):
        Button.__init__(self, event, surface, size_config)
        ModuleText.__init__(self, class_text)
        self.config = config

    def copy(self):
        return ModuleButton(
            self.event, self.surface, self.config, self.class_text, self.size_config
        )

    def check_config(self, text, effect_click=None):
        return self.config.check(text, effect_click)

    def write_in_config(self, text):
        self.config.write(text)

    def text_change(self, change, change_x, change_y):
        self.set_change_text(change, change_x, change_y)

    def get_text_self(self, base_key, color: tuple = (0, 0, 0)):
        self.get_set_text(base_key, self.x + 15, self.y + 2, color)

    def get_text(self, text_class: ModuleText, base_key, color: tuple = (0, 0, 0)):
        text_class.get_set_text(base_key, self.x + 15, self.y + 2, color)

    def Button(self, function1):
        button = self.draw_button(self.x, self.y, self.size, self.surface)  # type: ignore

        if button.rect.collidepoint(self.event.mx, self.event.my):
            button.draw_object((205, 200, 200), self.b_radius, 10)
            self.event.set_choose_button(1)
            self.event.set_choose_fake_button(1)

            if self.event.comparison_type(MOUSEBUTTONDOWN) and self.event.get_click():
                button.draw_object((205, 200, 200), 3, 10)
                self.event.set_choose_button(0)
                self.event.set_click(False)
                function1()

        button.draw_object((205, 200, 200), 3, 10)


class SurfaceM(Button):
    def __init__(
        self, event, surface: surface.Surface, x_move=0,
        y_move=0, size_config: float = 0,
    ):
        self.x_move = x_move
        self.y_move = y_move
        Button.__init__(self, event, surface, size_config)

    def copy(self):
        return SurfaceM(
            self.event, self.surface, self.x_move, self.y_move, self.size_config
        )

    def set_object(self, x, y, size):
        self.x, self.y = x * self.size_config, y * self.size_config
        self.size_x, self.size_y = size
        self.size = size
        self.b_radius = self.size_y / 2
        self.sub_surface = MyDrawObject(self.x, self.y, self.size, self.surface)
        return self.x, self.y, self.size

    def update_pos(self):
        self.sub_surface = MyDrawObject(self.x, self.y, self.size, self.surface)
        self.b_radius = self.size_y / 2

    def main_work(self, exit):
        surface = self.sub_surface.draw_object(
            (100, 100, 100), 
            round(self.b_radius),
            round(30 * self.size_config),
            round(40 * self.size_config),
        )
        # surface = self.sub_surface(self.x, self.y, self.size, self.surface) #type: ignore
        # surface.draw_object((100, 100, 100), round(self.b_radius), round(30*self.size_config), round(40*self.size_config))

        if not surface.collidepoint((self.event.mx, self.event.my)):
            self.event.set_choose_button(1)
            if self.event.comparison_type(MOUSEBUTTONDOWN) and self.event.get_click():
                self.event.set_choose_button(0)
                self.event.set_click(False)
                exit()
