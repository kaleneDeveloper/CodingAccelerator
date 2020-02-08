from PySide2 import QtCore, QtGui, QtWidgets

class App(QtWidgets.QWidget):
	def __init__(self):
		super(App, self).__init__()
		self.setWindowTitle('Mon Application')
		screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
		width, height = screen_resolution.width(), screen_resolution.height()
		self.resize(width/2, height/2)
		self.move(width/4, height/4)
		self.setup_UI()
		
	def setup_UI(self):
    	
		layout = QtWidgets.QGridLayout(self)
		font = QtGui.QFont()
		
		
		chk_box1 = QtWidgets.QCheckBox('Ceci est une checkbox1')
		font.setPointSize(10)
		chk_box1.setFont(font)
		chk_box1.setCheckState(QtCore.Qt.Checked)
		layout.addWidget(chk_box1, 0, 0, 1, 1)

		chk_box2 = QtWidgets.QCheckBox('Ceci est une checkbox2')
		font.setPointSize(10)
		chk_box2.setFont(font)
		chk_box2.setCheckState(QtCore.Qt.Checked)
		layout.addWidget(chk_box2, 1, 0, 1, 1)
		
		cbb_box1 = QtWidgets.QComboBox()
		font = QtGui.QFont()
		font.setPointSize(10)
		cbb_box1.setFont(font)
		cbb_box1.addItem("Item numero 1")
		cbb_box1.addItem("Item numero 2")
		cbb_box1.addItem("Item numero 3")
		layout.addWidget(cbb_box1, 2, 0, 1, 1)
		cbb_box1.setItemText(0, "Premier")
		cbb_box1.setItemText(cbb_box1.count() -1, "Dernier")


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win = App()
	win.show()
	sys.exit(app.exec_())