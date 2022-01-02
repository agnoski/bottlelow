from controller import Controller
import logging

from sensor.sensor_simulator import SensorSimulator
from video_stream.video_stream_simulator import VideoStreamSimulator
from led.led_simulator import LedSimulator
from neural.neural_net import NeuralNet

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s][%(levelname)s][%(name)s] %(message)s')

    mode = "Simulator"
    if mode == "Simulator":

        video_stream = VideoStreamSimulator("images/simulator")
        sensor = SensorSimulator()
        led = LedSimulator()

        queue_size = 1

        controller = Controller(video_stream, sensor, led, queue_size)
        neural_net =  NeuralNet("weights/weight_gray_3.h5")
        controller.register(lambda frame: logging.debug("Listener invoked"))
        controller.start()
        logging.info("waiting")