from config_manager import ConfigManager
from controller import Controller
from frame.frame_processor import FrameProcessor
from frame.roi import ROI
from led.led_simulator import LedSimulator
from neural.neural_net import NeuralNet
from PyQt5.QtWidgets import QApplication
from sensor.sensor_simulator import SensorSimulator
from ui.main_window import MainWindow
from video_stream.video_stream_simulator import VideoStreamSimulator

import logging
import sys

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s][%(levelname)s][%(name)s] %(message)s')

    config_manager = ConfigManager("config.yaml")

    application_config = config_manager.config["application"]
    mode = application_config["mode"]

    controller_config = config_manager.config["controller"]
    roi = ROI(controller_config["roi"])
    limits = controller_config["limits"]
    queue_size = controller_config["queue_size"]

    controller = None
    if mode == "Simulator":
        simulator_config = config_manager.config["simulator"]
        video_stream = VideoStreamSimulator(simulator_config["images_folder_path"])
        sensor = SensorSimulator()
        led = LedSimulator()

        controller = Controller(video_stream, sensor, led, roi, limits, queue_size)

    neural_config = config_manager.config["neural"]
    neural_net =  NeuralNet(neural_config["weights_file_path"])
    frame_processor = FrameProcessor(neural_net)

    controller.register_processor(frame_processor.process)
    controller.start()

    app = QApplication([])

    window = MainWindow(controller)
    window.show()

    sys.exit(app.exec_())