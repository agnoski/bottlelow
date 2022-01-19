from PyQt5.QtWidgets import QMainWindow
from .main_widget import MainWidget

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title = "BottleLow"
        #self.left = 0
        #self.top = 0

        #self.setCursor(Qt.BlankCursor)
        self.initUI()

    def closeEvent(self, event):
        self.controller.close()
        event.accept()

    def initUI(self):
        self.setWindowTitle(self.title)
        widget = MainWidget(parent=self, controller=self.controller)
        self.setCentralWidget(widget)
        self.setFixedSize(1024, 600)
        #self.showFullScreen()