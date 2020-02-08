import sys
import os
from PySide2 import QtWidgets, QtGui, QtCore

class App(QtWidgets.QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.setWindowTitle("PyQT tuts!")
        screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.resize(width/2, height/2)
        self.move(width/4, height/4)
        self.setup_UI()

    def setup_UI(self):
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayout = QtWidgets.QGridLayout(self)
        
        self.btn_0 = QtWidgets.QPushButton("Quit")
        self.btn_0.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.btn_0.resize(200,200)
        self.gridLayout.addWidget(self.btn_0, 0, 0, 1, 1)

        self.btn_1 = QtWidgets.QPushButton("1")
        self.btn_1.resize(200,200)
        self.btn_1.clicked.connect(self.clicked)
        self.gridLayout.addWidget(self.btn_1, 1, 0, 1, 1)

        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setFixedSize(64, 64)
                widget.setFont(font)

    def clicked(self):
        print("Hello wolrd")   

        
def run():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    windows = App()
    windows.show()
    sys.exit(app.exec_())

run()
