from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt

from .styles import Styles

class ImageWidget(QWidget):
    width, height = 360, 480
    def __init__(self, parent):
        super().__init__(parent)

        self.image = QLabel()
        self.image.setFixedSize(self.width, self.height) # (240, 320) x 1.5
        self.image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image.setScaledContents(True)
        self.image.setPixmap(QPixmap(self.width, self.height))

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
        main_layout.addWidget(self.image)

        #self.setLayout(btn_layout)
        self.setLayout(main_layout)

    def update_image(self, frame):
        image = frame.image
        roi = frame.roi
        height, width, _ = image.shape
        self.qImg = QImage(image, width, height, QImage.Format_RGB888)
        self.qpixmap = QPixmap(self.qImg)
        self.painter = QPainter(self.qpixmap)
        self.painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        self.painter.drawRect(roi.x0, roi.y0, roi.width, roi.height)
        self.painter.end()
        self.image.setPixmap(self.qpixmap)