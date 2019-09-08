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
import psutil

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QPushButton,
    QLineEdit,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QWidget)

class Workstation(QWidget):
    def __init__(self, parent, top):
        super(QWidget, self).__init__(parent)
        self.top = top
        hlayout = QHBoxLayout()
        self.layout = QGridLayout()
        hlayout.addLayout(self.layout)
        hlayout.setAlignment(Qt.AlignTop)
        self.setLayout(hlayout)
        self.row = 0

        self.__addLabel__("Federate Name")
        self.federateName = QLineEdit('REMOTE_WORKSTATION')
        self.__addInput__(self.federateName)

        self.__addLabel__("Message Directory Cache")
        self.messageDirectoryCache = QLineEdit(self)
        self.__addInputAndSelect__(self.messageDirectoryCache, self.top)

        self.__addLabel__("Map Data Cache")
        self.mapDataCache = QLineEdit(self)
        self.__addInputAndSelect__(self.mapDataCache, self.top)

        self.__addLabel__("Raster Map Cache")
        self.rasterMapCache = QLineEdit(self)
        self.__addInputAndSelect__(self.rasterMapCache, self.top)

        self.__addLabel__("Remote Control Location")
        self.remoteControlLocation = QLineEdit(self)
        self.__addInputAndSelect__(self.remoteControlLocation, self.top)

    def __addLabel__(self, label):
        lbl = QLabel(label)
        self.layout.addWidget(lbl, self.row, 0, 1, -1)
        self.row += 1

    def __addInput__(self, input):
        self.layout.addWidget(input, self.row, 0, 1, 4)
        self.row += 1

    def __addSelect__(self, input):
        self.layout.addWidget(BrowseButton(self, input), self.row-1, 4, 1, 1)

    def __addInputAndSelect__(self, input, top):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(input)
        browseButton = BrowseButton(self, input, top)
        browseButton.adjustSize()
        hbox.addWidget(browseButton)
        widget = QWidget(self)
        widget.setLayout(hbox)
        self.layout.addWidget(widget, self.row, 0, 1, -1)
        self.row += 1

    def tabName(self):
        return 'Workstation'

class BrowseButton(QPushButton, QLineEdit, QMainWindow):
    def __init__(self, parent, input, top):
        super(QPushButton, self).__init__(parent)
        self.input = input
        self.top = top
        self.setText('...')
        self.clicked.connect(self.on_click)

    def on_click(self):
        print('BrowseButton clicked {}'.format(self.input.text()))
        #self.input.setText('{} - Bar'.format(self.input.text()))
        folder = QFileDialog.getExistingDirectory(self,
            "Select Folder", "",QFileDialog.ShowDirsOnly)
        if folder:
            self.input.setText(folder)
            self.input.setStyleSheet("background-color:#ffff80")
            self.top.setEdited()
        self.input.setFocus()
