import logging
from frame.roi import ROI
from frame.frame import Frame

from worker import Worker
from video_stream.video_stream import VideoStream
from led.led import Led
from sensor.sensor import Sensor
from time import sleep
from queue import Full, Queue

class Controller:
    WAIT_TIME_LED_ON = 0.1
    WAIT_TIME_LED_OFF = 0.5

    def __init__(self, video_stream:VideoStream, sensor:Sensor, led:Led, roi:ROI, limits, queue_size:int = 0) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.video_stream = video_stream
        self.led = led
        self.sensor = sensor
        self.roi = roi
        self.limits = limits
        self.input_queue = Queue(queue_size)
        self.output_queue = Queue(queue_size)

        self.started = False
        self.processors = []
        self.publishers = []
        self.thread_processor = Worker(target=self.process, name="Processor", args=(), daemon=True)
        self.thread_publisher = Worker(target=self.publish, name="Processor", args=(), daemon=True)

    def start(self):
        self.video_stream.start()
        self.sensor.set_when_deactivated(self.pipe)
        self.sensor.start()
        self.started = True
        self.thread_processor.start()
        self.thread_publisher.start()

    def close(self):
        self.started = False
        self.input_queue.join()
        self.output_queue.join()
        self.sensor.stop()

    def set_roi(self, roi):
        self.roi = roi

    def set_limits(self, limits):
        self.limits = limits

    def update_max_limit(self, val):
        self.limits["y_max"] = self.limits["y_max"] + val
        return self.limits

    def update_min_limit(self, val):
        self.limits["y_min"] = self.limits["y_min"] + val
        return self.limits

    def update_roi(self, val):
        self.roi.x0 = self.roi.x0 + val
        return self.roi

    def disable_sensor(self):
        self.sensor.set_when_deactivated(None)

    def pipe(self):
        self.logger.debug("Processing event")
        self.led.on()
        sleep(self.WAIT_TIME_LED_ON)
        try:
            image = self.video_stream.read()
            self.input_queue.put_nowait(image)
        except Full:
            self.logger.error("Failed to add image. Input queue full")
        sleep(self.WAIT_TIME_LED_OFF)
        self.led.off()

    def register_processor(self, processor):
        self.processors.append(processor)

    def register_publisher(self, publisher):
        self.publishers.append(publisher)

    def process(self):
        while(self.started):
            image = self.input_queue.get()
            frame = Frame(image, self.roi, self.limits)
            self.logger.info("Processing new image")
            for processor in self.processors:
                try:
                    frame = processor(frame)
                    self.output_queue.put_nowait(frame)
                except Full:
                    self.logger.error("Failed to add frame. Output queue full")
            self.input_queue.task_done()
        self.logger.info("Closing process controller...")

    def publish(self):
        while(self.started):
            self.logger.info("Waiting new frame")
            frame = self.output_queue.get()
            self.logger.info("Publishing new frame")
            for publisher in self.publishers:
                publisher(frame)
            self.output_queue.task_done()

        self.logger.info("Closing publish controller...")