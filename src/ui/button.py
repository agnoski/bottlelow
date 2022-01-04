from PyQt5.QtWidgets import QPushButton
from .styles import Styles

class Button(QPushButton):
    def __init__(self, text, fun):
        super().__init__(text)
        self.setFixedSize(Styles.button_size)
        self.clicked.connect(fun)
