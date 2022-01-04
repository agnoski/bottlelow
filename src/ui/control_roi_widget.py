from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
from .styles import Styles

class ControlROIWidget(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        layout = QHBoxLayout()

        def create_UpDown_layout(title, textUp, textDown, fun):
            group = QGroupBox(title)
            button_up = create_button(textUp, fun)
            button_down = create_button(textDown, fun)
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

        layout.addWidget(create_UpDown_layout('max limit', '+', '-', lambda x: x))
        layout.addWidget(create_UpDown_layout('min limit', '+', '-', lambda x: x))
        layout.addWidget(create_UpDown_layout('move rect.', '<-', '->', lambda x: x))
        self.setLayout(layout)
