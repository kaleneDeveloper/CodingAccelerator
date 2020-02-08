# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Test(object):
    def setupUi(self, Test):
        if Test.objectName():
            Test.setObjectName(u"Test")
        Test.resize(514, 150)
        Test.setMinimumSize(QSize(400, 150))
        Test.setMaximumSize(QSize(800, 158))
        self.gridLayout = QGridLayout(Test)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(Test)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(64, 32))
        self.lineEdit.setMaximumSize(QSize(600, 32))

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.Choose = QLabel(Test)
        self.Choose.setObjectName(u"Choose")
        self.Choose.setMinimumSize(QSize(64, 32))
        self.Choose.setMaximumSize(QSize(64, 32))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75);
        self.Choose.setFont(font)
        self.Choose.setTextFormat(Qt.AutoText)
        self.Choose.setScaledContents(False)
        self.Choose.setWordWrap(False)
        self.Choose.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.Choose, 1, 0, 1, 2)

        self.pushButton_2 = QPushButton(Test)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(64, 32))
        self.pushButton_2.setMaximumSize(QSize(64, 32))

        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)

        self.pushButton = QPushButton(Test)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(64, 32))
        self.pushButton.setMaximumSize(QSize(64, 32))

        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.label = QLabel(Test)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(64, 32))
        self.label.setMaximumSize(QSize(64, 32))

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(Test)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(64, 32))
        self.lineEdit_2.setMaximumSize(QSize(600, 32))

        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.label_2 = QLabel(Test)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(64, 32))
        self.label_2.setMaximumSize(QSize(64, 32))

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)


        self.retranslateUi(Test)

        QMetaObject.connectSlotsByName(Test)
    # setupUi

    def retranslateUi(self, Test):
        Test.setWindowTitle(QCoreApplication.translate("Test", u"Form", None))
        self.Choose.setText(QCoreApplication.translate("Test", u"Choose", None))
        self.pushButton_2.setText(QCoreApplication.translate("Test", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Test", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Test", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Test", u"TextLabel", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Test = QWidget()
    ui = Ui_Test()
    ui.setupUi(Test)
    Test.show()
    sys.exit(app.exec_())