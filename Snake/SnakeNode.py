from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter

class SnakeNode(QtWidgets.QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QtCore.Qt.GlobalColor.darkBlue)
        painter.drawRect(75, 50, 50, 50)


