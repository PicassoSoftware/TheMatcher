import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from textsearchgui import TextEdit


class Regex(QWidget):

    def __init__(self):
        super(Regex, self).__init__()
        self.startButton = QPushButton('Start')
        self.stopButton = QPushButton('Stop')
        self.dfaButton = QPushButton('DFA')
        self.nfaButton = QPushButton('NFA')
        self.nfaButton.setFixedSize(100, 30)
        self.dfaButton.setFixedSize(100, 30)
        self.startButton.setFixedSize(100, 30)
        self.stopButton.setFixedSize(100, 30)

        self.initUI()

    def initUI(self):
        self.title = QLabel('REGEX')
        self.text = QLabel('Metin')

        self.lineEdit = QLineEdit(self.text)
        self.textEdit = QTextEdit()
        self.label = QLabel(self)

        self.txt = QTextEdit()

        self.mainLayout = QHBoxLayout()
        self.regexLayout = QHBoxLayout()
        self.metinLayout = QHBoxLayout()
        self.ssLayout = QHBoxLayout()
        self.layout1 = QVBoxLayout()  #sağ taraf için layout oluşturma
        self.layout2 = QVBoxLayout()  #sol taraf  için layout oluşturma
        self.nfaDfaLayout = QHBoxLayout()

        self.regexLayout.addWidget(self.title)
        self.regexLayout.addWidget(self.lineEdit)

        self.metinLayout.addWidget(self.text)
        self.metinLayout.addWidget(self.textEdit)

        self.layout2.addLayout(self.regexLayout)
        self.layout2.addWidget(self.text)
        self.layout2.addWidget(self.textEdit)
        self.layout2.addLayout(self.ssLayout)
        self.ssLayout.addWidget(self.startButton)
        self.ssLayout.addWidget(self.stopButton)
        self.ssLayout.addStretch()

        self.nfaDfaLayout.addStretch()
        self.nfaDfaLayout.addWidget(self.dfaButton)
        self.nfaDfaLayout.addWidget(self.nfaButton)
        self.nfaDfaLayout.addStretch()

        self.layout1.addLayout(self.nfaDfaLayout)
        self.layout1.addWidget(self.label)

        self.mainLayout.addLayout(self.layout2)
        self.mainLayout.addLayout(self.layout1)

        self.dfaButton.clicked.connect(self.select)
        self.nfaButton.clicked.connect(self.select)

        self.startButton.clicked.connect(self.search)
        self.stopButton.clicked.connect(self.stop)

        self.setLayout(self.mainLayout)

        self.setGeometry(50, 50, 1200, 500)
        self.setWindowTitle(' Giriş ')

    def search(self):
        self.textEdit.setReadOnly(True)
 
        if self.nfaButton.isEnabled():
            fa = False
        else:
            fa = True
  
        self.src = TextEdit(self.lineEdit.text(), self.textEdit.toPlainText() + " ", self.textEdit, fa, 0.4, self.label)
        self.src.run()

    def stop(self):
        self.src.stop = True
        self.textEdit.setReadOnly(False)

    def select(self):
        if self.sender().text() == 'DFA':
            self.dfaButton.setEnabled(False)
            self.nfaButton.setEnabled(True)
        else:
            self.nfaButton.setEnabled(False)
            self.dfaButton.setEnabled(True)


def main():
    app = QApplication(sys.argv)
    ex = Regex()
    ex.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()