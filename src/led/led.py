import logging

class Led:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def on(self):
        pass

    def off(self):
        pass