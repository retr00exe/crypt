# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vigenere.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VigenereWindow(object):
    def setupUi(self, VigenereWindow):
        VigenereWindow.setObjectName("VigenereWindow")
        VigenereWindow.resize(420, 601)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        VigenereWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vigenere.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VigenereWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(VigenereWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelVignere = QtWidgets.QLabel(self.centralwidget)
        self.labelVignere.setGeometry(QtCore.QRect(20, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.labelVignere.setFont(font)
        self.labelVignere.setObjectName("labelVignere")
        self.labelKey = QtWidgets.QLabel(self.centralwidget)
        self.labelKey.setGeometry(QtCore.QRect(20, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelKey.setFont(font)
        self.labelKey.setObjectName("labelKey")
        self.lineEditKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditKey.setGeometry(QtCore.QRect(80, 70, 81, 22))
        self.lineEditKey.setObjectName("lineEditKey")
        self.labelPlainText = QtWidgets.QLabel(self.centralwidget)
        self.labelPlainText.setGeometry(QtCore.QRect(20, 130, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPlainText.setFont(font)
        self.labelPlainText.setObjectName("labelPlainText")
        self.labelCipherText = QtWidgets.QLabel(self.centralwidget)
        self.labelCipherText.setGeometry(QtCore.QRect(20, 320, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCipherText.setFont(font)
        self.labelCipherText.setObjectName("labelCipherText")
        self.textEditPlainText = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditPlainText.setGeometry(QtCore.QRect(20, 150, 371, 151))
        self.textEditPlainText.setObjectName("textEditPlainText")
        self.textEditCipherText = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditCipherText.setGeometry(QtCore.QRect(20, 340, 371, 151))
        self.textEditCipherText.setObjectName("textEditCipherText")
        self.pushButtonEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEncrypt.setGeometry(QtCore.QRect(20, 510, 93, 28))
        self.pushButtonEncrypt.setObjectName("pushButtonEncrypt")
        self.pushButtonEncrypt.clicked.connect(self.encrypt)
        self.pushButtonDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDecrypt.setGeometry(QtCore.QRect(130, 510, 93, 28))
        self.pushButtonDecrypt.setObjectName("pushButtonDecrypt")
        VigenereWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VigenereWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 26))
        self.menubar.setObjectName("menubar")
        VigenereWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VigenereWindow)
        self.statusbar.setObjectName("statusbar")
        VigenereWindow.setStatusBar(self.statusbar)
        self.retranslateUi(VigenereWindow)
        QtCore.QMetaObject.connectSlotsByName(VigenereWindow)

    def retranslateUi(self, VigenereWindow):
        _translate = QtCore.QCoreApplication.translate
        VigenereWindow.setWindowTitle(_translate("VigenereWindow", "Vigenère Cipher"))
        self.labelVignere.setText(_translate("VigenereWindow", "Vigenère Cipher"))
        self.labelKey.setText(_translate("VigenereWindow", "Key :"))
        self.labelPlainText.setText(_translate("VigenereWindow", "Input"))
        self.labelCipherText.setText(_translate("VigenereWindow", "Output"))
        self.pushButtonEncrypt.setText(_translate("VigenereWindow", "Encrypt"))
        self.pushButtonDecrypt.setText(_translate("VigenereWindow", "Decrypt"))

    def generateKey(self, string, key): 
            key = list(key) 
            if len(string) == len(key): 
                return(key) 
            else: 
                for i in range(len(string) - len(key)): 
                    key.append(key[i % len(key)]) 
            return("". join(key)) 
        
    def encrypt(self): 
        cipher_text = [] 
        string = self.textEditPlainText.toPlainText()
        inputKey = self.lineEditKey.text()
        key = self.generateKey(string,inputKey)
        print(string)
        print(key)
        for i in range(len(string)): 
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A') 
            cipher_text.append(chr(x)) 
        encrypted = "" . join(cipher_text)
        self.textEditCipherText.setText(encrypted)

    def decrypt(self, cipher_text, key): 
        orig_text = [] 
        for i in range(len(cipher_text)): 
            x = (ord(cipher_text[i]) - 
                ord(key[i]) + 26) % 26
            x += ord('A') 
            orig_text.append(chr(x)) 
        return("" . join(orig_text)) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VigenereWindow = QtWidgets.QMainWindow()
    ui = Ui_VigenereWindow()
    ui.setupUi(VigenereWindow)
    VigenereWindow.show()
    sys.exit(app.exec_())
