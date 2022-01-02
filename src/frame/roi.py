class ROI:
    def __init__(self, x0, y0, height, width):
        self.x0 = x0
        self.y0 = y0
        self.height = height
        self.width = width
    
    def to_array(self, image):
        return image[self.y0:self.y0 + self.height, self.x0:self.x0 + self.width, : ]
