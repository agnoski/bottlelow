from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

import logging
import sys

from controller import Controller
from sensor.sensor_simulator import SensorSimulator
from frame.frame_processor import FrameProcessor
from video_stream.video_stream_simulator import VideoStreamSimulator
from led.led_simulator import LedSimulator
from neural.neural_net import NeuralNet
from frame.roi import ROI

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s][%(levelname)s][%(name)s] %(message)s')

    controller = None
    mode = "Simulator"
    if mode == "Simulator":

        video_stream = VideoStreamSimulator("images/simulator")
        sensor = SensorSimulator()
        led = LedSimulator()

        queue_size = 10

        # TODO: Load from config
        roi = ROI(100, 20, 280, 40)
        controller = Controller(video_stream, sensor, led, roi, queue_size)
        neural_net =  NeuralNet("weights/weight_gray_3.h5")

        frame_processor = FrameProcessor(neural_net)
        controller.register_processor(frame_processor.process)
        controller.start()
        logging.info("waiting")

    app = QApplication([])

    window = MainWindow(controller)
    window.show()

    sys.exit(app.exec_())