is_move = True


class Resizable:
    def __init__(self, size_config) -> None:
        self.size_config = size_config
        self.size_x = getattr(self, "x", 0)
        self.size_y = getattr(self, "y", 0)

    def change_size(self, pixel_x_size=None, pixel_y_size=None, milliseconds=0):  # type: ignore
        global is_move
        self.pixel_x_size = pixel_x_size
        self.pixel_y_size = pixel_y_size
        if is_move:
            if milliseconds == 0:
                times = 1
            else:
                times = milliseconds / 10

            if pixel_x_size is None:
                self.move_to_x_size = 0
                self.pixel_x_size = self.size_x
            else:
                self.move_to_x_size = (pixel_x_size - self.size_x) / times

            if pixel_y_size is None:
                self.move_to_y_size = 0
                self.pixel_y_size = self.size_y
            else:
                self.move_to_y_size = (pixel_y_size - self.size_y) / times

        else:
            self.pixel_x_size = self.size_x
            self.pixel_y_size = self.size_y
            self.move_to_x_size = 0
            self.move_to_y_size = 0

    def animation_resize(self, func=None):
        self.size_x = (self.size_x + self.move_to_x_size) * self.size_config
        self.size_y = (self.size_y + self.move_to_y_size) * self.size_config
        self.size = self.size_x, self.size_y
        if (
            round(self.size_x) == self.pixel_x_size
            and round(self.size_y) == self.pixel_y_size
        ):
            self.move_to_x_size = 0
            self.move_to_y_size = 0
            self.size = self.size_x, self.size_y
            self.pixel_x_size = None
            self.pixel_y_size = None
