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

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        editMenu = mainMenu.addMenu('&Edit')
        viewMenu = mainMenu.addMenu('&View')
        searchMenu = mainMenu.addMenu('&Search')
        toolsMenu = mainMenu.addMenu('&Tools')
        helpMenu = mainMenu.addMenu('&Help')

        #
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

        self.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    App()

