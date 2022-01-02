import logging

from video_stream.video_stream import VideoStream
from led.led import Led
from sensor.sensor import Sensor
from time import sleep
from threading import Thread
from queue import Full, Queue

class Controller:
    WAIT_TIME_LED_ON = 0.1
    WAIT_TIME_LED_OFF = 0.5

    def __init__(self, video_stream:VideoStream, sensor:Sensor, led:Led, queue_size:int = 0) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.video_stream = video_stream
        self.led = led
        self.sensor = sensor
        self.queue = Queue(queue_size)
        self.listeners = []
        self.started = False
        self.thread = Thread(target=self.notifier, args=(), daemon=True)

    def start(self):
        self.video_stream.start()
        self.sensor.set_when_deactivated(self.pipe)
        self.started = True
        self.thread.start()
        self.thread.join()

    def disable_sensor(self):
        self.sensor.set_when_deactivated(None)

    def pipe(self):
        self.logger.debug("Controller: processing event")
        self.led.on()
        sleep(self.WAIT_TIME_LED_ON)
        try:
            frame = self.video_stream.read()
            self.queue.put_nowait(frame)
        except Full:
            self.logger.error("Controller: failed to add image. Queue Full")
        sleep(self.WAIT_TIME_LED_OFF)
        self.led.off()

    def register(self, listener):
        self.listeners.append(listener)

    def notifier(self):
        while(self.started):
            frame = self.queue.get()
            self.logger.info("Processing new frame")
            for listener in self.listeners:
                listener(frame)