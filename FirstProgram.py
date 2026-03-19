import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("First Program")
        button = QPushButton("Click me")

        #self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(100, 100))
        self.setMaximumSize(QSize(500, 500))

        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()