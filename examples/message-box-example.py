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
    QMainWindow,
    QWidget,
    QPushButton,
    QMessageBox,
    QHBoxLayout)

class App(QMainWindow):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle('PyQt5 Message Box')
        self.setGeometry(100, 100, 320, 200)

        #
        # Create a button that when clicked will pop up our dialog.
        # Connect our function on_click so that it is called when
        # the button is clicked.
        #
        button = QPushButton('Click to Open Message Box', self)
        button.setToolTip('This opens an example message box')
        button.clicked.connect(self.on_click)
        #
        # Add the button to the center of our simple window.
        #
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(button)
        self.setCentralWidget(widget)

        self.show()
        sys.exit(app.exec_())

    #
    # This is our hook to pop up our simple dialog.
    # To show the effects of clicking either button, write
    # approprite text to the main window's status line at the bottom
    # of the main window.
    #
    def on_click(self):
        buttonReply = QMessageBox.question(
            self,
            'PyQt5',
            'Do you like PyQt5?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            self.statusBar().showMessage('You clicked Yes. That''s good.')
        else:
            self.statusBar().showMessage('You clicked No. Why are you here?')

if __name__ == '__main__':
    App()
