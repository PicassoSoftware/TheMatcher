#Pycharm için pip install PyQt5 yapılmalıdır.
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,  QWheelEvent
from textSearchGui import TextEdit


class Regex(QWidget):

    def __init__(self):
        super(Regex, self).__init__()
        #Arka plan renklerini, kutuların şeklini ayarlar.
        self.setStyleSheet(("""background-color: 
                               rgba(35,39,42); 
                               color: rgba(153,170,181); 
                               border-style: solid;
                               border-radius: 6px;
                               border-width: 3px; 
                               border-color: 
                               rgba(68,68,68);"""))
        #Butonları ekliyoruz.
        self.startButton = QPushButton('Start')
        self.stopButton = QPushButton('Stop')
        self.dfaButton = QPushButton('DFA')
        self.dfaButton.setEnabled(False)      #Dfa butonu basılı halde gelir.
        self.dfaButton.setStyleSheet("background-color :rgba(120, 123, 147) ")
        self.nfaButton = QPushButton('NFA')
        self.fileButton = QPushButton('Open File')
        self.nfaButton.setFixedSize(80, 30)
        self.dfaButton.setFixedSize(80, 30)
        self.fileButton.setFixedSize(80, 30)
        self.startButton.setFixedSize(100, 30)
        self.stopButton.setFixedSize(100, 30)

        self.initUI()

    def initUI(self):
        #Metin kutusu , butonlar ekleme işlemleri yapılır.
        self.text_css = 'border-style: none'
        self.title = QLabel('RegEx')
        self.text = QLabel('Text')
        self.text.setFixedSize(40, 20)

        self.title.setStyleSheet(self.text_css)
        self.text.setStyleSheet(self.text_css)

        self.lineEdit = QLineEdit(self.text)
        self.textEdit = QTextEdit()
        self.label = QLabel(self)
     

        self.mainLayout = QHBoxLayout()
        self.regexLayout = QHBoxLayout()
        self.metinLayout = QGridLayout()
        self.ssLayout = QHBoxLayout()  #start/ stop butonlarının eklendiği layout oluşturma
        self.layout1 = QVBoxLayout()  # sağ taraf için layout oluşturma
        self.layout2 = QVBoxLayout()  # sol taraf  için layout oluşturma
        self.nfaDfaLayout = QHBoxLayout()

        self.regexLayout.addWidget(self.title)
        self.regexLayout.addWidget(self.lineEdit)
        self.regexLayout.addWidget(self.fileButton)

        self.metinLayout.addWidget(self.text, 0, 0, 1, 1)
        self.metinLayout.addWidget(self.textEdit, 0, 1, 5, 3)

        self.layout2.addLayout(self.regexLayout)
        self.layout2.addLayout(self.metinLayout)
        self.layout2.addLayout(self.nfaDfaLayout)
        self.ssLayout.addStretch()
        self.ssLayout.addWidget(self.startButton)
        self.ssLayout.addWidget(self.stopButton)
        self.ssLayout.addStretch()

        self.nfaDfaLayout.addStretch()  #Boşluk bırakılmasını sağlar.
        self.nfaDfaLayout.addWidget(self.dfaButton)
        self.nfaDfaLayout.addWidget(self.nfaButton)
        self.nfaDfaLayout.addStretch()

        self.layout1.addWidget(self.label)
        self.layout1.addLayout(self.ssLayout)

        self.mainLayout.addLayout(self.layout2)
        self.mainLayout.addLayout(self.layout1)
        
        self.dfaButton.clicked.connect(self.select)
        self.nfaButton.clicked.connect(self.select)
        self.fileButton.clicked.connect(self.open)

        self.startButton.clicked.connect(self.search)
        self.stopButton.clicked.connect(self.stop)

        self.setLayout(self.mainLayout)

        self.setFixedSize(1600, 700)
        self.setWindowTitle(' The Matcher  ')

    def search(self):
        self.startButton.setStyleSheet("background-color : rgba(120, 123, 147)")
        self.stopButton.setStyleSheet('background-color: None')
        self.textEdit.setReadOnly(True)  #Text kısmına yazmayı engeller.

        if self.nfaButton.isEnabled():
            fa = True
        else:
            fa = False

        self.src = TextEdit(self.lineEdit.text(), self.textEdit.toPlainText()+" ", self.textEdit, fa, 0.2, self.label)
        self.src.run()

    def stop(self):
        self.src.stop = True   #Arama işlemini durdurur.
        self.textEdit.setReadOnly(False)
        self.stopButton.setStyleSheet("background-color : rgba(120, 123, 147)")
        self.startButton.setStyleSheet('background-color: None')

    def select(self):
        if self.sender().text() == 'DFA':
            self.dfaButton.setEnabled(False)
            self.nfaButton.setEnabled(True)  # Nfa butonu basılabilir haldedir.
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
