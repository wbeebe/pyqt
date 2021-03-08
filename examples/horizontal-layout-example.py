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
    QPushButton,
    QHBoxLayout,
    QGroupBox,
    QDialog,
    QVBoxLayout)

class App(QDialog):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle('PyQt6 Horizontal Layout')
        self.setGeometry(100, 100, 400, 100)
        self.CreateHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()
        sys.exit(app.exec())

    def CreateHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("What is your favorite color?")
        layout = QHBoxLayout()

        buttonBlue = QPushButton('Blue', self)
        buttonBlue.clicked.connect(lambda: self.on_click(buttonBlue))
        layout.addWidget(buttonBlue)

        buttonRed = QPushButton('Red', self)
        buttonRed.clicked.connect(lambda: self.on_click(buttonRed))
        layout.addWidget(buttonRed)

        buttonGreen = QPushButton('Green', self)
        buttonGreen.clicked.connect(lambda: self.on_click(buttonGreen))
        layout.addWidget(buttonGreen)

        self.horizontalGroupBox.setLayout(layout)

    def on_click(self, pushButton):
        print('PyQt6 {0} button clicked.'.format(pushButton.text()))

if __name__ == '__main__':
    App()

