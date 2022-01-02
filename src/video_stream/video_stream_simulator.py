import os, os.path
from PIL import Image
import numpy as np
from video_stream.video_stream import VideoStream

class VideoStreamSimulator(VideoStream):
    def __init__(self, path):
        super().__init__()
        self.frames = []
        self.current_frame_idx = -1
        self.frames_folder_path = path

    def _get_next_frame(self):
        if len(self.frames) > 0:
            self.current_frame_idx = self.current_frame_idx % len(self.frames)
            frame = self.frames[self.current_frame_idx]
            self.current_frame_idx += 1
            return frame
        else:
            return None #empty image

    def _load_frames(self):
        path = self.frames_folder_path
        valid_images = [".jpg", ".png"]
        for f in os.listdir(path):
            ext = os.path.splitext(f)[1]
            if ext.lower() not in valid_images:
                continue
            image = np.array(Image.open(os.path.join(path,f)))
            self.frames.append(image)
        self.logger.info(f"Loaded {len(self.frames)} images")

    def start(self):
        # load frame from folder and set current index to 0
        self._load_frames()
        if len(self.frames) > 0:
            self.current_frame_idx = 0

    def read(self):
        self.logger.debug("New frame")
        frame = self._get_next_frame()
        return frame
