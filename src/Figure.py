from .structures.SparseMatrix import SparseMatrix 

class Figure:
    def __init__(self, figure: SparseMatrix, inicio_x, inicio_y):
        self.figure = figure
        self.inicio_x = inicio_x
        self.inicio_y = inicio_y