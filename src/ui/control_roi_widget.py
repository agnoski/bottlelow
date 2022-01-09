from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
from PyQt5.QtCore import pyqtSignal
from .styles import Styles

class ControlROIWidget(QWidget):
    VAL_INCREASE = 1

    signal_max_limit = pyqtSignal(int)
    signal_min_limit = pyqtSignal(int)
    signal_move_roi = pyqtSignal(int)

    def __init__(self,parent):
        super().__init__(parent)
        layout = QHBoxLayout()

        def create_UpDown_layout(title, textUp, textDown, fun1, fun2):
            group = QGroupBox(title)
            button_up = create_button(textUp, fun1)
            button_down = create_button(textDown, fun2)
            layout = QVBoxLayout()
            layout.addWidget(button_up)
            layout.addWidget(button_down)
            group.setLayout(layout)
            return group

        def create_button(text, fun):
            button = QPushButton(text)
            button.setFixedSize(Styles.button_size)
            button.setStyleSheet(Styles.btn_style)
            button.clicked.connect(fun)
            return button

        def update_max_limit(val):
            self.signal_max_limit.emit(val)

        def update_min_limit(val):
            self.signal_min_limit.emit(val)

        def update_roi(val):
            self.signal_move_roi.emit(val)

        layout.addWidget(create_UpDown_layout('max limit', '+', '-', lambda: update_max_limit(self.VAL_INCREASE), lambda: update_max_limit(-self.VAL_INCREASE)))
        layout.addWidget(create_UpDown_layout('min limit', '+', '-', lambda: update_min_limit(self.VAL_INCREASE), lambda: update_min_limit(-self.VAL_INCREASE)))
        layout.addWidget(create_UpDown_layout('move rect.', '<-', '->', lambda: update_roi(-self.VAL_INCREASE), lambda: update_roi(self.VAL_INCREASE)))
        self.setLayout(layout)
