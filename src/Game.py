from UI.main_ui import Ui_MainWindow
from structures.LinkedList import LinkedList
from structures.SparseMatrix import SparseMatrix


class Game:
    figures_list = LinkedList()
    # Definiendo figura 1 "L"    
    figure1 = SparseMatrix()
    figure1.insert(1,1,1)
    figure1.insert(2,1,-1)
    figure1.insert(1,2,1)
    figure1.insert(2,2,-1)
    figure1.insert(1,3,1)
    figure1.insert(2,3,-1)
    figure1.insert(1,4,1)
    figure1.insert(2,4,1)
    figures_list.add(figure1)
    # Definiendo figura 2 "L" invertida    
    figure2 = SparseMatrix()
    figure2.insert(1,1,-1)
    figure2.insert(2,1,1)
    figure2.insert(1,2,-1)
    figure2.insert(2,2,1)
    figure2.insert(1,3,-1)
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
    figure5.insert(1,1,-1)
    figure5.insert(2,1,1)
    figure5.insert(3,1,1)
    figure5.insert(4,1,-1)
    figure5.insert(1,2,1)
    figure5.insert(2,2,1)
    figure5.insert(3,2,1)
    figure5.insert(4,2,1)
    figures_list.add(figure5)
     # Definiendo figura 4 "Cuadrado 2x2"    
    figure4 = SparseMatrix()
    figure4.insert(1,1,1)
    figure4.insert(1,2,1)
    figure4.insert(1,3,1)
    figure4.insert(1,4,1)    
    figures_list.add(figure4)   
    
    
    def __init__(self, ui : Ui_MainWindow):        
        pass
