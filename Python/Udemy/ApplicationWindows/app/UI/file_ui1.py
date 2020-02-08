# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtWidgets, QtGui, QtCore


class App(object):
    def setupUi(self, Form):
        Form.setObjectName("Test 1")
        screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        Form.resize(width/2, height/2)
        Form.move(width/4, height/4)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 10, 500, 1000))
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
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Test"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "New Item1"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "New Item2"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "New Item3"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "New Item4"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    windows = App()
    windows.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
