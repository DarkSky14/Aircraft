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
	
    def animation(self, func = None): # type: ignore #
        self.x = (self.x + self.move_to_x)
        self.y = (self.y + self.move_to_y)
        if round(self.x) == self.pixel_x and round(self.y) == self.pixel_y:
            self.move_to_x = 0
            self.move_to_y = 0
            self.x_true = self.x
            self.y_true = self.y
            func  # type: ignore
            #return True

class Resizable:
    def __init__(self) -> None:
        pass

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
        self.size_x = (self.size_x + self.move_to_x_size)
        self.size_y = (self.size_y + self.move_to_y_size)
        self.size = self.size_x, self.size_y
        if round(self.size_x) == self.pixel_x_size and round(self.size_y) == self.pixel_y_size:
            self.move_to_x_size = 0
            self.move_to_y_size = 0         
            self.size = self.size_x, self.size_y
            self.pixel_x_size = None
            self.pixel_y_size = None
            func  # type: ignore
            del func 

    def add_func_resize(self, func): 
        print("void")
        self.func = func
