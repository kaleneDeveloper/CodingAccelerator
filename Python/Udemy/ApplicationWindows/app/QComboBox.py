from PySide2 import QtCore, QtGui, QtWidgets

class App(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Mon Application')
		screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
		width, height = screen_resolution.width(), screen_resolution.height()
		self.resize(width/2, height/2)
		self.move(width/4, height/4)
		self.setup_UI()
	
	def setup_UI(self):
		layout = QtWidgets.QGridLayout(self)
		
		chk_box1 = QtWidgets.QCheckBox('Ceci est une checkbox1')
		chk_box1.setCheckState(QtCore.Qt.Checked)
		layout.addWidget(chk_box1, 0, 0, 1, 1)
		
		cbb_box2 = QtWidgets.QComboBox()
		cbb_box2.addItem("Item numero 1")
		cbb_box2.addItem("Item numero 2")
		cbb_box2.addItem("Item numero 3")
		cbb_box2.setMinimumSize(QtCore.QSize(64, 32))
		layout.addWidget(cbb_box2, 1, 0, 1, 1)

		cbb_box1 = QtWidgets.QComboBox()
		cbb_box1.addItem("Item numero 1")
		cbb_box1.addItem("Item numero 2")
		cbb_box1.addItem("Item numero 3")
		cbb_box1.setMinimumSize(QtCore.QSize(64, 32))
		layout.addWidget(cbb_box1, 2, 0, 1, 1)


if __name__ == "__main__":
	import sys
	import os
	os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
	app = QtWidgets.QApplication(sys.argv)
	app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	win = App()
	win.show()
	sys.exit(app.exec_())