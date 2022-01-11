from app.config_manager import ConfigManager
from app.controller import Controller
from core.frame.frame_processor import FrameProcessor
from core.frame.roi import ROI
from core.hardware.hardware import Hardware
from core.hardware.led.led_simulator import LedSimulator
from core.hardware.sensor.sensor_simulator import SensorSimulator
from core.hardware.video_stream.video_stream_simulator import VideoStreamSimulator
from core.neural.neural_net import NeuralNet
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

import logging
import sys

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s][%(levelname)s][%(name)s] %(message)s')

    config_manager = ConfigManager("config.yaml")

    application_config = config_manager.config["application"]
    mode = application_config["mode"]

    hardware = None
    hardware_config = config_manager.config["hardware"]
    if mode == "Simulator":
        simulator_config = hardware_config["simulator"]
        sensor = SensorSimulator()
        video_stream = VideoStreamSimulator(simulator_config["images_folder_path"])
        led = LedSimulator()
        hardware = Hardware(sensor, video_stream, led)
    
    controller_config = config_manager.config["controller"]
    roi = ROI(controller_config["roi"])
    limits = controller_config["limits"]
    queue_size = controller_config["queue_size"]
    controller = Controller(hardware, roi, limits, queue_size)

    neural_config = config_manager.config["neural"]
    neural_net =  NeuralNet(neural_config["weights_file_path"])
    frame_processor = FrameProcessor(neural_net)

    controller.register_processor(frame_processor.process)
    controller.start()

    app = QApplication([])

    window = MainWindow(controller)
    window.show()

    sys.exit(app.exec_())