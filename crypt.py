# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crypt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from encoding import *


class Ui_MainWindow(object):
    
    listJenis = ["Base64","Base32","Base16","Ascii85","ASCII","Reverse","ROT13","MD5","SHA-1","SHA-224","SHA-256","SHA-384","SHA-512"]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBoxPilihJenis = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxPilihJenis.setGeometry(QtCore.QRect(30, 30, 241, 31))
        self.comboBoxPilihJenis.setObjectName("comboBoxPilihJenis")
        for jenis in self.listJenis:
            self.comboBoxPilihJenis.addItem(jenis)
        inputComboBox = self.comboBoxPilihJenis.currentText()

#=======================================================================================================================================================#
        
        self.labelPlainText1 = QtWidgets.QLabel(self.centralwidget)
        self.labelPlainText1.setEnabled(True)
        self.labelPlainText1.setGeometry(QtCore.QRect(30, 80, 55, 20))
        self.labelPlainText1.setObjectName("labelPlainText1")
        
        self.labelPlainText2 = QtWidgets.QLabel(self.centralwidget)
        self.labelPlainText2.setEnabled(True)
        self.labelPlainText2.setGeometry(QtCore.QRect(530, 290, 55, 20))
        self.labelPlainText2.setObjectName("labelPlainText2")

        self.labelEncryptedText1 = QtWidgets.QLabel(self.centralwidget)
        self.labelEncryptedText1.setGeometry(QtCore.QRect(30, 290, 231, 16))
        self.labelEncryptedText1.setObjectName("labelEncryptedText1")
        
        self.labelEncryptedText2 = QtWidgets.QLabel(self.centralwidget)
        self.labelEncryptedText2.setGeometry(QtCore.QRect(530, 80, 231, 16))
        self.labelEncryptedText2.setObjectName("labelEncryptedText2")
        
#=======================================================================================================================================================#
#ENCRYPT
        self.textEditPlainText1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditPlainText1.setGeometry(QtCore.QRect(30, 110, 391, 111))
        self.textEditPlainText1.setObjectName("textEditPlainText1")

        self.pushButtonEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEncrypt.setGeometry(QtCore.QRect(30, 230, 141, 28))
        self.pushButtonEncrypt.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonEncrypt.setObjectName("pushButtonEncrypt")
        
        self.pushButtonEncrypt.clicked.connect(self.solver)

    

        self.textEditEncryptedText1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditEncryptedText1.setGeometry(QtCore.QRect(30, 320, 391, 111))
        self.textEditEncryptedText1.setObjectName("textEditEncryptedText1")

