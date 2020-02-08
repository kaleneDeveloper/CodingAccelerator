from PySide2 import QtCore, QtGui, QtWidgets
import sys

class App(QtWidgets.QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.setWindowTitle("Application 01")
        screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.resize(width/2, height/2)
        self.move(width/4, height/4)
        self.setup_UI()
        self.setup_css()       
    
    def setup_UI(self):
        self.operation = QtWidgets.QLineEdit()
        self.resulat = QtWidgets.QLineEdit()
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.btn_0 = QtWidgets.QPushButton("0")
        self.btn_1 = QtWidgets.QPushButton("1")
        self.btn_2 = QtWidgets.QPushButton("2")
        self.btn_3 = QtWidgets.QPushButton("3")
        self.btn_4 = QtWidgets.QPushButton("4")
        self.btn_5 = QtWidgets.QPushButton("5")
        self.btn_6 = QtWidgets.QPushButton("6")
        self.btn_7 = QtWidgets.QPushButton("7")
        self.btn_8 = QtWidgets.QPushButton("8")
        self.btn_9 = QtWidgets.QPushButton("9")

        self.btn_point = QtWidgets.QPushButton(".")
        self.btn_point = QtWidgets.QPushButton("+")
        self.btn_point = QtWidgets.QPushButton("-")
        self.btn_point = QtWidgets.QPushButton("x")
        self.btn_point = QtWidgets.QPushButton("/")
        self.btn_point = QtWidgets.QPushButton("=")
        self.btn_point = QtWidgets.QPushButton("C")

        self.gridLayout.addWidget(self.operation, 0, 0, 1,4)
        self.gridLayout.addWidget(self.resultat, 0, 0, 1,4)

        
    
    def setup_css(self):    
        self.setStyleSheet("""
        background-color: rgb(70, 70 ,70);
        color: rgb(255, 255, 255); 
               
        """)

def main():
    app = QtWidgets.QApplication(sys.argv)

    windows = App()
    windows.show()
    sys.exit(app.exec_())
    
main()




