# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from ..Game import Game
from ..structures.LinkedList import LinkedList
from .Color import Color


class Ui_MainWindow(object):

    colors = LinkedList()
    colors.add(Color("Azul", "#00F"))
    colors.add(Color("Rojo", "#F00"))
    colors.add(Color("Amarillo", "#FFE800"))
    colors.add(Color("Verde", "#0F0"))
    playing = False    
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.espacio_juego = QtWidgets.QGroupBox(self.centralwidget)
        self.espacio_juego.setObjectName("espacio_juego")
        self.gridLayout = QtWidgets.QGridLayout(self.espacio_juego)
        self.gridLayout.setObjectName("gridLayout")
        self.tablero_juego = QtWidgets.QTableWidget(self.espacio_juego)
        self.tablero_juego.setObjectName("tablero_juego")
        self.tablero_juego.setColumnCount(0)
        self.tablero_juego.setRowCount(0)
        self.gridLayout.addWidget(self.tablero_juego, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.espacio_juego, 0, 0, 1, 3)
        self.frame_puntos_figura = QtWidgets.QFrame(self.centralwidget)
        self.frame_puntos_figura.setObjectName("frame_puntos_figura")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_puntos_figura)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame_puntos_figura)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.puntos_j1 = QtWidgets.QLabel(self.groupBox)
        self.puntos_j1.setObjectName("puntos_j1")
        self.verticalLayout.addWidget(self.puntos_j1)
        self.puntos_j2 = QtWidgets.QLabel(self.groupBox)
        self.puntos_j2.setObjectName("puntos_j2")
        self.verticalLayout.addWidget(self.puntos_j2)
        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)
        self.tablero_muestra = QtWidgets.QTableWidget(self.frame_puntos_figura)
        self.tablero_muestra.setObjectName("tablero_muestra")
        self.tablero_muestra.setColumnCount(0)
        self.tablero_muestra.setRowCount(0)
        self.gridLayout_3.addWidget(self.tablero_muestra, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_4.addWidget(self.frame_puntos_figura, 1, 2, 1, 1)
        self.controles_juego = QtWidgets.QGroupBox(self.centralwidget)
        self.controles_juego.setObjectName("controles_juego")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.controles_juego)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.controles_juego)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.text_x = QtWidgets.QLineEdit(self.controles_juego)
        self.text_x.setObjectName("text_x")
        self.horizontalLayout_2.addWidget(self.text_x)
        self.label_7 = QtWidgets.QLabel(self.controles_juego)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.text_y = QtWidgets.QLineEdit(self.controles_juego)
        self.text_y.setObjectName("text_y")
        self.horizontalLayout_2.addWidget(self.text_y)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(24, -1, 24, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_colocar = QtWidgets.QPushButton(self.controles_juego)
        self.button_colocar.setObjectName("button_colocar")
        self.horizontalLayout_3.addWidget(self.button_colocar)
        self.button_turno = QtWidgets.QPushButton(self.controles_juego)
        self.button_turno.setObjectName("button_turno")
        self.horizontalLayout_3.addWidget(self.button_turno)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.lcdNumber = QtWidgets.QLCDNumber(self.controles_juego)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_6.addWidget(self.lcdNumber)
        self.gridLayout_4.addWidget(self.controles_juego, 1, 1, 1, 1)
        self.config_juego = QtWidgets.QGroupBox(self.centralwidget)
        self.config_juego.setObjectName("config_juego")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.config_juego)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.color_jugador1 = QtWidgets.QComboBox(self.config_juego)
        self.color_jugador1.setObjectName("color_jugador1")
        self.color_jugador1.addItem("")
        self.color_jugador1.addItem("")
        self.color_jugador1.addItem("")
        self.color_jugador1.addItem("")
        self.verticalLayout_3.addWidget(self.color_jugador1)
        self.color_jugador2 = QtWidgets.QComboBox(self.config_juego)
        self.color_jugador2.setObjectName("color_jugador2")
        self.color_jugador2.addItem("")
        self.color_jugador2.addItem("")
        self.color_jugador2.addItem("")
        self.color_jugador2.addItem("")
        self.verticalLayout_3.addWidget(self.color_jugador2)
        self.label = QtWidgets.QLabel(self.config_juego)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.config_juego)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.text_tiempo = QtWidgets.QSpinBox(self.config_juego)
        self.text_tiempo.setMinimum(10)
        self.text_tiempo.setMaximum(60)
        self.text_tiempo.setProperty("value", 60)
        self.text_tiempo.setObjectName("text_tiempo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.text_tiempo)
        self.label_3 = QtWidgets.QLabel(self.config_juego)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.text_filas = QtWidgets.QSpinBox(self.config_juego)
        self.text_filas.setMinimum(5)
        self.text_filas.setMaximum(99)
        self.text_filas.setProperty("value", 10)
        self.text_filas.setObjectName("text_filas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.text_filas)
        self.label_4 = QtWidgets.QLabel(self.config_juego)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.text_cols = QtWidgets.QSpinBox(self.config_juego)
        self.text_cols.setMinimum(5)
        self.text_cols.setMaximum(99)
        self.text_cols.setProperty("value", 10)
        self.text_cols.setObjectName("text_cols")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.text_cols)
        self.label_5 = QtWidgets.QLabel(self.config_juego)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.text_piezas = QtWidgets.QLineEdit(self.config_juego)
        self.text_piezas.setMaxLength(3)
        self.text_piezas.setObjectName("text_piezas")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.text_piezas)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.button_iniciar = QtWidgets.QPushButton(self.config_juego)
        self.button_iniciar.setObjectName("button_iniciar")
        self.verticalLayout_4.addWidget(self.button_iniciar)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_4.addWidget(self.config_juego, 1, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 2)
        self.gridLayout_4.setRowStretch(0, 3)
        self.gridLayout_4.setRowStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 909, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuJuego = QtWidgets.QMenu(self.menuBar)
        self.menuJuego.setObjectName("menuJuego")
        MainWindow.setMenuBar(self.menuBar)
        self.actionEjemplos = QtWidgets.QAction(MainWindow)
        self.actionEjemplos.setObjectName("actionEjemplos")
        self.actionAbrir_partida = QtWidgets.QAction(MainWindow)
        self.actionAbrir_partida.setObjectName("actionAbrir_partida")
        self.actionGuardar_partida = QtWidgets.QAction(MainWindow)
        self.actionGuardar_partida.setObjectName("actionGuardar_partida")
        self.actionAyuda = QtWidgets.QAction(MainWindow)
        self.actionAyuda.setObjectName("actionAyuda")
        self.menuJuego.addAction(self.actionAbrir_partida)
        self.menuJuego.addAction(self.actionGuardar_partida)
        self.menuJuego.addAction(self.actionAyuda)
        self.menuBar.addAction(self.menuJuego.menuAction())

        self.text_piezas.setValidator(QtGui.QIntValidator())
        self.text_x.setValidator(QtGui.QIntValidator())
        self.text_x.setMaxLength(3)
        self.text_y.setValidator(QtGui.QIntValidator())
        self.text_y.setMaxLength(3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Juego"))
        self.groupBox.setTitle(_translate("MainWindow", "Puntos"))
        self.puntos_j1.setText(_translate("MainWindow", "J1:"))
        self.puntos_j2.setText(_translate("MainWindow", "J2:"))
        self.label_6.setText(_translate("MainWindow", " X:"))
        self.label_7.setText(_translate("MainWindow", "Y:"))
        self.button_colocar.setText(_translate("MainWindow", "Colocar"))
        self.button_turno.setText(_translate("MainWindow", "Terminar turno"))
        self.color_jugador1.setItemText(0, _translate("MainWindow", "Azul"))
        self.color_jugador1.setItemText(1, _translate("MainWindow", "Rojo"))
        self.color_jugador1.setItemText(2, _translate("MainWindow", "Amarillo"))
        self.color_jugador1.setItemText(3, _translate("MainWindow", "Verde"))
        self.color_jugador2.setItemText(0, _translate("MainWindow", "Rojo"))
        self.color_jugador2.setItemText(1, _translate("MainWindow", "Amarillo"))
        self.color_jugador2.setItemText(2, _translate("MainWindow", "Verde"))
        self.color_jugador2.setItemText(3, _translate("MainWindow", "Azul"))
        self.label.setText(_translate("MainWindow", "Colores"))
        self.label_2.setText(_translate("MainWindow", "Tiempo"))
        self.label_3.setText(_translate("MainWindow", "Filas"))
        self.label_4.setText(_translate("MainWindow", " Columnas"))
        self.label_5.setText(_translate("MainWindow", "#Piezas"))
        self.text_piezas.setPlaceholderText(_translate("MainWindow", "Cantidad"))
        self.button_iniciar.setText(_translate("MainWindow", "INICIAR"))
        self.menuJuego.setTitle(_translate("MainWindow", "Juego"))
        self.actionEjemplos.setText(_translate("MainWindow", "Ejemplos"))
        self.actionAbrir_partida.setText(_translate("MainWindow", "Abrir partida"))
        self.actionGuardar_partida.setText(_translate("MainWindow", "Guardar partida"))
        self.actionAyuda.setText(_translate("MainWindow", "Ayuda"))

    def show_info(self, text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()    

    def grid_game_board(self, rows, columns):
        self.tablero_muestra.setRowCount(4)
        self.tablero_muestra.setColumnCount(4)    
        self.tablero_juego.setRowCount(rows)
        self.tablero_juego.setColumnCount(columns)          
        self.tablero_juego.horizontalHeader().setDefaultSectionSize(75)
        self.tablero_juego.horizontalHeader().setMinimumSectionSize(75)                
        self.tablero_juego.verticalHeader().setDefaultSectionSize(50)
        self.tablero_juego.verticalHeader().setMinimumSectionSize(50)
        self.tablero_juego.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        #Tablero muestra
        self.tablero_muestra.horizontalHeader().setDefaultSectionSize(50)
        self.tablero_muestra.horizontalHeader().setMinimumSectionSize(50)                
        self.tablero_muestra.verticalHeader().setDefaultSectionSize(25)
        self.tablero_muestra.verticalHeader().setMinimumSectionSize(25)
        self.tablero_muestra.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
    def add_square(self, row, column, player_number, color):        
        self.tablero_juego.setItem(row, column, QtWidgets.QTableWidgetItem(str(player_number)))
        self.tablero_juego.item(row, column).setBackground(QtGui.QColor(color))
    
    def add_model_square(self, row, column, color):        
        self.tablero_muestra.setItem(row, column, QtWidgets.QTableWidgetItem("-"))
        self.tablero_muestra.item(row, column).setBackground(QtGui.QColor(color))  

    def get_color(self, color) -> str:        
        for i in range(Ui_MainWindow.colors.length):
            node = Ui_MainWindow.colors.get_node(i + 1)            
            if node != None:
                aux_color = node.data
                if color == aux_color.name:
                    return aux_color.code
        return "#FFF"
                
    def new_game(self):
        color_j1 = self.color_jugador1.currentText()
        color_j2 = self.color_jugador2.currentText()
        time = self.text_tiempo.value()
        self.columns = self.text_cols.value()
        self.rows = self.text_filas.value()
        n_pieces = self.text_piezas.text()
        if color_j1 != color_j2:
            if len(n_pieces) == 0:
                n_pieces = "1000"
            n_pieces = int(n_pieces)
            color_j1 = self.get_color(color_j1)
            color_j2 = self.get_color(color_j2)
            print(color_j1, color_j2)
            self.grid_game_board(self.rows, self.columns)
            self.game = Game(self.rows, self.columns, color_j1, color_j2, n_pieces, self)            
            Ui_MainWindow.playing = True
            self.config_juego.setEnabled(False)
            self.controles_juego.setEnabled(True)
        else:            
            self.show_info("Datos incorrectos\nRecuerde:\n1. Los colores de los jugadores deben ser diferentes")
                    
    def put_figures(self):
        try:
            row = int(self.text_y.text())
            column = int(self.text_x.text())                   
            if row > 0 and column > 0 and row <= self.rows and column <= self.columns:
                self.game.move(row, column)
            else:
                self.game.player_chance()
            self.text_x.clear()
            self.text_y.clear()
        except ValueError:
            self.show_info("Ingrese valores válidos")
            print(ValueError)

    def end_turn(self):
        self.game.change_turn()

    def add_actions(self):
        self.button_iniciar.clicked.connect(lambda: self.new_game())
        self.button_colocar.clicked.connect(lambda: self.put_figures())
        self.button_turno.clicked.connect(lambda: self.end_turn())
    
    def start(self):  
        self.add_actions()
        self.controles_juego.setEnabled(False)        
        self.game = None                
        #self.grid_espacio_juego(20,20)
        #self.game.add_model(self) # esto va en cuando ya se esté jugando
     



    

