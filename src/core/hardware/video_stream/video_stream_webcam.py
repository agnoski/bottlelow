from core.hardware.video_stream.video_stream import VideoStream
from threading import Lock

import cv2

class WebcamVideoStream(VideoStream):
    def __init__(self, src = 0, width = 320, height = 240):
        super().__init__()
        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        (self.grabbed, self.frame) = self.stream.read()
        while self.grabbed == False:
            (self.grabbed, self.frame) = self.stream.read()
        self.started = False
        self.read_lock = Lock()

    def run(self):
        while self.started:
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self):
        self.read_lock.acquire()
        frame = self.frame.copy()
        self.read_lock.release()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        return frame

    def __exit__(self, exc_type, exc_value, traceback):
        self.stream.release()