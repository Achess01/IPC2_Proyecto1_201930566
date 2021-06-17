class Player:
    def __init__(self, number, color, n_pieces):
        self.number = number
        self.color = color
        self.n_pieces = n_pieces
        self.chance = 2
    
    def calc_points():
        pass

    def minus_chache(self):
        self.chance = self.chance - 1;
        if self.chance > 0:
            return self.chance()
        else: 
            self.chance = 2
            return 0