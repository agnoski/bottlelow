from gpiozero import BUTTON
from sensor.sensor import Sensor

class SensorRBP(Sensor):
    def __init__(self, sensor_id):
        super().__init__()
        self.sensor = BUTTON(sensor_id)

    def set_when_deactivated(self, fun):
        self.sensor.when_deactivated = fun