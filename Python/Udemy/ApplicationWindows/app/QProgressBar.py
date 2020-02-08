from PySide2 import QtWidgets, QtGui, QtCore

class App(QtWidgets.QWidget):
	def __init__(self):
		super(App, self).__init__()

		self.setWindowTitle('Mon Application')

		layout = QtWidgets.QGridLayout(self)

		prg_demo = QtWidgets.QProgressBar()
		prg_demo.setRange(0, 100)
		prg_demo.setTextVisible(True)
		layout.addWidget(prg_demo, 0, 0, 1, 1)
		for i in range(100):
			prg_demo.setValue(i)


def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = App()
    windows.show()
    sys.exit(app.exec_())
run()