#=======================================================================================================================================================#

        self.textEditEncryptedText2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditEncryptedText2.setGeometry(QtCore.QRect(530, 110, 391, 111))
        self.textEditEncryptedText2.setObjectName("textEditEncryptedText2")

        self.pushButtonDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDecrypt.setGeometry(QtCore.QRect(530, 230, 141, 28))
        self.pushButtonDecrypt.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonDecrypt.setObjectName("pushButtonDecrypt")

        self.textEditPlainText2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditPlainText2.setGeometry(QtCore.QRect(530, 320, 391, 111))
        self.textEditPlainText2.setObjectName("textEditPlainText2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1019, 26))
        self.menubar.setObjectName("menubar")
        self.menuEncrpyt = QtWidgets.QMenu(self.menubar)
        self.menuEncrpyt.setObjectName("menuEncrpyt")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBase64 = QtWidgets.QAction(MainWindow)
        self.actionBase64.setObjectName("actionBase64")
        self.actionCaesar_Cipher = QtWidgets.QAction(MainWindow)
        self.actionCaesar_Cipher.setObjectName("actionCaesar_Cipher")
        self.actionBase64_2 = QtWidgets.QAction(MainWindow)
        self.actionBase64_2.setObjectName("actionBase64_2")
        self.actionBase32 = QtWidgets.QAction(MainWindow)
        self.actionBase32.setObjectName("actionBase32")
        self.actionAscii85 = QtWidgets.QAction(MainWindow)
        self.actionAscii85.setObjectName("actionAscii85")
        self.actionROT13 = QtWidgets.QAction(MainWindow)
        self.actionROT13.setObjectName("actionROT13")
        self.actionMD5 = QtWidgets.QAction(MainWindow)
        self.actionMD5.setObjectName("actionMD5")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuEncrpyt.addAction(self.actionNew)
        self.menuEncrpyt.addAction(self.actionQuit)
        self.menubar.addAction(self.menuEncrpyt.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        counter=len(self.listJenis)
        for jenis in self.listJenis:
            self.comboBoxPilihJenis.setItemText(counter, _translate("MainWindow",jenis))
        self.labelPlainText1.setText(_translate("MainWindow", "Plain Text"))
        self.labelPlainText2.setText(_translate("MainWindow", "Plain Text"))
        self.labelEncryptedText1.setText(_translate("MainWindow", "Encrypted Text"))
        self.labelEncryptedText2.setText(_translate("MainWindow", "Encrypted Text"))
        self.pushButtonEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.pushButtonDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.menuEncrpyt.setTitle(_translate("MainWindow", "Menu"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    def solver(self):
        textboxValue = self.textEditPlainText1.toPlainText()
        inputComboBox = self.comboBoxPilihJenis.currentText()
        solve = solver(inputComboBox,textboxValue)
        hasil = solve.encrypt(inputComboBox,textboxValue)
        self.textEditEncryptedText1.setText(hasil)

    def encrypt(self):
        import base64, hashlib, codecs

        inputComboBox = self.comboBoxPilihJenis.currentText()
        if(inputComboBox=="Base64"):
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            base64_bytes = base64.b64encode(textUTF8)
            base64 = base64_bytes.decode("utf-8")
            self.textEditEncryptedText1.setText(base64)

        if(inputComboBox=="Base32"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            base32_bytes = base64.b32encode(textUTF8)
            base32 = base32_bytes.decode("utf-8")
            self.textEditEncryptedText1.setText(base32)

        if(inputComboBox=="Base16"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            base16_bytes = base64.b16encode(textUTF8)
            base16 = base16_bytes.decode("utf-8")
            self.textEditEncryptedText1.setText(base16)

        if(inputComboBox=="Ascii85"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            Ascii85_bytes = base64.b85encode(textUTF8)
            Ascii85 = Ascii85_bytes.decode("utf-8")
            self.textEditEncryptedText1.setText(Ascii85)

        if(inputComboBox=="ASCII"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            asciiText = ' '.join(str(ord(c))for c in textboxValue)
            self.textEditEncryptedText1.setText(asciiText)

        if(inputComboBox=="Reverse"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            reverse = textboxValue[::-1]
            self.textEditEncryptedText1.setText(reverse)

        if(inputComboBox=="ROT13"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            rot13 = codecs.encode(textboxValue, 'rot_13')
            self.textEditEncryptedText1.setText(rot13)

        if(inputComboBox=="MD5"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            hash = hashlib.md5(textUTF8)
            md5 = hash.hexdigest()
            self.textEditEncryptedText1.setText(md5)

        if(inputComboBox=="SHA-1"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            hash = hashlib.sha1(textUTF8)
            sha1 = hash.hexdigest()
            self.textEditEncryptedText1.setText(sha1)

        if(inputComboBox=="SHA-224"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            hash = hashlib.sha224(textUTF8)
            sha224 = hash.hexdigest()
            self.textEditEncryptedText1.setText(sha224)

        if(inputComboBox=="SHA-256"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            hash = hashlib.sha256(textUTF8)
            sha256 = hash.hexdigest()
            self.textEditEncryptedText1.setText(sha256)

        if(inputComboBox=="SHA-384"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            hash = hashlib.sha384(textUTF8)
            sha384 = hash.hexdigest()
            self.textEditEncryptedText1.setText(sha384)

        if(inputComboBox=="SHA-512"):
            self.textEditEncryptedText1.setText("")
            textboxValue = self.textEditPlainText1.toPlainText()
            textUTF8 = textboxValue.encode("utf-8")
            hash = hashlib.sha512(textUTF8)
            sha512 = hash.hexdigest()
            self.textEditEncryptedText1.setText(sha512)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
