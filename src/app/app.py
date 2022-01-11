from app.config_manager import ConfigManager
from app.controller import Controller
from core.frame.frame_processor import FrameProcessor
from core.frame.roi import ROI
from core.hardware.hardware import Hardware
from core.hardware.led.led_simulator import LedSimulator
from core.hardware.sensor.sensor_simulator import SensorSimulator
from core.hardware.video_stream.video_stream_simulator import VideoStreamSimulator
from core.neural.neural_net import NeuralNet

import logging

class App:
    def __init__(self, path_config):
        self.logger = logging.getLogger(self.__class__.__name__)

        config_manager = ConfigManager(path_config)

        application_config = config_manager.config["application"]
        mode = application_config["mode"]

        neural_config = config_manager.config["neural"]
        frame_processor = self._init_frame_processor(neural_config)

        hardware_config = config_manager.config["hardware"]
        hardware = self._init_hardware(mode, hardware_config)
        
        controller_config = config_manager.config["controller"]
        self.controller = self._init_controller(hardware, controller_config)

        self.controller.register_processor(frame_processor.process)

    def _init_frame_processor(self, neural_config):
        self.logger.info("Init frame processor...")

        neural_net =  NeuralNet(neural_config["weights_file_path"])
        return FrameProcessor(neural_net)

    def _init_hardware(self, mode, hardware_config):
        self.logger.info("Init hardware...")

        hardware = None
        if mode == "Simulator":
            hardware = self._init_hardware_simulator(hardware_config["simulator"])
        elif mode == "RBP":
            hardware = self._init_hardware_rbp(hardware_config["rbp"])

        return hardware

    def _init_hardware_simulator(self, simulator_config):
        sensor = SensorSimulator()
        video_stream = VideoStreamSimulator(simulator_config["images_folder_path"])
        led = LedSimulator()
        return Hardware(sensor, video_stream, led)

    def _init_hardware_rbp(self, rbp_config):
        pins_config = rbp_config["pins"]
        sensor = SensorRBP(pins_config["sensor"])
        led = LedRBP(pins_config["flash"])

        cam_config = rbp_config["cam"]
        video_stream = WebcamVideoStream(cam_config["src"], cam_config["width"], cam_config["height"])

        return Hardware(sensor, video_stream, led)

    def _init_controller(self, hardware, controller_config):
        self.logger.info("Init controller...")

        roi = ROI(controller_config["roi"])
        limits = controller_config["limits"]
        queue_size = controller_config["queue_size"]
        return Controller(hardware, roi, limits, queue_size)

    def start(self):
        self.controller.start()

    def get_controller(self):
        return self.controller