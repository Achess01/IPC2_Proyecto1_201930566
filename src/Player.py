class Player:
    def __init__(self, number, color, n_pieces, color_name):
        self.number = number
        self.color = color
        self.color_name = color_name
        self.n_pieces = n_pieces
        self.chance = 2
        self.points = 0
            
    def add_point(self):
        self.points += 1
        
    def discount(self):
        self.n_pieces = self.n_pieces - 1
        return self.n_pieces

    def minus_chance(self):
        self.chance = self.chance - 1;
        if self.chance > 0:
            return self.chance
        else: 
            self.chance = 2
            return 0