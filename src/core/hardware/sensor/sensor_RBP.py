from core.hardware.sensor.sensor import Sensor
from gpiozero import Button

class SensorRBP(Sensor):
    def __init__(self, sensor_id = 26):
        super().__init__()
        self.sensor = Button(sensor_id)

    def set_when_deactivated(self, fun):
        self.sensor.when_deactivated = fun