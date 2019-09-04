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
import datetime

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
        self.setGeometry(100, 100, 640, 480)
        self.setCentralWidget(TabContainer(self))
        self.show()
        sys.exit(app.exec_())

class TabContainer(QTabWidget):
    def __init__(self, parent):
        super(QTabWidget, self).__init__(parent)
        self.parent = parent

        # Enable the ability to move individual tabs and reorganize them.
        # Disable the ability to close them.
        # Setting tabs as closable displays a close button on each tab.
        #
        self.setMovable(True)
        self.setTabsClosable(False)
        parent.statusBar().showMessage(
            "Application started {0}".format(
                datetime.datetime.now()))

        # Create tabs to be placed in tab container
        #
        self.tab1 = About(self)
        self.tab2 = Workstation(self)

        # Add individual tabs into container.
        #
        self.addTab(self.tab1,self.tab1.tabName())
        self.addTab(self.tab2,self.tab2.tabName())

        # Connect actions through tab container.
        # You can select a tab, so that is active.
        # Tab closure is disabled, but the hook and code are
        # left here for possible future capabilities.
        #
        self.currentChanged.connect(self.tabSelected)
        self.tabCloseRequested.connect(self.tabClose)

    def tabSelected(self):
        self.parent.statusBar().showMessage(
            "Selected tab {}".format(self.tabText(self.currentIndex())))

    def tabClose(self):
        parent.statusBar().showMessage(
            "Tab close request on tab {0}".format(self.currentIndex()+1))
        if self.count() > 1:
            self.removeTab(self.currentIndex())

if __name__ == '__main__':
    App()

