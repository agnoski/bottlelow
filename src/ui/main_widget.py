from PyQt5.QtWidgets import QWidget
from .image_widget import ImageWidget
from .control_widget import ControlWidget
from .control_roi_widget import ControlROIWidget

class MainWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.mainUI()
        
    def mainUI(self):
        image = ImageWidget(parent=self)
        image.move(10,10)

        control_state = ControlWidget(parent=self)
        control_state.move(390,10)

        control_roi = ControlROIWidget(parent=self)
        control_roi.move(390,65)

        #train_widget = TrainWidget(parent=self)
        #train_widget.move(390,230)