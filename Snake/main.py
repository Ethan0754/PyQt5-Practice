import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snake")
        self.setMinimumSize(800, 400)

        self.label = QLabel(self)

        canvas = QtGui.QPixmap(800, 400)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        painter = QPainter(self.label.pixmap())
        painter.setRenderHint(QPainter.Antialiasing)
        green_brush = QBrush(Qt.green, Qt.SolidPattern)
        light_green_brush = QBrush(QColor(144, 238, 144), Qt.SolidPattern)
        painter.setBrush(light_green_brush)

        color_switch = True
        for i in range(10):
            for j in range(10):
                painter.drawRect(50*j, 50*i, 50, 50)
                if color_switch:
                    painter.setBrush(green_brush)
                else:
                    painter.setBrush(light_green_brush)
                color_switch = not color_switch
            color_switch = not color_switch
        painter.end()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
