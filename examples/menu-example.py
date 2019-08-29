#!/usr/bin/env python3
#
#  Copyright (c) 2019 William H. Beebe, Jr.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import sys

from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QApplication,
    QWidget,
    QPushButton,
    QAction)

from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle('PyQt5 Menu Example')
        self.setGeometry(100, 100, 640, 480)
        self.statusBar().showMessage('Message in statusbar.')

        # We want references to the individual menus so that
        # menu entries can be added to the top level menu entries.
        #
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        editMenu = mainMenu.addMenu('&Edit')
        viewMenu = mainMenu.addMenu('&View')
        searchMenu = mainMenu.addMenu('&Search')
        toolsMenu = mainMenu.addMenu('&Tools')
        self.MakeHelpMenu(mainMenu)

        # I have a bug here: The icon (QIcon) will not display.
        # I broke up the instatiation to debug this, but nothing
        # works. I'm using Raspbian Buster's 24x24 exit PNG file.
        #
        exitButton = QAction(self)
        exitButton.setText('E&xit')
        exitButton.setIcon(QIcon('exit.png'))
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        # Make a toolbar. I'm using the same PNG for an icon
        # I tried to use on the Exit menu selection. It is
        # displayed here, but not there. *sigh*
        #
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Alt+X')
        exitAction.triggered.connect(self.close)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.show()
        sys.exit(app.exec_())

    def MakeHelpMenu(self, mainMenu):
        helpMenu = mainMenu.addMenu('&Help')

        aboutAction=QAction(QIcon(), 'About', self)
        aboutAction.setStatusTip('About this application')
        aboutAction.triggered.connect(self.About)
        helpMenu.addAction(aboutAction)

        aboutQtAction=QAction(QIcon(), 'About Qt', self)
        aboutQtAction.setStatusTip('About Qt and Qt Licensing')
        aboutQtAction.triggered.connect(self.AboutQt)
        helpMenu.addAction(aboutQtAction)

    def About(self):
        QMessageBox.information(self, 'About', 'Menu Example 0.0')

    def AboutQt(self):
        QMessageBox.aboutQt(self, 'About PyQt')

if __name__ == '__main__':
    App()

