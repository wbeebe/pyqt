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

from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.QtCore import Qt, PYQT_VERSION_STR

from PyQt5.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QWidget)

class About(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        hlayout = QHBoxLayout()
        self.layout = QGridLayout()
        hlayout.addLayout(self.layout)
        hlayout.setAlignment(Qt.AlignTop)
        self.setLayout(hlayout)
        self.row = 0

        self.__addLine__(
            "Python Version:",
            "{}.{}.{} {}".format(
                sys.version_info.major,
                sys.version_info.minor,
                sys.version_info.micro,
                sys.version_info.releaselevel))

        self.__addLine__("Qt Version:", PYQT_VERSION_STR)

        self.__addLine__("Platform:", sys.platform)

        self.__addLine__(
            "Total Physical Memory:",
            "{:.1f} GiB".format(psutil.virtual_memory().total / (1024 ** 3)))

        self.__addLine__(
            "Root Disk Space as Total/Used/Free:",
            "{:.1f} GiB/{:.1f} GiB/{:.1f} GiB".format(
                psutil.disk_usage('/').total / (1024 ** 3),
                psutil.disk_usage('/').used / (1024 ** 3),
                psutil.disk_usage('/').free / (1024 ** 3)))

        self.__addLine__(
            "Swap Space as Total/Used/Free:",
            "{:.1f} GiB/{:.1f} GiB/{:.1f} GiB".format(
                psutil.swap_memory().total / (1024 ** 3),
                psutil.swap_memory().used / (1024 ** 3),
                psutil.swap_memory().free / (1024 ** 3)))

        self.__addLine__(
            "CPU Temperature:",
            "{:.1f}\xb0 C".format(psutil.sensors_temperatures()['cpu-thermal'][0].current))

    def __addLine__(self, label, value):
        lbl = QLabel(label)
        lbl.setAlignment(Qt.AlignRight)
        self.layout.addWidget(lbl, self.row, 0)

        lbl = QLabel(value)
        lbl.setAlignment(Qt.AlignTop)
        self.layout.addWidget(lbl, self.row, 1)
        self.row += 1

    def tabName(self):
        return 'About'
