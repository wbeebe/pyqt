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
    QLineEdit,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QWidget)

class Workstation(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
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
        self.__addInput__(self.messageDirectoryCache)

        self.__addLabel__("Map Data Cache")
        self.mapDataCache = QLineEdit(self)
        self.__addInput__(self.mapDataCache)

        self.__addLabel__("Raster Map Cache")
        self.rasterMapCache = QLineEdit(self)
        self.__addInput__(self.rasterMapCache)

        self.__addLabel__("Remote Control Location")
        self.remoteControlLocation = QLineEdit(self)
        self.__addInput__(self.remoteControlLocation)

    def __addLabel__(self, label):
        lbl = QLabel(label)
        self.layout.addWidget(lbl, self.row, 0, 1, -1)
        self.row += 1

    def __addInput__(self, input):
        self.layout.addWidget(input, self.row, 0, 1, 4)
        self.row += 1

    def tabName(self):
        return 'Workstation'
