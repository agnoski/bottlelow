from sensor.sensor import Sensor
from threading import Thread
from time import sleep

class SensorSimulator(Sensor):
    SLEEP_TIME = 5

    def __init__(self):
        super().__init__()
        self.thread = Thread(target=self.run, args=(), daemon=True)
        self.fun = None
        self.started = False

    def set_when_deactivated(self, fun):
        self.fun = fun
        self.started = True
        self.thread.start()

    def run(self):
        self.logger.info("Sensor Simulator started")
        while(self.started):
            self.logger.debug("Sensor triggered")
            self.fun()
            sleep(self.SLEEP_TIME)