import sys
import yaml
import db
import os
import subprocess
import scrapy
import threading
import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    uic.loadUi('ui/ChartBase.ui', window)
    window.setWindowTitle('ChartBase')
    window.setFixedSize(800, 600)

    dlChorusBtn = window.findChild(QtWidgets.QPushButton, 'dlChorusBtn')
    dlChorusBtn.clicked.connect(scrapeFromChours)

    dlC3Btn = window.findChild(QtWidgets.QPushButton, 'dlC3Btn')
    dlC3Btn.clicked.connect(scrapeFromC3)

    # TODO import songs btn, choose dir

    # TODO organize songs btn

    chooseDirBtn = window.findChild(QtWidgets.QPushButton, 'chooseDirBtn')
    chooseDirBtn.clicked.connect(chooseDir)

    window.show()
    sys.exit(app.exec_())

    db.initDB()


def scrapeFromChours():
    pass


def scrapeFromC3():
    # Write spider
    pass


def organizeSongs():
    pass


def chooseDir():
    pass


if __name__ == '__main__':
    DL_DIR = None
    with open('config.yaml', 'r') as configFile:
        if yaml.load(configFile)['DL_DIR'] == None:
            print(f'{DL_DIR}')
    window()
