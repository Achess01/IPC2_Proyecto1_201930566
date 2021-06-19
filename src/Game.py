from .Player import Player
from .structures.LinkedList import LinkedList
from .structures.SparseMatrix import SparseMatrix
from PyQt5 import QtWidgets
from .Figure import Figure
import random


class Game:
    CANTIDAD_FIGURAS = 6
    figures_list = LinkedList()
    # Definiendo figura 1 "L"

    figure1 = Figure(SparseMatrix(), 1,1)
    figure1.figure.insert(1,1,1)
    #figure1.insert(2,1,-1)
    figure1.figure.insert(1,2,1)
    #figure1.insert(2,2,-1)
    figure1.figure.insert(1,3,1)
    #figure1.insert(2,3,-1)
    figure1.figure.insert(1,4,1)
    figure1.figure.insert(2,4,1)
    figures_list.add(figure1)
    # Definiendo figura 2 "L" invertida
    figure2 = Figure(SparseMatrix(), 2,1)
    #figure2.insert(1,1,-1)
    figure2.figure.insert(2,1,1)
    #figure2.figure.insert(1,2,-1)
    figure2.figure.insert(2,2,1)
    #figure2.figure.insert(1,3,-1)
    figure2.figure.insert(2,3,1)
    figure2.figure.insert(1,4,1)
    figure2.figure.insert(2,4,1)
    figures_list.add(figure2)
    # Definiendo figura 3 "4 cuadros horizontales"
    figure3 = Figure(SparseMatrix(), 1,1)
    figure3.figure.insert(1,1,1)
    figure3.figure.insert(2,1,1)
    figure3.figure.insert(3,1,1)
    figure3.figure.insert(4,1,1)
    figures_list.add(figure3)
    # Definiendo figura 4 "Cuadrado 2x2"
    figure4 = Figure(SparseMatrix(), 1,1)
    figure4.figure.insert(1,1,1)
    figure4.figure.insert(2,1,1)
    figure4.figure.insert(1,2,1)
    figure4.figure.insert(2,2,1)
    figures_list.add(figure4)
    #Definiendo figura 5 "Pieza formada por cuatro posiciones
    #formando una línea horizontal y, sobre esas
    #cuatro posiciones, dos cuadros formando una línea horizontal a manera de simular
    #una pirámide."
    figure5 = Figure(SparseMatrix(), 2,1)
    #figure5.figure.insert(1,1,-1)
    figure5.figure.insert(2,1,1)
    figure5.figure.insert(3,1,1)
    #figure5.figure.insert(4,1,-1)
    figure5.figure.insert(1,2,1)
    figure5.figure.insert(2,2,1)
    figure5.figure.insert(3,2,1)
    figure5.figure.insert(4,2,1)
    figures_list.add(figure5)
     # Definiendo figura 6 "4 cuadros verticales"
    figure6 = Figure(SparseMatrix(), 1,1)
    figure6.figure.insert(1,1,1)
    figure6.figure.insert(1,2,1)
    figure6.figure.insert(1,3,1)
    figure6.figure.insert(1,4,1)
    figures_list.add(figure6)

    def __init__(self,rows, columns, color_j1, color_j2, n_pieces, ui):
        self.ui = ui
        self.players = LinkedList()
        self.players.add(Player(1,color_j1, n_pieces))
        self.players.add(Player(2,color_j2, n_pieces))
        self.board = SparseMatrix()
        self.board.set_max(rows, columns)
        self.initial_turn()
        self.actual_figure = self.add_model()
        self.winner = None
        self.draw = False

    def player_chance(self):
        n = self.turn.data.minus_chance()
        self.ui.show_info("Casilla inválida\nOportunidades restantes: " + str(n))
        if n < 1:
            self.change_turn()

    def initial_turn(self):
        ran = random.randint(1,2)
        self.turn = self.players.get_node(ran)

    def set_winner(self):
        #j1
        j1 = self.players.get_node(1).data
        #j2
        j2 = self.players.get_node(2).data
        if j1.points > j2.points:
            self.winner = j1
        elif j1.points < j2.points:
            self.winner = j2
        else:
            self.draw = True

    def is_playable(self):
        rows = self.board.max_rows
        columns = self.board.max_columns
        player_number = self.turn.data.number        
        for i in range(rows):
            for j in range(columns):
                square = self.board.search_node(i + 1, j + 1)
                if square == None:
                    if self.board.is_insertable(i+1, j+1, player_number, self.actual_figure):
                        return True
        return False

    def change_turn(self):
        self.turn.data.chance = 2
        self.turn = self.turn.get_next()
        if self.turn == None:
            self.turn = self.players.get_node(1)
        self.actual_figure = self.add_model()
        if not self.is_playable():
            self.set_winner()
            self.ui.end_game()
        
    

    def move(self, row, column):
        self.make_move(row, column)        
        #print(self.turn.data.color)
    
    def discount_piece(self):
        return self.turn.data.discount()
    
    def show_info_player(self):
        pieces = self.discount_piece()     
        points = self.turn.data.points       
        if self.turn.data.number == 1:
            self.ui.puntos_j1.setText("J1: " + str(points) + "pts.\n" + str(pieces) + " restantes")
        else:
            self.ui.puntos_j2.setText("J2: " + str(points) + "pts.\n" + str(pieces) + " restantes")

    def make_move(self, row, column):
        if self.board.is_insertable(row, column, self.turn.data.number, self.actual_figure):
            self.add_to_board(column, row)
            self.show_info_player()
            self.change_turn()
        else:
            self.player_chance()
            self.ui.show_info("No se puede insertar en esa casilla")

    def add_model(self) -> Figure:
        self.ui.tablero_muestra.clear()
        color = self.turn.data.color
        ran = random.randint(1, Game.CANTIDAD_FIGURAS)
        figure = Game.figures_list.get_node(ran).data
        node = figure.figure
        for i in range(node.rows):
            for j in range(node.columns):
                row = i + 1
                column = j + 1
                square = node.search_node(row, column)
                if square != None:
                    self.ui.add_model_square(i, j, color)
        return figure
    
    def add_to_board(self, x, y):        
        translate_x = x - self.actual_figure.inicio_x
        translate_y = y - self.actual_figure.inicio_y
        color = self.turn.data.color 
        number = self.turn.data.number        
        aux = self.actual_figure.figure.root
        aux = aux.get_down()
        while aux != None:
            aux2 = aux.get_right()
            while aux2 != None:
                column = aux2.x + translate_x
                row = aux2.y + translate_y
                self.ui.add_square(row - 1, column - 1, number, color)   
                self.board.insert(column, row, number)
                self.turn.data.add_point()
                aux2 = aux2.get_right()
            aux = aux.get_down()

