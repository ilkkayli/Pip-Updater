# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Nov 27 08:24:01 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(461, 444)
        self.updateButton = QtGui.QPushButton(Dialog)
        self.updateButton.setGeometry(QtCore.QRect(130, 110, 75, 23))
        self.updateButton.setObjectName("updateButton")
        self.quitButton = QtGui.QPushButton(Dialog)
        self.quitButton.setGeometry(QtCore.QRect(250, 110, 75, 23))
        self.quitButton.setObjectName("quitButton")
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(70, 60, 361, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(75, 190, 321, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.showDetailsButton = QtGui.QPushButton(Dialog)
        self.showDetailsButton.setGeometry(QtCore.QRect(70, 150, 75, 23))
        self.showDetailsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.showDetailsButton.setObjectName("showDetailsButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Pip Upgrade", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setText(QtGui.QApplication.translate("Dialog", "Update!", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("Dialog", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Ready to update", None, QtGui.QApplication.UnicodeUTF8))
        self.showDetailsButton.setText(QtGui.QApplication.translate("Dialog", "Details", None, QtGui.QApplication.UnicodeUTF8))

