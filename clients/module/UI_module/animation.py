is_move = True

class AnimationMove:
    def __init__(self, size_config) -> None:
        self.size_config = size_config

    def moved(self, pixel_x = None, pixel_y = None, millisecounds: int = 0): # type: ignore #
        global is_move
        self._pixel_x = pixel_x
        self._pixel_y = pixel_y

        if is_move == True:
            if millisecounds == 0:
                times = 1
            else:
                times = (millisecounds / 10)

            if pixel_x == None:
                self._move_to_x = 0
                self._pixel_x = round(self.x)
            else:
                self._pixel_x = round(self._pixel_x * self.size_config)
                self._move_to_x = (self._pixel_x - self.x) / times

            if pixel_y == None:
                self._move_to_y = 0
                self._pixel_y = round(self.y)
            else:
                self._pixel_y = round(self._pixel_y * self.size_config)
                self._move_to_y = (self._pixel_y - self.y) / times

        
        else:
            if pixel_x == None:
                self._pixel_x = self.x
            else:
                self.x = round(self._pixel_x * self.size_config)

            if pixel_y == None:
                self._pixel_y = self.y
            else:
                self.y = round(self._pixel_y * self.size_config)

            self._move_to_x = 0
            self._move_to_y = 0
	
    def animation(self, func = None): # type: ignore #
        self.x += self._move_to_x
        self.y += self._move_to_y
        if round(self.x) == self._pixel_x and round(self.y) == self._pixel_y:
            self._move_to_x = 0
            self._move_to_y = 0
            self.x_true = self.x
            self.y_true = self.y
            if func != None:
                func()
                del func 

class Resizable:
    def __init__(self, size_config) -> None:
        self.size_config = size_config

    def change_size(self, pixel_x_size = None, pixel_y_size = None, millisecounds = 0): # type: ignore
        global is_move
        self.pixel_x_size = pixel_x_size
        self.pixel_y_size = pixel_y_size
        if is_move == True:
            if millisecounds == 0:
                times = 1
            else:
                times = (millisecounds / 10)

            if pixel_x_size == None:
                self.move_to_x_size = 0
                self.pixel_x_size = self.size_x
            else:
                self.move_to_x_size = ((pixel_x_size - self.size_x) / times)

            if pixel_y_size == None:
                self.move_to_y_size = 0
                self.pixel_y_size = self.size_y
            else:
                self.move_to_y_size = ((pixel_y_size - self.size_y) / times)
        
        else:
            self.pixel_x_size = self.size_x
            self.pixel_y_size = self.size_y
            self.move_to_x_size = 0
            self.move_to_y_size = 0
    
    def animation_resize(self, func = None):
        self.size_x = (self.size_x + self.move_to_x_size) ^ self.size_config
        self.size_y = (self.size_y + self.move_to_y_size) ^ self.size_config
        self.size = self.size_x, self.size_y
        if round(self.size_x) == self.pixel_x_size and round(self.size_y) == self.pixel_y_size:
            self.move_to_x_size = 0
            self.move_to_y_size = 0         
            self.size = self.size_x, self.size_y
            self.pixel_x_size = None
            self.pixel_y_size = None
            if func != None:
                func()
                del func 

    def add_func_resize(self, func): 
        print("void")
        self.func = func
