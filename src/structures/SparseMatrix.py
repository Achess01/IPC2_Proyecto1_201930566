from src.Square import Square
from src.structures.MatrixNode import MatrixNode
from graphviz import Digraph


class SparseMatrix:
    def __init__(self):
        self.root = MatrixNode(0,0, Square(0))
        self.rows = 0
        self.columns = 0
        self.max_rows = 0
        self.max_columns = 0
    
    def set_max(self, max_rows, max_columns):
        self.max_rows = max_rows
        self.max_columns = max_columns

    def insertColumn(self, columnNumber) -> MatrixNode:
        header = self.root.get_right()
        column = MatrixNode(columnNumber, 0, Square(0))
        if header == None:
            # Agrega la nueva columna a la derecha del root
            self.root.set_right(column)
            column.set_left(self.root)
            self.columns += 1
            return column
        else:
            if header.x > columnNumber:
                # Agrega la nueva columna entre el root y otra columna
                column.set_right(header)
                column.set_left(self.root)
                self.root.set_right(column)
                header.set_left(column)
                self.columns += 1
                return column
            else:
                aux = header
                while aux.get_right() != None:
                    if aux.get_right().x > columnNumber:
                        # Agrega una columna entre dos.
                        aux2 = aux.get_right()
                        column.set_right(aux2)
                        column.set_left(aux)
                        aux2.set_left(column)
                        aux.set_right(column)
                        self.columns += 1
                        return column
                    aux = aux.get_right()
                aux.set_right(column)
                column.set_left(aux)
                self.columns += 1
                return column
                                            
    def insertRow(self, rowNumber) -> MatrixNode:
        header = self.root.get_down()
        row = MatrixNode(0, rowNumber, Square(0))
        if header == None:
            # Agrega la nueva fila a la derecha del root
            self.root.set_down(row)
            row.set_up(self.root)
            self.rows += 1
            return row
        else:
            if header.y > rowNumber:
                # Agrega la nueva fila entre el root y otra fila
                row.set_down(header)
                row.set_up(self.root)
                self.root.set_down(row)
                header.set_up(row)
                self.rows += 1
                return row
            else:
                aux = header
                while aux.get_down() != None:
                    if aux.get_down().y > rowNumber:
                        # Agrega una fila entre dos.
                        aux2 = aux.get_down()
                        row.set_down(aux2)
                        row.set_up(aux)
                        aux2.set_up(row)
                        aux.set_down(row)
                        self.rows += 1
                        return row
                    aux = aux.get_down()
                aux.set_down(row)
                row.set_up(aux)
                self.rows += 1
                return row
    
    def getRow(self, rowNumber, create : bool) -> MatrixNode:
        aux = self.root.get_down()
        while aux != None:
            if aux. y== rowNumber:
                return aux
            aux = aux.get_down()
        if create:
            return self.insertRow(rowNumber)
        return None


    
    def getColumn(self, columnNumber, create: bool):
        aux = self.root.get_right()
        while aux != None:
            if aux.x == columnNumber:
                return aux
            aux = aux.get_right()
        if create:
            return self.insertColumn(columnNumber)
        return None
    
    def insert(self, column, row, player_number):
        newNode = MatrixNode(column, row, Square(player_number))
        x = newNode.x
        y = newNode.y

        rowHead = self.getRow(y, True)
        columnHead = self.getColumn(x, True)
        # En columna
        col = rowHead.get_right()
        if col == None:
            rowHead.set_right(newNode)
            newNode.set_left(rowHead)
        else:
            if col.x > x:
                newNode.set_right(col);
                newNode.set_left(rowHead)
                rowHead.set_right(newNode)
                col.set_left(newNode)
            elif col.x < x:
                aux = col
                inserted = False
                while aux.get_right() != None:
                    if aux.get_right().x > x:
                        aux2 = aux.get_right()
                        newNode.set_right(aux2)
                        newNode.set_left(aux)
                        aux.set_right(newNode)
                        aux2.set_left(newNode)
                        inserted = True
                        break
                    aux = aux.get_right()
                if not inserted:
                    aux.set_right(newNode)
                    newNode.set_left(aux)
            else:
                # El nodo ya existe
                pass
        
        # En fila
        row = columnHead.get_down()
        if row == None:
            columnHead.set_down(newNode)
            newNode.set_up(columnHead)
        else:
            if row.y > y:
                newNode.set_down(row);
                newNode.set_up(columnHead)
                columnHead.set_down(newNode)
                row.set_up(newNode)
            elif row.y < y:
                aux = row
                inserted = False
                while aux.get_down() != None:
                    if aux.get_down().y > y:
                        aux2 = aux.get_down()
                        newNode.set_down(aux2)
                        newNode.set_up(aux)
                        aux.set_down(newNode)
                        aux2.set_up(newNode)
                        inserted = True
                        break
                    aux = aux.get_down()
                if not inserted:
                    aux.set_down(newNode)
                    newNode.set_up(aux)
            else:
                # El nodo ya existe
                pass

    def search_node(self, row, column) -> MatrixNode:
        rowHead = self.getRow(row, False)
        if rowHead != None:            
            tmp = rowHead.get_right()
            while tmp != None:
                if tmp.x == column:
                    return tmp    
                tmp = tmp.get_right()    
        return None 

    def is_insertable(self, row, column, player_number, figure):
        if self.max_rows != None and self.max_columns != None:            
            translate_x = column - figure.inicio_x
            translate_y = row - figure.inicio_y 
            aux = figure.figure.root                              
            aux = aux.get_down()        
            while aux != None:              
                aux2 = aux.get_right()
                while aux2 != None:                                    
                    x = aux2.x + translate_x
                    y = aux2.y + translate_y
                    if x > 0 and x <= self.max_columns and y > 0 and y <= self.max_rows:                              
                        square = self.search_node(y, x)
                        left = self.search_node(y, x - 1)
                        right = self.search_node(y, x + 1)
                        up = self.search_node(y - 1, x)
                        down = self.search_node(y + 1, x)
                        if square != None:
                            return False
                        if left != None:
                            if left.square.player_number == player_number:
                                return False
                        if right != None:
                            if right.square.player_number == player_number:
                                return False
                        if up != None:
                            if up.square.player_number == player_number:
                                return False
                        if down != None:
                            if down.square.player_number == player_number:
                                return False
                    else:
                        return False
                    aux2 = aux2.get_right()
                aux = aux.get_down()        
        return True

    def show(self, colorj1, colorj2, name, show):
        dot = Digraph(format='png', filename='assets/' + name + '.dot',
        node_attr={'style': 'filled', 'shape': 'box'})                     
        aux = self.root                
        # Creando nodos
        while aux != None:   
            aux2 = aux
            with dot.subgraph() as s:                
                while aux2 != None:                
                    n = aux2.square.player_number
                    text = str(n)             
                    color = "white"
                    x= str(aux2.x)
                    y= str(aux2.y)    
                    if n == 1:
                        color = colorj1
                    elif n == 2:
                        color = colorj2
                    else:
                        color = 'lightblue'
                        text = "(" + x+ ", " + y+")"
                                       
                    s.attr(rank='same')
                    s.attr('node', color=color)                    
                    s.node('node'+x+y, text)                     
                    aux2 = aux2.get_right()
                aux = aux.get_down() 
        #Creando enlaces
        aux = self.root                        
        while aux != None:
            aux2 = aux
            while aux2 != None:             
                x = aux2.x
                y = aux2.y                                                               
                if aux2.get_down() != None:
                    aux3 = aux2.get_down()
                    y2 = aux3.y
                    dot.edge('node'+str(x)+str(y), 'node'+str(x)+str(y2), dir="both")                    
                aux2 = aux2.get_down()   
            aux = aux.get_right()   
        if show:
            dot.view()
        else: 
            dot.render()

        
                


    
   

        