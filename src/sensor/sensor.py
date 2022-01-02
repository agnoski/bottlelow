import logging

class Sensor:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def set_when_deactivated(self, fun):
        pass