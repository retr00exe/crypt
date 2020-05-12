from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, qApp
from encrypt import *
from decrypt import *

class UI_MainWindow(object):
    listJenis = ["Base64","Base32","Base16","Ascii85","ASCII","Reverse","ROT13","MD5","SHA-1","SHA-224","SHA-256","SHA-384","SHA-512"]
    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBoxPilihJenis = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxPilihJenis.setGeometry(QtCore.QRect(30, 35, 240, 30))
        self.comboBoxPilihJenis.setObjectName("comboBoxPilihJenis")
        for jenis in self.listJenis:
            self.comboBoxPilihJenis.addItem(jenis)
        inputComboBox = self.comboBoxPilihJenis.currentText()
        self.comboBoxPilihJenis.currentIndexChanged.connect(self.disableHash)
        
#=======================================================================================================================================================#
#LABEL
        self.labelPilihAlgoritma = QtWidgets.QLabel(self.centralwidget)
        self.labelPilihAlgoritma.setGeometry(QtCore.QRect(30, 5, 230, 30))
        self.labelPilihAlgoritma.setObjectName("labelPilihAlgoritma")
        
        self.labelPlainText1 = QtWidgets.QLabel(self.centralwidget)
        self.labelPlainText1.setGeometry(QtCore.QRect(30, 80, 55, 20))
        self.labelPlainText1.setObjectName("labelPlainText1")
        
        self.labelPlainText2 = QtWidgets.QLabel(self.centralwidget)
        self.labelPlainText2.setGeometry(QtCore.QRect(530, 290, 55, 20))
        self.labelPlainText2.setObjectName("labelPlainText2")

        self.labelEncryptedText1 = QtWidgets.QLabel(self.centralwidget)
        self.labelEncryptedText1.setGeometry(QtCore.QRect(30, 290, 230, 15))
        self.labelEncryptedText1.setObjectName("labelEncryptedText1")
        
        self.labelEncryptedText2 = QtWidgets.QLabel(self.centralwidget)
        self.labelEncryptedText2.setGeometry(QtCore.QRect(530, 80, 230, 15))
        self.labelEncryptedText2.setObjectName("labelEncryptedText2")
        
#=======================================================================================================================================================#
#ENCRYPT
        self.textEditPlainText1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditPlainText1.setGeometry(QtCore.QRect(30, 110, 390, 110))
        self.textEditPlainText1.setObjectName("textEditPlainText1")

        self.pushButtonEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEncrypt.setGeometry(QtCore.QRect(30, 230, 140, 30))
        self.pushButtonEncrypt.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonEncrypt.setObjectName("pushButtonEncrypt")
        self.pushButtonEncrypt.clicked.connect(self.encrypt)

        self.textEditEncryptedText1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditEncryptedText1.setGeometry(QtCore.QRect(30, 320, 390, 110))
        self.textEditEncryptedText1.setObjectName("textEditEncryptedText1")

#=======================================================================================================================================================#
#DECRYPT
        self.textEditEncryptedText2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditEncryptedText2.setGeometry(QtCore.QRect(530, 110, 390, 110))
        self.textEditEncryptedText2.setObjectName("textEditEncryptedText2")

        self.pushButtonDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDecrypt.setGeometry(QtCore.QRect(530, 230, 140, 30))
        self.pushButtonDecrypt.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonDecrypt.setObjectName("pushButtonDecrypt")
        self.pushButtonDecrypt.clicked.connect(self.decrypt)

        self.textEditPlainText2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditPlainText2.setGeometry(QtCore.QRect(530, 320, 390, 110))
        self.textEditPlainText2.setObjectName("textEditPlainText2")

#=======================================================================================================================================================#
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setShortcut("Ctrl+N")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.triggered.connect(qApp.quit)

        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionQuit)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enkripsi dan Dekripsi Kriptografi"))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.jpg'))
        counter=len(self.listJenis)
        for jenis in self.listJenis:
            self.comboBoxPilihJenis.setItemText(counter, _translate("MainWindow",jenis))
        self.labelPilihAlgoritma.setText(_translate("MainWindow", "Pilih Algoritma"))
        self.labelPlainText1.setText(_translate("MainWindow", "Plain Text"))
        self.labelPlainText2.setText(_translate("MainWindow", "Plain Text"))
        self.labelEncryptedText1.setText(_translate("MainWindow", "Ciphertext"))
        self.labelEncryptedText2.setText(_translate("MainWindow", "Ciphertext"))
        self.pushButtonEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.pushButtonDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    def encrypt(self):
        textboxValue = self.textEditPlainText1.toPlainText()
        inputComboBox = self.comboBoxPilihJenis.currentText()
        solve = encrypt()
        solve.setValue(inputComboBox,textboxValue)
        self.textEditEncryptedText1.setText(solve.getValue())

    def decrypt(self):
        textboxValue = self.textEditEncryptedText2.toPlainText()
        inputComboBox = self.comboBoxPilihJenis.currentText()
        solve = decrypt()
        solve.setValue(inputComboBox,textboxValue)
        self.textEditPlainText2.setText(solve.getValue())

    def disableHash(self):
        inputComboBox = self.comboBoxPilihJenis.currentText()
        hashList = ["MD5","SHA-1","SHA-224","SHA-256","SHA-384","SHA-512"]
        if(inputComboBox in hashList):
            self.textEditEncryptedText2.setDisabled(True)
            self.textEditPlainText2.setDisabled(True)
        else:
            self.textEditEncryptedText2.setDisabled(False)
            self.textEditPlainText2.setDisabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindow()
    ui.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())