from PySide2 import QtWidgets, QtGui, QtCore

class MonApplication(QtWidgets.QWidget):
	def __init__(self):
		super(MonApplication, self).__init__()

		# On cree un layout de type QGridLayout
		layout = QtWidgets.QGridLayout(self)

		# Exemple 1
		# btn_1 = QtGui.QPushButton('0.0')
		# btn_2 = QtGui.QPushButton('0.1')
		# btn_3 = QtGui.QPushButton('0.2')
		# btn_4 = QtGui.QPushButton('1.0')
		# btn_5 = QtGui.QPushButton('1.1')
		# btn_6 = QtGui.QPushButton('1.2')
		# btn_7 = QtGui.QPushButton('2.0')
		# btn_8 = QtGui.QPushButton('2.1')
		# btn_9 = QtGui.QPushButton('2.3')

		# layout.addWidget(btn_1, 0, 0)
		# layout.addWidget(btn_2, 0, 1)
		# layout.addWidget(btn_3, 0, 2)
		# layout.addWidget(btn_4, 1, 0)
		# layout.addWidget(btn_5, 1, 1)
		# layout.addWidget(btn_6, 1, 2)
		# layout.addWidget(btn_7, 2, 0)
		# layout.addWidget(btn_8, 2, 1)
		# layout.addWidget(btn_9, 2, 2)

		# Exemple 2
		btn_1 = QtWidgets.QPushButton('0.0-1x3')
		btn_2 = QtWidgets.QPushButton('1.0-1x1')
		btn_3 = QtWidgets.QPushButton('1.1-1x1')
		btn_4 = QtWidgets.QPushButton('1.2-1x1')

		# On ajoute les widgets au layout avec 'addWidget'
		layout.addWidget(btn_1, 0, 1, 1, 3)
		layout.addWidget(btn_2, 1, 0, 1, 1)
		layout.addWidget(btn_3, 1, 1, 1, 1)
		layout.addWidget(btn_4, 1, 2, 1, 1)

		self.resize(500, 500)


app = QtWidgets.QApplication([])
fenetre = MonApplication()
fenetre.show()
app.exec_()

