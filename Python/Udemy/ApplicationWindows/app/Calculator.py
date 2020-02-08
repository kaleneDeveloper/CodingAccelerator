from PySide2 import QtCore, QtGui, QtWidgets
import sys
import os
class App(QtWidgets.QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.setWindowTitle("Application 01")
        screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        # self.resize(width/2, height/2)
        self.move(width/4, height/4)
        self.setup_UI()
        self.setup_css()       
    
    def setup_UI(self):
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.operation = QtWidgets.QLineEdit()
        self.resultat = QtWidgets.QLineEdit()
        self.operation.setFont(font)
        self.resultat.setFont(font)
        
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

        self.btn_dot = QtWidgets.QPushButton(".")
        self.btn_plus = QtWidgets.QPushButton("+")
        self.btn_minus = QtWidgets.QPushButton("-")
        self.btn_times = QtWidgets.QPushButton("x")
        self.btn_integer = QtWidgets.QPushButton("/")
        self.btn_equal = QtWidgets.QPushButton("=")
        self.btn_clear = QtWidgets.QPushButton("C")
        

        self.gridLayout.addWidget(self.operation, 0, 0, 1, 4)
        self.gridLayout.addWidget(self.resultat, 1, 0, 1, 4)
        self.gridLayout.addWidget(self.btn_clear, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_integer, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_times, 3, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_4, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_5, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_6, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_minus, 4, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_1, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_2, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_3, 5, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_plus, 5, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_0, 6, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_dot, 6, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_equal, 6, 3, 1, 1)
        
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setFixedSize(64, 64)
                widget.setFont(font)
    
    def setup_css(self):    
        self.setStyleSheet("""
        background-color: rgb(70, 70 ,70);
        color: rgb(255, 255, 255); 
               
        """)

def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    windows = App()
    windows.show()
    sys.exit(app.exec_())
    
main()