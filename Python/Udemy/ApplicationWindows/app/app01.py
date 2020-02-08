from PySide2 import QtCore, QtGui, QtWidgets
import sys

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application 01")
        screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.resize(width/4, height/4)
        self.move(width/4, height/4)
        self.setup_UI()
        self.setup_css()       
    
    def setup_UI(self):
        # self.layout = QtWidgets.QHBoxLayout(self)
        self.layout = QtWidgets.QGridLayout(self)
        
        self.label_choose = QtWidgets.QLabel()
        self.label_choose.setMinimumSize(QtCore.QSize(64, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_choose.setFont(font)
        self.label_choose.setTextFormat(QtCore.Qt.AutoText)
        self.label_choose.setScaledContents(False)
        self.label_choose.setWordWrap(False)
        self.label_choose.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_choose.setObjectName("Choose")
        self.label_choose.setText("Choose:")
        self.layout.addWidget(self.label_choose, 0, 0, 1, 1)
        
        self.label_Hello1 = QtWidgets.QLabel("Hello1")
        self.label_Hello2 = QtWidgets.QLabel("Hello2")
        self.btn_Test4 = QtWidgets.QPushButton("Test4")
        self.btn_Test5 = QtWidgets.QPushButton("Test5")
        
        # self.label1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        # self.label2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self.label3.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.btn_Test4.setMinimumSize(QtCore.QSize(128, 64))
        self.btn_Test5.setMinimumSize(QtCore.QSize(128, 64))
        self.label_Hello2.setMinimumSize(QtCore.QSize(128, 64))
        self.label_Hello1.setMinimumSize(QtCore.QSize(128, 64))
        self.label_choose.setMinimumSize(QtCore.QSize(128, 64))

        self.lineEdit1 = QtWidgets.QLineEdit()
        self.lineEdit1.setPlaceholderText('Enter your text ...')
        self.lineEdit1.setMinimumSize(QtCore.QSize(128, 64))
        self.lineEdit2 = QtWidgets.QLineEdit()
        self.lineEdit2.setPlaceholderText('Enter your text ...')
        self.lineEdit2.setMinimumSize(QtCore.QSize(128, 64))
        
        # self.layout.addWidget(self.label, 3, 0)
       
        self.layout.addWidget(self.label_Hello1, 1, 0, 1, 1)
        self.layout.addWidget(self.btn_Test4, 1, 2, 1, 1)
        self.layout.addWidget(self.label_Hello2, 2, 0, 1, 1)
        self.layout.addWidget(self.btn_Test5, 2, 2, 1, 1)
        self.layout.addWidget(self.lineEdit1, 1, 1, 1, 1)
        self.layout.addWidget(self.lineEdit2, 2, 1, 1, 1)
        
    
    def setup_css(self):    
        self.setStyleSheet("""
        background-color: rgb(70, 70 ,70);
        color: rgb(255, 255, 255); 
               
        """)
        self.lineEdit1.setStyleSheet("color: rgb(240, 240, 240)")
        self.lineEdit2.setStyleSheet("color: rgb(240, 240, 240)")

def main():
    app = QtWidgets.QApplication(sys.argv)

    windows = App()
    windows.show()
    sys.exit(app.exec_())
    
main()




