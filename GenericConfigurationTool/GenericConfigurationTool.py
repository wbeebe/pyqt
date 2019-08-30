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
    QPushButton,
    QWidget,
    QAction,
    QTabWidget,
    QVBoxLayout)

from PyQt5.QtGui import QIcon

from AboutUI import About
from WorkstationUI import Workstation

class App(QMainWindow):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle('Generic Configuration Tool')
        self.setGeometry(100, 100, 640, 300)
        self.setCentralWidget(MyTabWidget(self))
        self.show()
        sys.exit(app.exec_())

class MyTabWidget(QTabWidget):
    def __init__(self, parent):
        super(QTabWidget, self).__init__(parent)
        self.parent = parent

        # Enable the ability to move tabs and reorganize them, as well
        # as close them. Setting tabs as closable displays a close button
        # on each tab.
        #
        self.setTabsClosable(False)
        self.setMovable(True)

        # Create tabs in tab container
        #
        self.tab1 = About(self)
        self.tab2 = Workstation(self)

        # Add tabs
        #
        self.addTab(self.tab1,self.tab1.tabName())
        self.addTab(self.tab2,self.tab2.tabName())

        self.currentChanged.connect(self.tabSelected)
        self.tabCloseRequested.connect(self.closeRequest)

    def tabSelected(self):
        self.parent.statusBar().showMessage("Selected tab {0}".format(self.currentIndex()+1))

    def closeRequest(self):
        parent.statusBar().showMessage("Tab close request on tab {0}".format(self.currentIndex()+1))
        if self.count() > 1:
            self.removeTab(self.currentIndex())

if __name__ == '__main__':
    App()

