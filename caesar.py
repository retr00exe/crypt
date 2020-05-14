from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_CaesarWindow(object):
    def setupUi(self, CaesarWindow):
        CaesarWindow.setObjectName("CaesarWindow")
        CaesarWindow.resize(420, 601)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        CaesarWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("caesar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CaesarWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CaesarWindow)
        self.centralwidget.setObjectName("centralwidget")
        #LABEL
        self.labelCaesar = QtWidgets.QLabel(self.centralwidget)
        self.labelCaesar.setGeometry(QtCore.QRect(20, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.labelCaesar.setFont(font)
        self.labelCaesar.setObjectName("labelCaesar")
        self.labelShift = QtWidgets.QLabel(self.centralwidget)
        self.labelShift.setGeometry(QtCore.QRect(20, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelShift.setFont(font)
        self.labelShift.setObjectName("labelShift")

        self.labelPlainText1 = QtWidgets.QLabel(self.centralwidget)
        self.labelPlainText1.setGeometry(QtCore.QRect(20, 130, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPlainText1.setFont(font)
        self.labelPlainText1.setObjectName("labelPlainText1")

        self.labelCipherText1 = QtWidgets.QLabel(self.centralwidget)
        self.labelCipherText1.setGeometry(QtCore.QRect(20, 320, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCipherText1.setFont(font)
        self.labelCipherText1.setObjectName("labelCipherText1")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(80, 70, 51, 25))
        self.spinBox.setObjectName("spinBox")

        self.textEditPlainText1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditPlainText1.setGeometry(QtCore.QRect(20, 150, 371, 151))
        self.textEditPlainText1.setObjectName("textEditPlainText1")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditPlainText1.setFont(font)

        self.textEditCipherText1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditCipherText1.setGeometry(QtCore.QRect(20, 340, 371, 151))
        self.textEditCipherText1.setObjectName("textEditCipherText1")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditCipherText1.setFont(font)

        self.pushButtonEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEncrypt.setGeometry(QtCore.QRect(20, 510, 93, 28))
        self.pushButtonEncrypt.setObjectName("pushButtonEncrypt")
        self.pushButtonEncrypt.clicked.connect(self.encrypt)

        self.pushButtonDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDecrypt.setGeometry(QtCore.QRect(130, 510, 93, 28))
        self.pushButtonDecrypt.setObjectName("pushButtonDecrypt")
        self.pushButtonDecrypt.clicked.connect(self.decrypt)

        CaesarWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CaesarWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 23))
        self.menubar.setObjectName("menubar")
        CaesarWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CaesarWindow)
        self.statusbar.setObjectName("statusbar")
        CaesarWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CaesarWindow)
        QtCore.QMetaObject.connectSlotsByName(CaesarWindow)

    def retranslateUi(self, CaesarWindow):
        _translate = QtCore.QCoreApplication.translate
        CaesarWindow.setWindowTitle(_translate("CaesarWindow", "Caesar Cipher"))
        self.labelCaesar.setText(_translate("CaesarWindow", "Caesar Cipher"))
        self.labelShift.setText(_translate("CaesarWindow", "Shift :"))
        self.labelPlainText1.setText(_translate("CaesarWindow", "Input"))
        self.labelCipherText1.setText(_translate("CaesarWindow", "Output"))
        self.pushButtonEncrypt.setText(_translate("CaesarWindow", "Encrypt"))
        self.pushButtonDecrypt.setText(_translate("CaesarWindow", "Decrypt"))
    
    def encrypt(self): 
        textboxValue = self.textEditPlainText1.toPlainText()
        shift = self.spinBox.value()
        encrypted = "" 
        for char in textboxValue:
            if char == ' ':
                encrypted = encrypted + char
            elif  char.isupper():
                encrypted = encrypted + chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted = encrypted + chr((ord(char) + shift - 97) % 26 + 97)
        self.textEditCipherText1.setText(encrypted)

    def decrypt(self):
        textboxValue = self.textEditPlainText1.toPlainText()
        shift = self.spinBox.value()
        decrypted = "" 
        for char in textboxValue:
            if char == ' ':
                decrypted = decrypted + char
            elif  char.isupper():
                decrypted = decrypted + chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted = decrypted + chr((ord(char) - shift - 97) % 26 + 97)
        self.textEditCipherText1.setText(decrypted)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaesarWindow = QtWidgets.QMainWindow()
    ui = Ui_CaesarWindow()
    ui.setupUi(CaesarWindow)
    CaesarWindow.show()
    sys.exit(app.exec_())
