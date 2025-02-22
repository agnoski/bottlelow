class Frame:
    def __init__(self, image, roi, limits, metadata={}, filepath=""):
        self.image = image
        self.roi = roi
        self.limits = limits
        self.metadata = metadata
        self.filepath = filepath
        self.levels = None
        self.foam = None

    def roi_array(self):
        return self.roi.to_array(self.image)