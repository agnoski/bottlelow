from PyQt5.QtWidgets import QWidget
from .image_widget import ImageWidget
from .control_widget import ControlWidget
from .run_mode.run_widget import RunWidget

class MainWidget(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent=parent)
        self.controller = controller
        self.mainUI()
        
    def mainUI(self):
        image_widget = ImageWidget(parent=self)
        image_widget.move(10,10)
        self.controller.register_publisher(image_widget.update_frame)

        control_state = ControlWidget(parent=self)
        control_state.move(390,10)

        control_roi = RunWidget(parent=self)
        control_roi.move(390,60)
        #TODO capire perché serve questo...
        control_roi.stackedWidget.move(390,60) 

        def update_max_limit(value):
            limits = self.controller.update_max_limit(value)
            image_widget.set_limits(limits)

        def update_min_limit(value):
            limits = self.controller.update_min_limit(value)
            image_widget.set_limits(limits)

        control_roi.signal_max_limit.connect(update_max_limit)
        control_roi.signal_min_limit.connect(update_min_limit)

        #train_widget = TrainWidget(parent=self)
        #train_widget.move(390,230)