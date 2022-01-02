import logging

class VideoStream:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self):
        pass

    def read(self):
        pass