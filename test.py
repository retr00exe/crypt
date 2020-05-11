# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 140, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 170, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(4, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(5, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(6, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(7, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(8, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(9, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(10, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(11, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(12, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(13, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(14, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(15, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(16, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(17, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(18, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(19, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(20, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(21, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(22, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(23, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(24, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(25, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(26, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(27, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(28, _translate("MainWindow", "New Item"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
