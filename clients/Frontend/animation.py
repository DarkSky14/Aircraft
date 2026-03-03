is_move = True

class AnimationMove:
    def __init__(self) -> None:
        pass

    def moved(self, pixel_x = None, pixel_y = None, millisecounds: int = 0): # type: ignore #
        global is_move
        self.pixel_x = pixel_x
        self.pixel_y = pixel_y

        if is_move == True:
            if millisecounds == 0:
                times = 1
            else:
                times = (millisecounds / 10)

            if pixel_x == None:
                self.move_to_x = 0
                self.pixel_x = self.x
            else:
                self.move_to_x = ((pixel_x - self.x_true) / times)

            if pixel_y == None:
                self.move_to_y = 0
                self.pixel_y = self.y
            else:
                self.move_to_y = ((pixel_y - self.y_true) / times)
        
        else:
            self.pixel_x = self.x
            self.pixel_y = self.y
            self.move_to_x = 0
            self.move_to_y = 0
	
    def animation(self):
        self.x = (self.x + self.move_to_x)
        self.y = (self.y + self.move_to_y)
        if round(self.x) == self.pixel_x and round(self.y) == self.pixel_y:
            self.move_to_x = 0
            self.move_to_y = 0
            self.x_true = self.x
            self.y_true = self.y
            return True

class Resizable:
    def __init__(self) -> None:
        pass
