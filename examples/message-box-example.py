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
    QApplication,
    QWidget,
    QPushButton,
    QMessageBox,
    QHBoxLayout)

class App(QWidget):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()

        self.setWindowTitle('PyQt5 Message Box')
        self.setGeometry(100, 100, 320, 200)
        self.setLayout(QHBoxLayout())

        button = QPushButton('Open Message Box', self)
        button.setToolTip('This opens an example message box')
        self.layout().addWidget(button)
        button.clicked.connect(self.on_click)

        self.show()
        sys.exit(app.exec_())

    def on_click(self):
        buttonReply = QMessageBox.question(
            self,
            'PyQt5',
            'Do you like PyQt5?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')

if __name__ == '__main__':
    App()
