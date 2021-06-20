from xml.etree.ElementTree import ElementTree
from .structures.SparseMatrix import SparseMatrix
import xml.etree.cElementTree as ET

def set_image(rows, columns, board : SparseMatrix):
    mapa = ""            
    for i in range(rows):
        for j in range(columns):
            square = board.search_node(i + 1, j + 1)
            if square == None:
                mapa += "-"
            else:
                mapa += str(square.square.player_number)
        mapa +="\n"
    return mapa

def find_game(name, games: ElementTree = None):
    if games == None:
        try:
            games = ET.parse('games.xml')
        except:
            return None
    return games.find("./matriz/[nombre='"+ name + "']")

    

def save_game(name, board : SparseMatrix, color1, color2):
    try:
        try: 
            games = ET.parse('games.xml')            
        except:            
            arbol = ET.ElementTree(ET.Element("matrices"))
            arbol.write('games.xml')
            games = ET.parse('games.xml')

        root = games.getroot()
        matrix = find_game(name, games)
        rows = board.max_rows
        columns = board.max_columns                
        if matrix != None:            
            imagen = matrix.find('imagen')
            imagen.text = set_image(rows, columns, board)
        else:                                    
            if root.tag != "matrices":
                return False            
            matrix = ET.SubElement(root, "matriz")
            nombre = ET.SubElement(matrix, "nombre")
            nombre.text = name     
            colorj1 = ET.SubElement(matrix, "color1")
            colorj1.text = color1                
            colorj2 = ET.SubElement(matrix, "color2")
            colorj2.text = color2
            filas = ET.SubElement(matrix, "filas")
            filas.text = str(board.max_rows)
            columnas = ET.SubElement(matrix, "columnas")
            columnas.text = str(board.max_columns)
            imagen = ET.SubElement(matrix, "imagen")            
            img = set_image(rows, columns, board)
            imagen.text = img
        arbol = ET.ElementTree(root)
        arbol.write('games.xml') 
        return True
    except ValueError:
        print(ValueError)
        return False
    
    def load_game():
        pass

