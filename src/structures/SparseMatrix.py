from src.Square import Square
from src.structures.MatrixNode import MatrixNode


class SparseMatrix:
    def __init__(self):
        self.root = MatrixNode(0,0, Square(0))
        self.rows = 0
        self.columns = 0

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
        row = MatrixNode(rowNumber, 0, Square(0))
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
            if aux.y == rowNumber:
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
    
    def insert(self, x, y, player_number):
        newNode = MatrixNode(x, y, Square(player_number))
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
        row = rowHead.get_right()
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



                


    
   

        