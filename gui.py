from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    uic.loadUi('ChartBase.ui', window)
    window.setWindowTitle('ChartBase')
    window.setFixedSize(800, 600)

    dlChorusBtn = window.findChild(QtWidgets.QPushButton, 'dlChorusBtn')
    dlChorusBtn.clicked.connect(btnClicked)

    dlMasterSheetBtn = window.findChild(
        QtWidgets.QPushButton, 'dlMasterSheetBtn')
    dlMasterSheetBtn.clicked.connect(btnClicked)

    dlC3Btn = window.findChild(QtWidgets.QPushButton, 'dlC3Btn')
    dlC3Btn.clicked.connect(btnClicked)

    unpackBtn = window.findChild(QtWidgets.QPushButton, 'unpackBtn')
    unpackBtn.clicked.connect(btnClicked)

    rmBadBtn = window.findChild(QtWidgets.QPushButton, 'rmBadBtn')
    rmBadBtn.clicked.connect(btnClicked)

    convertMidBtn = window.findChild(QtWidgets.QPushButton, 'convertMidBtn')
    convertMidBtn.clicked.connect(btnClicked)

    convertSongsBtn = window.findChild(
        QtWidgets.QPushButton, 'convertSongsBtn')
    convertSongsBtn.clicked.connect(btnClicked)

    chooseDirBtn = window.findChild(QtWidgets.QPushButton, 'chooseDirBtn')
    chooseDirBtn.clicked.connect(btnClicked)

    window.show()
    sys.exit(app.exec_())


def btnClicked():
    print('button was clicked')


if __name__ == '__main__':
    window()
