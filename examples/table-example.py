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
import sys, os

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout)

from PyQt5.QtGui import QColor

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Table Example')
        self.setGeometry(100, 100, 800, 600)
        #
        # Create a table, create a box layout, add the table to box layout and
        # then set the overall widget layout to the box layout.
        #
        self.createTable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.show()

    # Create a table with alphabet header labels. We're attempting to mimic
    # the classic spreadsheet look. This goes back to VisiCalc on the Apple ][
    # introduced in 1979.
    #
    def createTable(self):
        #
        # Define the max number of rows and the colomns. Lable the columns
        # with letters of the alphabet like spreadsheets since VisiCalc.
        #
        self.maxRows = 99
        self.headerLabels = ["A","B","C","D","E","F","G","H","I","J","K","L",
            "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.maxRows)
        self.tableWidget.setColumnCount(len(self.headerLabels))
        self.tableWidget.setHorizontalHeaderLabels(self.headerLabels)

        # Pre-populate the cells in the spreadsheets with data, strings in
        # this example.
        #
        for row in range(0, self.maxRows):
            for col in range(0, len(self.headerLabels)):
                self.tableWidget.setItem( row, col,
                    QTableWidgetItem("Cell {0}{1}".format(self.headerLabels[col], row+1)))
                #
                # Set every other row a light green color to help readability.
                #
                if row % 2 != 0:
                    self.tableWidget.item(row,col).setBackground(QColor(220,255,220))

        self.tableWidget.move(0,0)
        #
        # The next two function calls 'tighten up' the space around the text
        # items inserted into each cell.
        #
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        # Hook various events to their respective callbacks.
        #
        self.tableWidget.cellClicked.connect(self.cellClicked)
        self.tableWidget.cellChanged.connect(self.cellChanged)
        self.tableWidget.cellActivated.connect(self.cellActivated)
        self.tableWidget.cellEntered.connect(self.cellEntered)
        self.tableWidget.cellPressed.connect(self.cellPressed)

    # Various actions executed when the user clicks in a cell.
    #
    def cellClicked(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(' Clicked:', currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())

    def cellChanged(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(' Changed:', currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())

    def cellActivated(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(' Activated:', currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())

    def cellEntered(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(' Entered:', currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())

    def cellPressed(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print('Pressed:', currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    print('PID',os.getpid())
    sys.exit(app.exec_())

