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

from datetime import datetime

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QPushButton)

class App(QMainWindow):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()

        self.setWindowTitle('PyQt6 simple button example')
        self.setGeometry(100, 100, 360, 140)

        button = QPushButton('PyQt6 Push Button', self)
        button.setToolTip('Click button to change window status message.')
        #
        # Not too sure about setting the fixed size of the button.
        # But I did that to keep the button from stretching across the width of
        # the window. Must be a way to have the button fit the size of it's text.
        #
        button.clicked.connect(self.on_click)
        button.setFixedSize(150,30)

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(button)
        self.setCentralWidget(widget)
        self.statusBar().showMessage('Operational')
        self.show()
        sys.exit(app.exec())

    def on_click(self):
        # timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.statusBar().showMessage(
            'PyQt6 button clicked at {0}'.format(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

if __name__ == '__main__':
    App()
