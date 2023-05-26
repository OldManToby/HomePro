import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(800, 250, 1000, 1000) # XPOS , YPOS, WIDTH, HEIGHT
        self.setWindowTitle("MotoGP History") # Set title
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self) #Label
        self.label.setText("Welcome to the MotoGP History App!")
        self.label.move(50,50) #XPOS, YPOS
        
        self.b1 = QtWidgets.QPushButton(self) #Button
        self.b1.setText("Press Me")
        self.b1.clicked.connect(self.clicked) #Connect with function
        self.b1.move(100,100) #XPOS, YPOS
        self.update()

    def clicked(self):
        self.label.setText("nice")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv) # Application setup
    win = MainWindow()
    win.show() #Show window
    sys.exit(app.exec_())

window()

