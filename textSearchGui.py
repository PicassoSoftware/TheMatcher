import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QTextCharFormat, QTextCursor, QColor
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit)
import reg2nfa
import nfa2dfa
import statemanager
import time
import os


class TextEdit(QWidget):
    def __init__(self, regex='a*li', txt="ali veli", textEdit = None, fa = False, timer = 0.4, label = None):
        super(TextEdit, self).__init__()

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
        os.remove("fsm.txt.svg") 
        


    def highlight(self, start, n, col):
        cursor = self.textEdit.textCursor()
        clr = QColor(255,255,255)
        if col == 1:
            clr = QColor(0, 255, 0)
        elif col == 2:
            clr = QColor(255, 255, 0)
        elif col == 3:
            clr = QColor(255,255,255)

        # metin rengi
        fmt = QTextCharFormat()
        fmt.setForeground(clr)

        cursor.setPosition(start)
        cursor.movePosition(QTextCursor.Right,
                            QTextCursor.KeepAnchor, n)  
        cursor.mergeCharFormat(fmt)

    def wait(self, second):
        QCoreApplication.processEvents()
        time.sleep(second)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    textdit = QTextEdit()

    textEdit = TextEdit('(ab)*', 'aba abbbaa abaaa aba ab ', textdit)
    textEdit.run()
    textEdit.show()

    sys.exit(app.exec_())
