from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from .main_widget import MainWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.title = "BottleLow"
        #self.left = 0
        #self.top = 0

        #self.setCursor(Qt.BlankCursor)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title) 
        widget = MainWidget(parent=self)
        self.setCentralWidget(widget)
        self.setFixedSize(1024, 400)
        #self.showFullScreen()