from src.Game import Game
from src.UI.main_ui import Ui_MainWindow
from PyQt5 import QtWidgets


def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)    
    ui.start()
    # ui.grid_espacio_juego(20,20)
    # ui.add_square(1,1,1,"blue")        
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()