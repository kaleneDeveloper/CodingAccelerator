from PySide2 import QtCore, QtGui, QtWidgets

class FenetrePrincipale(QtWidgets.QWidget):
	def __init__(self):
		super(FenetrePrincipale, self).__init__()

		layout = QtWidgets.QHBoxLayout(self)

		lw_demo = QtWidgets.QListWidget(self)
		lw_demo.addItem('Premier')
		lw_demo.addItems(['Deuxieme', 'Troisieme'])
		lw_demo.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

		layout.addWidget(lw_demo)


app = QtWidgets.QApplication([])
fenetre = FenetrePrincipale()
fenetre.show()
app.exec_()