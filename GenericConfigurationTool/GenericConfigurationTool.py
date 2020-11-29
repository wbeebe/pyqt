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
    QHBoxLayout,
    QVBoxLayout,
    QMainWindow,
    QApplication,
    QMessageBox,
    QPushButton,
    QWidget,
    QAction,
    QTabWidget,
    QVBoxLayout)

from PyQt5.QtGui import QIcon

from AboutUI import About
from WorkstationUI import Workstation
from ServicesUI import Services


class App(QMainWindow):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle('Generic Configuration Tool')
        self.setGeometry(100, 100, 640, 480)
        self.isEdited = False
        self.saveAndClose = SaveAndCloseActions(self)

        centralWidget = QWidget()
        vbox = QVBoxLayout()
        centralWidget.setLayout(vbox)
        vbox.addWidget(TabContainer(self))
        vbox.addStretch(1)
        vbox.addWidget(self.saveAndClose)
        self.setCentralWidget(centralWidget)
        self.show()
        sys.exit(app.exec_())

    def closeEvent(self, event):
        if self.isEdited:
            # pop up dialog to alert user of unsaved edits.
            # offer then a chance to save before exiting.
            #
            messageBox = QMessageBox(self)
            messageBox.setIcon(QMessageBox.Question)
            messageBox.setWindowTitle("Close Check")
            messageBox.setText("You Have Unsaved Edits")
            messageBox.setInformativeText("You have made edits that have not been saved.\nReally close and not save?")
            messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            #
            # change the default Yes and No buttons to really say
            # what then mean: Yes = Save and No = Quit.
            # the button actions then match exactly what the dialog
            # is saying and there should be no disonnance.
            #
            buttonSave = messageBox.button(QMessageBox.Yes)
            buttonSave.setText("Save")
            buttonQuit = messageBox.button(QMessageBox.No)
            buttonQuit.setText("Close")
            messageBox.setDefaultButton(QMessageBox.Yes)
            buttonReply = messageBox.exec_()

            if buttonReply == QMessageBox.Yes:
                print("QMessageBox.Save")
                event.accept()
            else:
                print("QMessageBox.Close")
        else:
            print("Close event")
            event.accept()

    def setEdited(self):
        self.isEdited = True
        self.saveAndClose.enableSave()


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
        # self.setStyleSheet("QTabWidget::pane { border: 0; }")
        parent.statusBar().showMessage(
            "Application started {0}".format(
                datetime.datetime.now()))

        # Create tabs to be placed in tab container
        #
        self.tab1 = Workstation(self, self.parent)
        self.tab2 = Services(self, self.parent)
        self.tab3 = About(self)

        # Add individual tabs into container.
        #
        self.addTab(self.tab1, self.tab1.tabName())
        self.addTab(self.tab2, self.tab2.tabName())
        self.addTab(self.tab3, self.tab3.tabName())

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
            "Tab close request on tab {0}".format(self.currentIndex() + 1))
        if self.count() > 1:
            self.removeTab(self.currentIndex())


class SaveAndCloseActions(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.saveButton = QPushButton("Save")
        self.saveButton.setEnabled(False)
        closeButton = QPushButton("Close")
        closeButton.clicked.connect(self.closeOnClick)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.saveButton)
        hbox.addWidget(closeButton)
        self.setLayout(hbox)

    def closeOnClick(self):
        self.parent.close()

    def enableSave(self):
        self.saveButton.setEnabled(True)

    def disableSave(self):
        self.saveButton.setEnabled(False)


if __name__ == '__main__':
    App()
