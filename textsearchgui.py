import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QTextCharFormat, QTextDocument, QTextCursor, QColor, QPainter
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                             QToolBar, QLineEdit, QPushButton, QColorDialog, QHBoxLayout, QWidget)
import reg2nfa
import statemanager
import time

nfaController = reg2nfa.formal_nfa('Esra')
controlManager = statemanager.CheckStateManager(nfaController)

txt = "Esra Erkin Hatice daima elele abc "


class TextEdit(QMainWindow):
    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        kelimeler = txt.split()
        kelimeler.reverse()
        self.textEdit.setText(txt)
        self.textEdit.resize(800, 600)
        self.resize(800, 600)
        self.wait(0.2)
        start = 0
        n = 0
        for i, char in enumerate(txt):
            if char == " ":
                self.highlight(start, i - start, 2)
                self.wait(0.4)
                print(txt[start: i])
                if controlManager.checkString(txt[start: i]):
                    self.highlight(start, i - start, 1)
                start = i + 1

        self.setCentralWidget(self.textEdit)

    def highlight(self, start, n, col):
        cursor = self.textEdit.textCursor()
        clr = QColor(0, 0, 0)
        if col == 1:
            clr = QColor(0, 255, 0)
        elif col == 2:
            clr = QColor(255, 0, 255, 127)

        # metin rengi
        fmt = QTextCharFormat()
        fmt.setForeground(clr)

        cursor.setPosition(start)
        cursor.movePosition(QTextCursor.Right,
                            QTextCursor.KeepAnchor, n)  # keepanchor, merge bak
        cursor.mergeCharFormat(fmt)

    def wait(self, second):
        self.show()
        QCoreApplication.processEvents() #Belirtilen bayraklara göre çağıran iş parçacığı için bazı bekleyen olayları işleyen fonk.
        time.sleep(second)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    textEdit = TextEdit()
    textEdit.show()

    sys.exit(app.exec_())
