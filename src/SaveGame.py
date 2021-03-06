from xml.etree.ElementTree import ElementTree
from .structures.LinkedList import LinkedList
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

def find_games():
    try:
        games = ET.parse('games.xml')
        names = games.findall("./matriz/[nombre]")
        text_n = []
        text = ""
        i = 1
        for m in names:
            text_n.append(m[0].text)
            text += str(i) + ". " + m[0].text + "\n"            
            i += 1
        return text, text_n
    except:
        return "", ""

def open_game(name_searched):
    try:                
        games = ET.parse('games.xml')
        name = find_game(name_searched, games)
        # 0 nombre, 1 color1
        # 2 color2, 3 filas
        # 4 columnas, 5 texto 
        name_game = name[0].text.replace(" ", "")
        colorj1 = name[1].text.replace(" ", "")
        colorj2 = name[2].text.replace(" ", "")
        rows = int(name[3].text)
        columns = int(name[4].text)
        text = name[5].text.replace(" ", "").split("\n")   
        text.remove("")
        board = SparseMatrix()        
        if rows != len(text):
            return None,None,None,None,None,None                

        for i in range(len(text)):            
            if len(text[i]) != columns:                
                return None,None,None,None,None,None
            for j in range(len(text[i])):                                
                
                if text[i][j] != "-":    
                    number = 1
                    if text[i][j] == "2":
                        number = 2
                    elif text[i][j] == "1":
                        number = 1
                    else:
                        return None,None,None,None,None,None
                    board.insert(j+1, i+1, number)
        return name_game, colorj1,colorj2, rows, columns, board
    except:
        return None,None,None,None,None,None

def new_report(moves: LinkedList, colorj1, colorj2, winner, name):
    try:
        text_winner = "Empate"    
        color_winner = "#000"
        if winner != None:
            if winner.number == 1:
                text_winner ="Ganador J1"
                color_winner = colorj1
            else:
                text_winner = "Ganador J2"
                color_winner = colorj2
        new_node = """
        <div class="report">    
                <h2> Partida: """+name+"""</h2>
                <h3 style="color:"""+ colorj1 + """;">J1</h3>
                <h3 style="color:"""+ colorj2+""";">J2</h3>
                <h3 style="color: """+color_winner+""";">Resultado :""" +text_winner+"""</h3>
                <table>                
                    <tr>
                        <th colspan="6">MOVIMIENTOS</th>
                    </tr>
                    <tr>
                        <th>No.</th>
                        <th>Jugador</th>
                        <th>X</th>
                        <th>Y</th>
                        <th>Pieza</th>
                        <th>Status</th>
                    </tr>
                    <moves>                
                </table>
                <br/>
                <img src="./assets/"""+name+""".dot.png" alt="" width="500px">
                <hr/>
            </div>
                <!--n-->
        """
        text_moves = """"""
        for i in range(moves.length):
            data = moves.get_node(i+1).data
            text_moves += """
                <tr>
                    <td>"""+str(data.n)+"""</td>
                    <td>J"""+str(data.player_number)+"""</td>
                    <td>"""+str(data.x)+"""</td>
                    <td>"""+str(data.y)+"""</td>
                    <td><img src="./assets/figure"""+str(data.n_figure)+""".png" alt="" height="25px"></td>
                    <td>"""+data.message+"""</td>
                </tr>
            """
        new_node = new_node.replace("<moves>", text_moves)
        html = open('index.html', 'r')
        linea = html.read()    
        nuevo = linea.replace("<!--n-->", new_node)    
        html.close()
        html = open('index.html', 'w')
        html.write(nuevo)
        html.close()
    except ValueError:
        print(ValueError)


    
