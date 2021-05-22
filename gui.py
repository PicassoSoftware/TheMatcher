import sys
from PyQt5.QtCore import QCoreApplication, QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,  QWheelEvent
from textsearchgui import TextEdit


class Regex(QWidget):

    def __init__(self):
        super(Regex, self).__init__()

        self.setStyleSheet((" background-color: \
                               rgba(44, 47, 51); \
                               color: rgba(180,180,180); \
                               border-style: solid;\
                               border-radius: 6px; \
                               border-width: 1px; \
                               border-color: \
                               rgba(0,0,0);"))

        self.startButton = QPushButton('Start')
        self.stopButton = QPushButton('Stop')
        self.dfaButton = QPushButton('DFA')
        self.nfaButton = QPushButton('NFA')
        self.fileButton = QPushButton('Open File')
        self.nfaButton.setFixedSize(80, 30)
        self.dfaButton.setFixedSize(80, 30)
        self.fileButton.setFixedSize(80, 30)
        self.startButton.setFixedSize(100, 30)
        self.stopButton.setFixedSize(100, 30)

        self.initUI()

    def initUI(self):
        self.text_css = 'border-style: none'
        self.title = QLabel('RegEx')
        self.text = QLabel('Text')
        self.text.setFixedSize(40, 20)

        self.title.setStyleSheet(self.text_css)
        self.text.setStyleSheet(self.text_css)

        self.lineEdit = QLineEdit(self.text)
        self.textEdit = QTextEdit()
        #self.textEdit.setFixedSize(580, 400)
        self.label = QLabel(self)
        #self.label.setFixedSize(600, 420)
        self.txt = QTextEdit()

        self.mainLayout = QHBoxLayout()
        self.regexLayout = QHBoxLayout()
        self.metinLayout = QGridLayout()
        self.ssLayout = QHBoxLayout()
        self.layout1 = QVBoxLayout()  # sağ taraf için layout oluşturma
        self.layout2 = QVBoxLayout()  # sol taraf  için layout oluşturma
        self.nfaDfaLayout = QHBoxLayout()

        self.regexLayout.addWidget(self.title)
        self.regexLayout.addWidget(self.lineEdit)

        self.metinLayout.addWidget(self.text, 0, 0, 1, 1)
        self.metinLayout.addWidget(self.textEdit, 0, 1, 5, 3)

        self.layout2.addLayout(self.regexLayout)
        self.layout2.addLayout(self.metinLayout)
        self.layout2.addLayout(self.ssLayout)
        self.ssLayout.addWidget(self.fileButton)
        self.ssLayout.addStretch()
        self.ssLayout.addWidget(self.startButton)
        self.ssLayout.addWidget(self.stopButton)
        self.ssLayout.addStretch()

        self.nfaDfaLayout.addStretch()
        self.nfaDfaLayout.addWidget(self.dfaButton)
        self.nfaDfaLayout.addWidget(self.nfaButton)
        self.nfaDfaLayout.addStretch()

        self.layout1.addWidget(self.label)
        self.layout1.addLayout(self.nfaDfaLayout)

        self.mainLayout.addLayout(self.layout2)
        self.mainLayout.addLayout(self.layout1)

        self.dfaButton.clicked.connect(self.select)
        self.nfaButton.clicked.connect(self.select)
        self.fileButton.clicked.connect(self.open)

        self.startButton.clicked.connect(self.search)
        self.stopButton.clicked.connect(self.stop)

        self.setLayout(self.mainLayout)

        self.setGeometry(50, 50, 1200, 500)
        self.setWindowTitle(' Giriş ')

    def search(self):
        self.startButton.setStyleSheet("background-color : rgba(120, 123, 147)")
        self.stopButton.setStyleSheet('background-color: None')
        self.textEdit.setReadOnly(True)

        if self.nfaButton.isEnabled():
            fa = True
        else:
            fa = False

        self.src = TextEdit(self.lineEdit.text(), self.textEdit.toPlainText() + " ", self.textEdit, fa, 0.4, self.label)
        self.src.run()

    def stop(self):
        self.src.stop = True
        self.textEdit.setReadOnly(False)
        self.stopButton.setStyleSheet("background-color : rgba(120, 123, 147)")
        self.startButton.setStyleSheet('background-color: None')
        self.dfaButton.setStyleSheet('background-color: None')
        self.nfaButton.setStyleSheet('background-color: None')

    def select(self):
        if self.sender().text() == 'DFA':
            self.dfaButton.setEnabled(False)
            self.nfaButton.setEnabled(True)
            self.dfaButton.setStyleSheet("background-color :rgba(120, 123, 147) ")
            self.nfaButton.setStyleSheet('background-color: None')
        else:
            self.nfaButton.setEnabled(False)
            self.dfaButton.setEnabled(True)
            self.nfaButton.setStyleSheet("background-color : rgba(120, 123, 147)")
            self.dfaButton.setStyleSheet('background-color: None')

    def open(self):
        options = QFileDialog.Options()
        
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Text (*.txt)', options=options)
        
        if fileName:
            with open(fileName) as f:
                contents = f.read()
                self.textEdit.setText(contents)

def main():
    app = QApplication(sys.argv)
    ex = Regex()
    ex.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()