from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import sys
import yaml
import db
import os
import subprocess


def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    uic.loadUi('ui/ChartBase.ui', window)
    window.setWindowTitle('ChartBase')
    window.setFixedSize(800, 600)

    dlChorusBtn = window.findChild(QtWidgets.QPushButton, 'dlChorusBtn')
    dlChorusBtn.clicked.connect(downloadFromChours)

    dlMasterSheetBtn = window.findChild(
        QtWidgets.QPushButton, 'dlMasterSheetBtn')
    dlMasterSheetBtn.clicked.connect(downloadFromMasterSheet)

    dlC3Btn = window.findChild(QtWidgets.QPushButton, 'dlC3Btn')
    dlC3Btn.clicked.connect(downloadFromC3)

    unpackBtn = window.findChild(QtWidgets.QPushButton, 'unpackBtn')
    unpackBtn.clicked.connect(unpack)

    rmBadBtn = window.findChild(QtWidgets.QPushButton, 'rmBadBtn')
    rmBadBtn.clicked.connect(removeBad)

    convertMidBtn = window.findChild(QtWidgets.QPushButton, 'convertMidBtn')
    convertMidBtn.clicked.connect(convertMid)

    convertSongsBtn = window.findChild(
        QtWidgets.QPushButton, 'convertSongsBtn')
    convertSongsBtn.clicked.connect(convertSongs)

    chooseDirBtn = window.findChild(QtWidgets.QPushButton, 'chooseDirBtn')
    chooseDirBtn.clicked.connect(chooseDir)

    window.show()
    sys.exit(app.exec_())

    db.initDB()


def downloadFromChours():
    # TODO run twisted reactor for ScrapeHero spiders
    pass


def downloadFromMasterSheet():
    pass


def downloadFromC3():
    pass


def unpack():
    pass


def removeBad():
    pass


def downloadFromChours():
    pass


def convertMid():
    pass


def convertSongs():
    pass


def chooseDir():
    pass


if __name__ == '__main__':
    DL_DIR = None
    with open('config.yaml', 'r') as configFile:
        if yaml.load(configFile)['DL_DIR'] == None:
            print(f'{DL_DIR}')
    window()
