from src.Square import Square


class MatrixNode:
    def __init__(self, x, y, square: Square):
        self.x = x        
        self.y = y
        self.right = None
        self.left = None
        self.up = None
        self.down = None
        self.square = square
    
    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def get_left(self):
        return self.left
    
    def set_left(self, left):
        self.left = left
    
    def get_up(self):
        return self.up
    
    def set_up(self, up):
        self.up = up
    
    def get_down(self):
        return self.down

    def set_down(self, down):
        self.down = down