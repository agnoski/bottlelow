from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QPushButton, QHBoxLayout, QVBoxLayout

from .styles import Styles

class ImageWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        image = QLabel()
        image.setFixedSize(360,480) # (240, 320) x 1.5
        image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        image.setScaledContents(True)

        def create_button(text, fun):
            button = QPushButton(text)
            button.setStyleSheet(Styles.btn_style)
            button.clicked.connect(fun)
            return button

        button_left = create_button("<-", lambda: print("Left"))
        button_right = create_button("->", lambda: print("Right"))
        button_delete = create_button("delete", lambda: print("Delete"))

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(button_left)
        btn_layout.addWidget(button_right)
        btn_layout.addWidget(button_delete)

        main_layout = QVBoxLayout()
        main_layout.addWidget(image)

        self.setLayout(btn_layout)