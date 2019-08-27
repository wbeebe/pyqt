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

from math import log10

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QFrame,
    QTextEdit,
    QMessageBox,
    QColorDialog,
    QFileDialog,
    QHBoxLayout,
    QAction)

from PyQt5.QtGui import (
    QIcon,
    QFont,
    QPixmap,
    QPalette,
    QColor,
    QPainter)

from PyQt5.QtCore import QSettings
#
# A beginning primative QTextEdit with line numbers
#
class LineNumberedTextEdit(QFrame):
    #
    # Inner class to LineNumberTextEdit
    # Defines the functionality responsible for numbering to the left of the
    # text edit area for each line of text.
    #
    class NumberBar(QWidget):

        def __init__(self, *args):
            QWidget.__init__(self, *args)
            self.edit = None

            # This is used to update the width of the control.
            # It is the highest line that is currently visibile.
            #
            self.highest_line = 0

        def setTextEdit(self, edit):
            self.edit = edit

        def update(self, *args):

            # Updates the number bar to display the current set of numbers.
            # Also, adjusts the width of the number bar if necessary.
            #
            # The + 5 is used to compensate for the current line being bold.
            #
            width = int(log10(self.edit.document().blockCount()) + 1) * self.fontMetrics().width(str("0")) + 5
            if self.width() != width:
                self.setFixedWidth(width)
            QWidget.update(self, *args)

        def paintEvent(self, event):
            contents_y = self.edit.verticalScrollBar().value()
            page_bottom = contents_y + self.edit.viewport().height()
            font_metrics = self.fontMetrics()
            current_block = self.edit.document().findBlock(self.edit.textCursor().position())

            painter = QPainter(self)

            line_count = 0
            
            # Iterate over all text blocks in the document.
            #
            block = self.edit.document().begin()
            while block.isValid():
                line_count += 1

                # The top left position of the block in the document.
                #
                position = self.edit.document().documentLayout().blockBoundingRect(block).topLeft()

                # Check if the position of the block is out side of the visible
                # area.
                #
                if position.y() > page_bottom:
                    break

                # We want the line number for the selected line to be bold.
                #
                bold = False
                if block == current_block:
                    bold = True
                    font = painter.font()
                    font.setBold(True)
                    painter.setFont(font)

                # Draw the line number right justified at the y position of the
                # line. 3 is a magic padding number. drawText(x, y, text).
                #
                painter.drawText(self.width() - font_metrics.width(str(line_count)) - 3,
                    round(position.y()) - contents_y + font_metrics.ascent(), str(line_count))

                # Remove the bold style if it was set previously.
                #
                if bold:
                    font = painter.font()
                    font.setBold(False)
                    painter.setFont(font)

                block = block.next()

            self.highest_line = line_count
            painter.end()

            QWidget.paintEvent(self, event)
        #
        # End inner class
        #

    def __init__(self, *args):
        QFrame.__init__(self, *args)

        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        self.edit = QTextEdit()
        self.edit.setFrameStyle(QFrame.NoFrame)
        self.edit.setAcceptRichText(False)
        self.edit.setLineWrapMode(QTextEdit.NoWrap)

        self.number_bar = self.NumberBar()
        self.number_bar.setTextEdit(self.edit)

        hbox = QHBoxLayout(self)
        hbox.setSpacing(0)
        hbox.setContentsMargins(10,0,0,0)
        hbox.addWidget(self.number_bar)
        hbox.addWidget(self.edit)

        self.edit.installEventFilter(self)
        self.edit.viewport().installEventFilter(self)

    def eventFilter(self, object, event):

        # Update the line numbers for all events on the text edit and the viewport.
        # This is easier than connecting all necessary singals.
        #
        if object in (self.edit, self.edit.viewport()):
            self.number_bar.update()
            return False
        return QFrame.eventFilter(object, event)

    def getTextEdit(self):
        return self.edit
#
#
#
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        #print(self.scriptDir)

        self.setWindowTitle('PyQt5 Basic Editor')
        self.setGeometry(100, 100, 800, 640)
        self.makeMenu()
        self.addMainApp()
        self.show()
        self.statusBar().showMessage('Initialized.')

    def addMainApp(self):
        self.lineNumberedTextEdit = LineNumberedTextEdit()
        self.textEdit = self.lineNumberedTextEdit.getTextEdit()
        font = QFont()
        font.setStyleHint(QFont().Monospace)
        font.setFamily('monospace')
        self.textEdit.setFont(font)
        self.setCentralWidget(self.lineNumberedTextEdit)

    def makeMenu(self):
        self.makeFileMenu(self.menuBar())
        self.makeEditMenu(self.menuBar())
        self.makeSearchMenu(self.menuBar())
        self.makeToolsMenu(self.menuBar())
        self.makeHelpMenu(self.menuBar())

    def makeFileMenu(self, mainMenu):
        fileMenu = mainMenu.addMenu('&File')

        newAction = QAction(QIcon(), 'New', self)
        newAction.setStatusTip('New clear edit area')
        newAction.triggered.connect(self.newFile)
        fileMenu.addAction(newAction)

        openAction = QAction(QIcon(), 'Open', self)
        openAction.setStatusTip('Open file')
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        saveAction = QAction(QIcon(), 'Save', self)
        fileMenu.addAction(saveAction)

        saveAsAction = QAction(QIcon(), 'Save as', self)
        fileMenu.addAction(saveAsAction)
        
        fileMenu.addSeparator()

        exitAction = QAction(QIcon("application-exit.png"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        
    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle('PyQt5 Basic Editor')

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()",
            "", "Python Files (*.py);;All Files (*)", options=options)
        if fileName:
            self.setWindowTitle(fileName.split("/")[-1])
            with open(fileName) as inputFile:
                self.fileData = inputFile.read()

            self.textEdit.clear()
            self.textEdit.setPlainText(self.fileData)
    #
    #
    #

    def makeEditMenu(self, mainMenu):
        editMenu = mainMenu.addMenu('&Edit')

    def makeSearchMenu(self, mainMenu):
        searchMenu = mainMenu.addMenu('&Search')

    def makeToolsMenu(self, mainMenu):
        toolsMenu = mainMenu.addMenu('&Tools')

        bwColorAction=QAction(QIcon(), 'Background Color', self)
        bwColorAction.setStatusTip('Select background color')
        bwColorAction.triggered.connect(self.colorPicker)
        toolsMenu.addAction(bwColorAction)

    def colorPicker(self):
        color = QColorDialog.getColor()
        print(color.name())
        palette = self.textEdit.palette();
        palette.setColor(QPalette.Base, QColor(color))
        self.textEdit.setPalette(palette)

    def makeHelpMenu(self, mainMenu):
        helpMenu = mainMenu.addMenu('&Help')

        aboutAction=QAction(QIcon(), 'About', self)
        aboutAction.setStatusTip('About this application')
        aboutAction.triggered.connect(self.about)
        helpMenu.addAction(aboutAction)

        aboutQtAction=QAction(QIcon(), 'About Qt', self)
        aboutQtAction.setStatusTip('About Qt and Qt Licensing')
        aboutQtAction.triggered.connect(self.aboutQt)
        helpMenu.addAction(aboutQtAction)

    def about(self):
        QMessageBox.information(self, 'About', 'Basic Editor 0.2')

    def aboutQt(self):
        QMessageBox.aboutQt(self, 'About PyQt')
    
def saveSettings():
    print("Exiting")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(saveSettings)
    ex = App()
    print('PID',os.getpid())
    sys.exit(app.exec_())

