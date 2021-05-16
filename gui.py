import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from statemanager import CheckStateManager
import reg2nfa
from textsearchgui import TextEdit
from showFsm import Window
from graphviz import Digraph


class Regex(QWidget):

    def __init__(self):
        super(Regex, self).__init__()
        self.saveButton = QPushButton('Save')
        self.dfaButton = QPushButton('DFA')
        self.nfaButton = QPushButton('NFA')
        self.nfaButton.setFixedSize(100, 30)
        self.dfaButton.setFixedSize(100, 30)
        self.saveButton.setFixedSize(100, 30)

        self.initUI()

    def initUI(self):
        self.title = QLabel('REGEX')
        self.text = QLabel('Metin')

        self.lineEdit = QLineEdit(self.text)
        self.textEdit = QTextEdit()
        self.label = QLabel(self)
        #self.searchBox.setReadOnly(True)
        
        #self.Window = QWidget()
        #self.ornek = QTextEdit()


        self.txt = QTextEdit()

        self.mainLayout = QHBoxLayout()
        self.regexLayout = QHBoxLayout()
        self.metinLayout = QHBoxLayout()
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
        self.layout2.addWidget(self.saveButton)

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

        # mainLayout = QHBoxLayout()
        #
        #
        # qvbox = QVBoxLayout()
        # qvbox.setSpacing(10)
        #
        # qvbox.addWidget(title)
        # qvbox.addWidget(self.lineEdit)
        #
        # qvbox.addWidget(text)
        # qvbox.addWidget(self.textEdit)
        #
        #
        # qvbox.addWidget(self.savebtn)
        self.saveButton.clicked.connect(self.saveText)
        self.saveButton.clicked.connect(self.saveRegex)
        self.saveButton.clicked.connect(self.search)
        #
        # qvbox.addWidget(self.dfabtn)
        # self.dfabtn.setAccessibleName("DFA")
        # self.dfabtn.clicked.connect(self.select)
        # name = self.dfabtn.accessibleName()
        #
        # #qvbox.addWidget(self.fsm, 1, 6, 6, 1)
        # #qvbox.addLayout()
        #
        # qvbox.addWidget(self.txt)

        self.setLayout(self.mainLayout)

        self.setGeometry(50, 50, 1200, 500)
        self.setWindowTitle(' Giriş ')

    def saveRegex(self):
        self.regex = self.lineEdit.text()

    def search(self):
        self.textEdit.setReadOnly(True)
        #self.textEdit.setText(self.textEdit.toPlainText())

        if self.nfaButton.isEnabled():
            fa = False
        else:
            fa = True


        #self.fsm = Digraph("FSM","FSMtext.txt",format="svg")   
        self.src = TextEdit(self.lineEdit.text(), self.textEdit.toPlainText() + " ", self.textEdit, fa, self.label)
        self.src.run()
        self.textEdit.setReadOnly(False)

      # self.deneme.show()
    
        
    def saveText(self):
        with open('text.txt', 'w') as f:
            url_text = self.textEdit.toPlainText()
            f.write(url_text)



    # def select(self):
    #     if self.dfabtn.accessibleName() == 'NFA':
    #         self.dfabtn.setAccessibleName('DFA')
    #         self.dfabtn.setText('DFA')
    #
    #     else:
    #         self.dfabtn.setAccessibleName('NFA')
    #         self.dfabtn.setText('NFA')

    def select(self):
        if self.sender().text() == 'DFA':
            self.dfaButton.setEnabled(False)
            self.nfaButton.setEnabled(True)
            if (not self.dfaButton.isEnabled()):
                print('DFA seçildi.')
        else:
            self.nfaButton.setEnabled(False)
            self.dfaButton.setEnabled(True)
            if (not self.nfaButton.isEnabled()):
                print('Nfa seçildi.')
    
    def loadImage(self):
        self.acceptDrops()

        self.pixmap = QPixmap('fsm.gv.svg').scaled(640,480)

        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),self.pixmap.height())
        QCoreApplication.processEvents()

def main():
    app = QApplication(sys.argv)
    ex = Regex()
    ex.show()


    sys.exit(app.exec_())
    print("hatice")


if __name__ == '__main__':
    main()