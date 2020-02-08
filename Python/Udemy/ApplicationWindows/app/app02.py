from PySide2 import QtWidgets, QtGui, QtCore
import sys

class App(QtWidgets.QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.setWindowTitle("Application 02")
        screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.resize(width/2, height/2)
        self.move(width/4, height/4)
        self.setup_UI()
        self.setup_css()
        
    
    def setup_UI(self):
        self.layoutMain = QtWidgets.QHBoxLayout(self)
        
        self.layoutLeft= QtWidgets.QVBoxLayout(self)
        self.layoutRight = QtWidgets.QVBoxLayout(self)
        self.layoutMain.addLayout(self.layoutLeft)
        self.layoutMain.addLayout(self.layoutRight)
        
        btn1 = QtWidgets.QPushButton("Test1", self)
        btn2 = QtWidgets.QPushButton("Test2", self)
        btn3 = QtWidgets.QPushButton("Test3", self)
        
        self.layoutLeft.addWidget(btn1)
        self.layoutLeft.addWidget(btn2)
        self.layoutLeft.addWidget(btn3)
        
        btn4 = QtWidgets.QPushButton("Test4", self)
        btn5 = QtWidgets.QPushButton("Test5", self)
        btn6 = QtWidgets.QPushButton("Test6", self)
       
        self.layoutRight.addWidget(btn4)
        self.layoutRight.addWidget(btn5)
        self.layoutRight.addWidget(btn6)
        
    def setup_css(self):    
        self.setStyleSheet("""
        background-color: rgb(70, 70 ,70);
        color: rgb(255, 255, 255)          
        """)

def main():
    app = QtWidgets.QApplication(sys.argv)

    windows = App()
    windows.show()
    sys.exit(app.exec_())
    
main()


