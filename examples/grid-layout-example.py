#!/usr/bin/env python3
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

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QGroupBox,
    QDialog,
    QVBoxLayout,
    QGridLayout)

class App(QDialog):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle('PyQt6 Grid Layout')
        self.setGeometry(100, 100, 320, 100)
        self.CreateGridLayout()

        self.windowLayout = QVBoxLayout()
        self.windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.windowLayout)

        self.show()
        sys.exit(app.exec())

    def CreateGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        self.layout = QGridLayout()
        self.layout.setColumnStretch(2, 4)
        self.layout.setColumnStretch(1, 4)

        for label in "123456789":
            self.MakeButton(label)

        self.horizontalGroupBox.setLayout(self.layout)

    def MakeButton(self, label):
        button = QPushButton(label)
        button.clicked.connect(lambda: self.on_click(button))
        self.layout.addWidget(button)

    def on_click(self, pushButton):
        print('PyQt5 {0} button clicked.'.format(pushButton.text()))


if __name__ == '__main__':
    App()

