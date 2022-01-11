from core.hardware.video_stream.video_stream import VideoStream
from PIL import Image

import numpy as np
import os, os.path

class VideoStreamSimulator(VideoStream):
    def __init__(self, path):
        super().__init__()
        self.images = []
        self.current_image_idx = -1
        self.images_folder_path = path

        # load images from folder and set current index to 0
        self._load_images()
        if len(self.images) > 0:
            self.current_image_idx = 0

    def _get_next_image(self):
        if len(self.images) > 0:
            self.current_image_idx = self.current_image_idx % len(self.images)
            image = self.images[self.current_image_idx]
            self.current_image_idx += 1
            return image
        else:
            #empty image
            return None

    def _load_images(self):
        path = self.images_folder_path
        for f in os.listdir(path):
            extension = os.path.splitext(f)[1]
            if self._is_valid_extension(extension):
                image = np.array(Image.open(os.path.join(path, f)))
                self.images.append(image)
        self.logger.info(f"Loaded {len(self.images)} images")

    def _is_valid_extension(self, extension):
        valid_extensions = [".jpg", ".png"]
        return extension.lower() in valid_extensions

    def read(self):
        self.logger.debug("New image")
        image = self._get_next_image()
        return image