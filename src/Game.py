from .Player import Player
from .structures.LinkedList import LinkedList
from .structures.SparseMatrix import SparseMatrix
from PyQt5 import QtWidgets
import random


class Game:
    CANTIDAD_FIGURAS = 6    
    figures_list = LinkedList()
    # Definiendo figura 1 "L"    
    figure1 = SparseMatrix()
    figure1.insert(1,1,1)
    #figure1.insert(2,1,-1)
    figure1.insert(1,2,1)
    #figure1.insert(2,2,-1)
    figure1.insert(1,3,1)
    #figure1.insert(2,3,-1)
    figure1.insert(1,4,1)
    figure1.insert(2,4,1)
    figures_list.add(figure1)
    # Definiendo figura 2 "L" invertida    
    figure2 = SparseMatrix()
    #figure2.insert(1,1,-1)
    figure2.insert(2,1,1)
    #figure2.insert(1,2,-1)
    figure2.insert(2,2,1)
    #figure2.insert(1,3,-1)
    figure2.insert(2,3,1)
    figure2.insert(1,4,1)
    figure2.insert(2,4,1)
    figures_list.add(figure2)
    # Definiendo figura 3 "4 cuadros horizontales"    
    figure3 = SparseMatrix()
    figure3.insert(1,1,1)
    figure3.insert(2,1,1)
    figure3.insert(3,1,1)
    figure3.insert(4,1,1)    
    figures_list.add(figure3)
    # Definiendo figura 4 "Cuadrado 2x2"    
    figure4 = SparseMatrix()
    figure4.insert(1,1,1)
    figure4.insert(2,1,1)
    figure4.insert(1,2,1)
    figure4.insert(2,2,1)    
    figures_list.add(figure4)
    #Definiendo figura 5 "Pieza formada por cuatro posiciones 
    #formando una línea horizontal y, sobre esas
    #cuatro posiciones, dos cuadros formando una línea horizontal a manera de simular
    #una pirámide."    
    figure5 = SparseMatrix()
    #figure5.insert(1,1,-1)
    figure5.insert(2,1,1)
    figure5.insert(3,1,1)
    #figure5.insert(4,1,-1)
    figure5.insert(1,2,1)
    figure5.insert(2,2,1)
    figure5.insert(3,2,1)
    figure5.insert(4,2,1)
    figures_list.add(figure5)
     # Definiendo figura 4 "4 cuadros verticales"    
    figure6 = SparseMatrix()
    figure6.insert(1,1,1)
    figure6.insert(1,2,1)
    figure6.insert(1,3,1)
    figure6.insert(1,4,1)    
    figures_list.add(figure6)   
           
    def __init__(self, color_j1, color_j2, n_pieces, ui):
        self.ui = ui
        self.players = LinkedList()
        self.players.add(Player(1,color_j1, n_pieces))
        self.players.add(Player(2,color_j2, n_pieces))
        self.board = SparseMatrix()              
        self.initial_turn()
        self.add_model()
        
    
    def initial_turn(self):
        ran = random.randint(1,2)
        self.turn = self.players.get_node(ran)

    def change_turn(self):
        self.turn = self.turn.get_next()
        if self.turn == None:
            self.turn = self.players.get_node(1)
          
    
    def add_model(self) -> SparseMatrix:        
        color = self.turn.data.color
        ran = random.randint(1, Game.CANTIDAD_FIGURAS)
        node = Game.figures_list.get_node(ran)                
        for i in range(node.data.rows):
            for j in range(node.data.columns):                
                row = i + 1
                column = j + 1
                square = node.data.search_node(row, column)                                 
                if square != None:                    
                    self.ui.add_model_square(i, j, color)
        return node


