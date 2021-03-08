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

# For Qt.AlignCenter use
#
from PyQt6.QtCore import *

from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QVBoxLayout)

def App():
    app = QApplication(sys.argv)
    win = QWidget()

    win.setWindowTitle("PyQt6 QLabel Example")
    win.left = 100
    win.top = 100

    l1 = QLabel("Hello World")
    l2 = QLabel("Welcome to Python GUI Programming")
    #
    # Because you can't instantiate a QLable directly with a QPixmap.
    #
    l3 = QLabel()
    l3.setPixmap(QPixmap("python-small.png"))

    l1.setAlignment(Qt.Alignment.AlignCenter)
    l2.setAlignment(Qt.Alignment.AlignCenter)
    l3.setAlignment(Qt.Alignment.AlignCenter)

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()

    win.setLayout(vbox)
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    App()
