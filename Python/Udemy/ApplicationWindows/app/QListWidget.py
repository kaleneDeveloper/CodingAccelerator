from PySide2 import QtWidgets, QtGui, QtCore

class App(QtWidgets.QWidget):
	def __init__(self):
		super(App, self).__init__()
		self.setWindowTitle("PyQT tuts!")
		screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
		width, height = screen_resolution.width(), screen_resolution.height()
		self.resize(width/2, height/2)
		self.move(width/4, height/4)
		
		layout = QtWidgets.QHBoxLayout(self)
		self.listWidget = QtWidgets.QListWidget(self)
		layout.addWidget(self.listWidget)
		
  		# self.listWidget.setGeometry(QtCore.QRect(0, 0, 500, 1000))
		
		self.listWidget.setObjectName("listWidget")
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)
        
	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		# self.setWindowTitle(_translate("Form", "Test"))
		# __sortingEnabled = self.listWidget.isSortingEnabled()
		# self.listWidget.setSortingEnabled(False)
		item = self.listWidget.item(0)
		item.setText(_translate("Form", "New Item1"))
		item = self.listWidget.item(1)
		item.setText(_translate("Form", "New Item2"))
		item = self.listWidget.item(2)
		item.setText(_translate("Form", "New Item3"))
		item = self.listWidget.item(3)
		item.setText(_translate("Form", "New Item4"))
		# self.listWidget.setSortingEnabled(__sortingEnabled)
        
        
def run():
	import sys
	import os
	os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
	app = QtWidgets.QApplication(sys.argv)
	app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QtWidgets.QApplication(sys.argv)
	windows = App()
	windows.show()
	sys.exit(app.exec_())
run()
