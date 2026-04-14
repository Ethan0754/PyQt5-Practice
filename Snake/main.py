import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QSizePolicy

from Snake.Background import Background
from Snake.SnakeNode import SnakeNode


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("First Program")

        self.showMaximized()
        # self.setMinimumSize(QSize(100, 100))
        #self.setMaximumSize(QSize(500, 500))



app = QApplication(sys.argv)

window = MainWindow()
window.show()

layout = QGridLayout()
layout.setSpacing(0)

green_background = Background(QtCore.Qt.GlobalColor.green)
dark_green_background = Background(QtCore.Qt.GlobalColor.darkGreen)
alternate = 1
for row in range(10):
    for col in range(10):
        layout.setRowStretch(row, 1)
        layout.setColumnStretch(col, 1)
        if (col+alternate)%2 == 0:
            colored_widget = QWidget()
            colored_widget.setStyleSheet("background-color: green;")
            layout.addWidget(colored_widget, row, col)
            alternate = 1
        else:
            colored_widget = QWidget()
            colored_widget.setStyleSheet("background-color:rgb(0,255,0);")
            layout.addWidget(colored_widget, row, col)
            alternate = 0






snake_node = SnakeNode()
layout.addWidget(snake_node, 1, 0)

window.setLayout(layout)

app.exec()