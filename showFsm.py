from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
import time


class Window(QWidget): 
	def __init__(self, label = None):
		super().__init__()
		self.label = label
		self.loadImage()
		
	def loadImage(self):
		self.acceptDrops()
		
		self.pixmap = QPixmap('fsm.gv.svg').scaled(640,480)
			
		
		self.label.setPixmap(self.pixmap)
		self.label.resize(self.pixmap.width(),
						self.pixmap.height())
					
		QCoreApplication.processEvents()


