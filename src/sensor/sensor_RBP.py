from sensor.sensor import Sensor
from gpiozero import BUTTON

class SensorRBP(Sensor.Sensor):
    def __init__(self, sensor_id):
        self.sensor = BUTTON(sensor_id)

    def set_when_deactivated(self, fun):
        self.sensor.when_deactivated = fun