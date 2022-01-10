from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt

from .styles import Styles

class ImageWidget(QWidget):
    width, height = 360, 480
    def __init__(self, parent):
        super().__init__(parent)
        self.frame_image = None
        self.roi = None
        self.limits = None
        self.levels = None

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

    def set_roi(self, roi):
        self.roi = roi
        self.update()

    def set_limits(self, limits):
        self.limits = limits
        self.update()

    def update_frame(self, frame):
        self.frame_image = frame.image
        self.roi = frame.roi
        self.limits = frame.limits
        self.levels = frame.levels
        self.update()

    def update(self):
        height, width, _ = self.frame_image.shape
        self.qImg = QImage(self.frame_image, width, height, QImage.Format_RGB888)
        self.qpixmap = QPixmap(self.qImg)
        self.painter = QPainter(self.qpixmap)
        self.painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))

        # Draw roi
        self.painter.drawRect(self.roi.x0, self.roi.y0, self.roi.width, self.roi.height)

        # Draw limits
        self.painter.drawLine(self.roi.x0, self.limits["y_min"], self.roi.x0 + self.roi.width, self.limits["y_min"])
        self.painter.drawLine(self.roi.x0, self.limits["y_max"], self.roi.x0 + self.roi.width, self.limits["y_max"])

        # Draw levels
        self.painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
        for level in self.levels:
            self.painter.drawLine(self.roi.x0, level["center"], self.roi.x0 + self.roi.width, level["center"])

        self.painter.end()
        self.image.setPixmap(self.qpixmap)