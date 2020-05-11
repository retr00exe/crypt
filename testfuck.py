import sys
from PyQt5 import QtWidgets


class ComboWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ComboWidget, self).__init__(parent)
        self.setGeometry(50, 50, 200, 200)

        layout = QtWidgets.QVBoxLayout(self)

        self.comboA = QtWidgets.QComboBox()
        # The second addItem parameter is itemData, which we will retrieve later
        self.comboA.addItem('A', ['1', '2', '3', '4'])
        self.comboA.addItem('B', ['a', 'b', 'c', 'd', 'e'])
        self.comboA.currentIndexChanged.connect(self.indexChanged)
        layout.addWidget(self.comboA)

        self.comboB = QtWidgets.QComboBox()
        # We could have added the 1,2,3,4 items directly, but the following
        # is a bit more generic in case the combobox starts with a different
        # index for some reason:
        self.indexChanged(self.comboA.currentIndex())
        layout.addWidget(self.comboB)

        self.show()

    def indexChanged(self, index):
        self.comboB.clear()
        data = self.comboA.itemData(index)
        if data is not None:
            self.comboB.addItems(data)


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = ComboWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()