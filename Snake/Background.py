from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPalette
from PyQt5.QtWidgets import QSizePolicy


class Background(QtWidgets.QWidget):

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAutoFillBackground(True)
        self.palette = self.palette()
        self.palette.setColor(QPalette.Background, color)



    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)
        #painter.drawRect(50, 50, 50, 50)


