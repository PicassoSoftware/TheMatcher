from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
import time


class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.label = QLabel(self)
		self.loadImage()
		
	def loadImage(self):
		self.setWindowTitle("FSM")
		self.setGeometry(1000, 200, 640, 480)
		self.acceptDrops()
		
		self.pixmap = QPixmap('fsm.gv.svg').scaled(640,480)
			
		
		self.label.setPixmap(self.pixmap)
		self.label.resize(self.pixmap.width(),
						self.pixmap.height())
										
		self.show()
		QCoreApplication.processEvents()


