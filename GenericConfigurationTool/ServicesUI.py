#
#  Copyright (c) 2021 William H. Beebe, Jr.
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

from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QMainWindow,
    QRadioButton,
    QLineEdit,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QWidget)

class Services(QWidget):
    def __init__(self, parent, top):
        super(QWidget, self).__init__(parent)
        self.top = top
        hlayout = QHBoxLayout()
        self.layout = QGridLayout()
        hlayout.addLayout(self.layout)
        hlayout.setAlignment(hlayout, Qt.Alignment.AlignTop)
        self.setLayout(hlayout)
        self.row = 0

        self.__addLabel__("Gateway Services")
        self.__addLabel__("Gateway Host Name/IP Address")
        self.gatewayHostName = QLineEdit(self)
        self.__addInput__(self.gatewayHostName)

        self.__addLabel__("Exercise Data Server Host Name/IP Address")
        self.productionEDS = QLineEdit(self)
        self.prodEnable = QRadioButton("Production")
        self.prodEnable.setChecked(True)
        self.prodEnable.toggled.connect(self.radioProdClicked)
        self.prodEnable.setStyleSheet("QRadioButton{ width: 100; }")
        self.__addInputAndRadio__(self.productionEDS, self.prodEnable)
        self.testEDS = QLineEdit(self)
        self.testEnable = QRadioButton("Test")
        self.testEnable.toggled.connect(self.radioTestClicked)
        self.testEnable.setStyleSheet("QRadioButton{ width: 100; }")
        self.__addInputAndRadio__(self.testEDS, self.testEnable)

        self.__addLabel__("Messaging Port")
        self.messagePort = QLineEdit("61616")
        self.__addInput__(self.messagePort)

    def radioProdClicked(self):
        if self.sender().isChecked():
            self.testEnable.setChecked(False)

    def radioTestClicked(self):
        if self.sender().isChecked():
            self.prodEnable.setChecked(False)
        
    def __addLabel__(self, label):
        lbl = QLabel(label)
        self.layout.addWidget(lbl, self.row, 0, 1, -1)
        self.row += 1

    def __addInput__(self, input):
        self.layout.addWidget(input, self.row, 0, 1, 4)
        self.row += 1

    def __addInputAndRadio__(self, input, radio):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(input)
        hbox.addWidget(radio)
        widget = QWidget(self)
        widget.setLayout(hbox)
        self.layout.addWidget(widget, self.row, 0, 1, -1)
        self.row += 1

    def tabName(self):
        return 'Services'
