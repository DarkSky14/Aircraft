class AnimationMove:
    def __init__(self, size_config, button: "ButtonModify") -> None:
        self.object = button
        self.size_config = size_config
        self.x = button.x
        self.y = button.y
        self.func1 = None
        self.func2 = None
        self.move_status = False
        self.times = 0
        self._move_to_x = 0
        self._move_to_y = 0

    def moved(self, pixel_x=None, pixel_y=None, milliseconds: int = 0):  # type: ignore #
        self.move_status = True
        self.times = 1

        if self.object.text.config.check({"animation": "True"}):
            if milliseconds > 0:
                self.times = 60 * milliseconds

            if pixel_x is not None:
                pixel_x = round(pixel_x * self.size_config[0])
                self._move_to_x = (pixel_x - self.x) / self.times

            if pixel_y is not None:
                pixel_y = round(pixel_y * self.size_config[1])
                self._move_to_y = (pixel_y - self.y) / self.times

        else:
            if pixel_x is not None:
                self.x = round(pixel_x * self.size_config[0])

            if pixel_y is not None:
                self.y = round(pixel_y * self.size_config[1])

    def set_func(self, func1=None, func2 = None):
        if self.object.event.task.get_status() is False:
            self.object.event.task.set_status(True)
            self.func1 = func1
            self.func2 = func2

    def animation(self):
        if self.times > 0:
            self.x += self._move_to_x
            self.y += self._move_to_y
            self.object.__rect__update__()
            self.times -= 1
            if self.times == 0:
                self.move_status = False
                self.object.event.task.set_status(False)
                self._move_to_x = 0
                self._move_to_y = 0

                if self.func1 is not None:
                    self.object.event.task.add_task(self.func1)
                    self.func1 = None
                if self.func2 is not None:
                    self.object.event.task.add_task(self.func2)
                    self.func2 = None

class AnimationMoveExp:
    def __init__(self) -> None:
        self.size_config = (0, 0)
        self.move_status = False
        self.text = None

    def moved(self, name, pixel_x=None, pixel_y=None, milliseconds: float = 0):  # type: ignore #
        self.move_status = True
        name.times = 1

        if self.text.config.check({"animation": "True"}):
            if milliseconds > 0:
                name.times = 60 * milliseconds

            if pixel_x is not None:
                pixel_x = round(pixel_x * self.size_config[0])
                name._move_to_x = (pixel_x - name.x) / name.times

            if pixel_y is not None:
                pixel_y = round(pixel_y * self.size_config[1])
                name._move_to_y = (pixel_y - name.y) / name.times

        else:
            if pixel_x is not None:
                name.x = round(pixel_x * self.size_config[0])

            if pixel_y is not None:
                name.y = round(pixel_y * self.size_config[1])

    def set_func(self, name, func1=None, func2 = None):
        if name.event.task.get_status() is False:
            name.event.task.set_status(True)
            name.func1 = func1
            name.func2 = func2

    def animation(self, name):
        if name.times > 0:
            name.x += name._move_to_x
            name.y += name._move_to_y
            name.__rect__update__()
            name.times -= 1
            if name.times == 0:
                self.move_status = False
                name.event.task.set_status(False)
                name._move_to_x = 0
                name._move_to_y = 0

                if name.func1 is not None:
                    name.event.task.add_task(name.func1)
                    name.func1 = None
                if name.func2 is not None:
                    name.event.task.add_task(name.func2)
                    name.func2 = None


class Resizable:
    def __init__(self, size_config, button: "ButtonModify") -> None:
        self.object = button
        self.size_config = size_config
        self.size_x = button.size_x
        self.size_y = button.size_y

    def change_size(self, pixel_x_size=None, pixel_y_size=None, milliseconds=0):
        if self.object.text.config.check({"animation": "True"}):
            if milliseconds == 0:
                times = 1
            else:
                times = milliseconds / 100
            self.times = times

            if pixel_x_size is None:
                self.move_to_x_size = 0
            else:
                self.move_to_x_size = (pixel_x_size - self.size_x) / times

            if pixel_y_size is None:
                self.move_to_y_size = 0
            else:
                self.move_to_y_size = (pixel_y_size - self.size_y) / times

        else:
            if pixel_x_size is not None:
                self.size_x = round(pixel_x_size * self.size_config)

            if pixel_y_size is not None:
                self.size_y = round(pixel_y_size * self.size_config)

            self.times = 1
            self.move_to_x_size = 0
            self.move_to_y_size = 0

    def animation_resize(self, func=None):
        if self.times > 0:
            self.size_x = (self.size_x + self.move_to_x_size) * self.size_config
            self.size_y = (self.size_y + self.move_to_y_size) * self.size_config
            self.size = self.size_x, self.size_y
            self.times -= 1
            if self.times == 0:
                self.move_to_x_size = 0
                self.move_to_y_size = 0
