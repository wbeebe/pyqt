#!/usr/bin/env python3

"""
A beginning primative text editor with line numbers

  Copyright (c) 2021 William H. Beebe, Jr.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""
import sys
import os

from math import log10

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QFrame,
    QTextEdit,
    QMessageBox,
    QColorDialog,
    QFileDialog,
    QHBoxLayout)

from PyQt6.QtGui import (
    QAction,
    QIcon,
    QFont,
    QPalette,
    QColor,
    QPainter)

"""
A beginning primative QTextEdit with line numbers
"""
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

        def set_text_edit(self, edit):
            self.edit = edit

        def update(self, *args):

            # Updates the number bar width to display the current line numbers.
            #
            # The + 15 adds a bit of whitespace to the right of the line number.
            #
            width = int(log10(self.edit.document().blockCount()) + 1) * self.fontMetrics().averageCharWidth() + 5
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
                painter.drawText(self.width() - len(str(line_count)) * font_metrics.averageCharWidth() - 5,
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

        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Sunken)

        self.edit = QTextEdit()
        self.edit.setFrameStyle(QFrame.Shape.NoFrame)
        self.edit.setAcceptRichText(False)
        self.edit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.number_bar = self.NumberBar()
        self.number_bar.set_text_edit(self.edit)

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
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        print(self.scriptDir)

        self.setWindowTitle('PyQt6 Basic Editor Skeleton')
        self.setGeometry(100, 100, 800, 640)
        self.make_menu()
        self.addMainApp()
        self.show()
        self.statusBar().showMessage('Initialized.')

    def addMainApp(self):
        self.lineNumberedTextEdit = LineNumberedTextEdit()
        self.textEdit = self.lineNumberedTextEdit.getTextEdit()
        font = QFont()
        font.setStyleHint(QFont().StyleHint.Monospace)
        font.setFamily('monospace')
        self.textEdit.setFont(font)
        self.setCentralWidget(self.lineNumberedTextEdit)

    def make_menu(self):
        self.make_file_menu(self.menuBar())
        self.make_edit_menu(self.menuBar())
        self.make_search_menu(self.menuBar())
        self.make_tools_menu(self.menuBar())
        self.make_help_menu(self.menuBar())

    def make_file_menu(self, main_menu):
        file_menu = main_menu.addMenu('&File')

        new_action = QAction(QIcon(), 'New', self)
        new_action.setStatusTip('New clear edit area')
        new_action.triggered.connect(self.newFile)
        file_menu.addAction(new_action)

        open_action = QAction(QIcon(), 'Open', self)
        open_action.setStatusTip('Open file')
        open_action.triggered.connect(self.openFile)
        file_menu.addAction(open_action)

        save_action = QAction(QIcon(), 'Save', self)
        file_menu.addAction(save_action)

        save_as_action = QAction(QIcon(), 'Save as', self)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()

        exit_action = QAction(QIcon("application-exit.png"), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle('PyQt6 Basic Editor')

    def openFile(self):
        options  = QFileDialog.Options.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self,
            "QFileDialog.getOpenFileName()",
            "",
            "Python Files (*.py);;All Files (*)",
            options=options)
        if file_name:
            self.setWindowTitle(file_name.split("/")[-1])
            with open(file_name) as inputFile:
                file_data = inputFile.read()

            self.textEdit.clear()
            self.textEdit.setPlainText(file_data)
    #
    #
    #

    def make_edit_menu(self, main_menu):
        edit_menu = main_menu.addMenu('&Edit')

    def make_search_menu(self, main_menu):
        search_menu = main_menu.addMenu('&Search')

    def make_tools_menu(self, main_menu):
        tools_menu = main_menu.addMenu('&Tools')

        bwColorAction=QAction(QIcon(), 'Background Color', self)
        bwColorAction.setStatusTip('Select background color')
        bwColorAction.triggered.connect(self.color_picker)
        tools_menu.addAction(bwColorAction)

    def color_picker(self):
        color = QColorDialog.getColor()
        print(color.name())
        palette = self.textEdit.palette()
        palette.setColor(QPalette.ColorRole.Base, QColor(color))
        self.textEdit.setPalette(palette)

    def make_help_menu(self, main_menu):
        help_menu = main_menu.addMenu('&Help')

        about_action=QAction(QIcon(), 'About', self)
        about_action.setStatusTip('About this application')
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        about_qt_action=QAction(QIcon(), 'About Qt', self)
        about_qt_action.setStatusTip('About Qt and Qt Licensing')
        about_qt_action.triggered.connect(self.aboutQt)
        help_menu.addAction(about_qt_action)

    def about(self):
        QMessageBox.information(self, 'About', 'Basic Editor 0.3')

    def aboutQt(self):
        QMessageBox.aboutQt(self, 'About PyQt')

def save_settings():
    print("Exiting")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(save_settings)
    ex = App()
    print('PID',os.getpid())
    sys.exit(app.exec())
