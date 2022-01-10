class ROI:
    def __init__(self, roi):
        self.x0 = roi["x0"]
        self.y0 = roi["y0"]
        self.height = roi["height"]
        self.width = roi["width"]

    def to_array(self, image):
        return image[self.y0:self.y0 + self.height, self.x0:self.x0 + self.width, : ]
