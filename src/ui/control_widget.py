from PyQt5.QtWidgets import QWidget, QHBoxLayout
from .button import Button

class ControlWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        h_layout = QHBoxLayout()
        h_layout.addWidget(Button("Start", lambda: print("Start")))
        h_layout.addWidget(Button("Stop", lambda: print("Stop")))
        h_layout.addWidget(Button("Train", lambda: print("Train")))
        h_layout.addWidget(Button("Exit", lambda: print("Exit")))
        
        self.setLayout(h_layout)