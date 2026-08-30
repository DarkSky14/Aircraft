from module.event import Task

is_move = True


class AnimationMove:
    def __init__(self, size_config, button: "ButtonModify") -> None:
        self.object = button
        self.size_config = size_config
        self.x = button.x
        self.y = button.y
        self.func1 = None
        self.func2 = None
        self.move_status = False

    def moved(self, pixel_x=None, pixel_y=None, milliseconds: int = 0):  # type: ignore #
        global is_move
        if self.move_status is False:
            self.move_status = True
            if is_move:
                if milliseconds == 0:
                    times = 1
                else:
                    times = milliseconds / 10
                self.times = times

                if pixel_x is None:
                    self._move_to_x = 0
                else:
                    pixel_x = round(pixel_x * self.size_config)
                    self._move_to_x = (pixel_x - self.x) / times

                if pixel_y is None:
                    self._move_to_y = 0
                else:
                    pixel_y = round(pixel_y * self.size_config)
                    self._move_to_y = (pixel_y - self.y) / times

            else:
                if pixel_x is not None:
                    self.x = round(pixel_x * self.size_config)

                if pixel_y is not None:
                    self.y = round(pixel_y * self.size_config)

                self.times = 1
                self._move_to_x = 0
                self._move_to_y = 0


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


class Resizable:
    def __init__(self, size_config, button: "ButtonModify") -> None:
        self.object = button
        self.size_config = size_config
        self.size_x = button.size_x
        self.size_y = button.size_y

    def change_size(self, pixel_x_size=None, pixel_y_size=None, milliseconds=0):  # type: ignore
        global is_move
        if is_move:
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
