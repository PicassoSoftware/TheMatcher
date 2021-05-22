import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QTextCharFormat, QTextCursor, QColor
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit)
import reg2nfa
import nfa2dfa
import statemanager
import time


# txt = "1001 10000 10000000 100000000 000000000000 1010111101 101001 1001001 1001010011 0101101 001 10100 1010100 0100001 0000001 000000"
class TextEdit(QWidget):
    def __init__(self, regex=' ', txt=" ", textEdit = None, fa = False, timer = 0.4, label = None, parent=None):
        super(TextEdit, self).__init__(parent)

        self.stop = False
        self.regex = regex
        self.txt = txt
        self.textEdit = textEdit
        self.timer = timer

        self.wait(self.timer)

        if not fa:
            nfaController = reg2nfa.formal_nfa(self.regex)
        else:
            nfaController = nfa2dfa.formal_dfa(self.regex)

        self.controlManager = statemanager.CheckStateManager(nfaController, label)


    def run(self):
        start = 0
        for i, char in enumerate(self.txt):
            if self.stop:
                break
            if char == " ":
                self.highlight(start, i - start, 2)
                self.wait(self.timer)
                
                if self.controlManager.checkString(self.txt[start: i]):
                    self.highlight(start, i - start, 1)
                else:
                    self.highlight(start, i - start, 3)
                start = i + 1
        


    def highlight(self, start, n, col):
        cursor = self.textEdit.textCursor()
        clr = QColor(0, 0, 0)
        if col == 1:
            clr = QColor(0, 255, 0)
        elif col == 2:
            clr = QColor(255, 255, 0)
        elif col == 3:
            clr = QColor(0, 0, 0)

        # metin rengi
        fmt = QTextCharFormat()
        fmt.setForeground(clr)

        cursor.setPosition(start)
        cursor.movePosition(QTextCursor.Right,
                            QTextCursor.KeepAnchor, n)  # keepanchor, merge bak
        cursor.mergeCharFormat(fmt)

    def wait(self, second):
        QCoreApplication.processEvents() #Belirtilen bayraklara göre çağıran iş parçacığı için bazı bekleyen olayları işleyen fonk.
        time.sleep(second)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    textdit = QTextEdit()

    textEdit = TextEdit('(ab)*', 'aba abbbaa abaaa aba ab ', textdit)
    textEdit.run()
    textEdit.show()

    sys.exit(app.exec_())
