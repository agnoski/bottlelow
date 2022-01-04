from frame.frame import Frame
from neural.neural_netUtils import NeuralNetUtils

class FrameProcessor:
    def __init__(self, neuralNet, roi):
        self.neuralNet = neuralNet
        self.roi = roi

    def process(self, image):
        frame = Frame(image, self.roi, {})
        roi_array = frame.roi_array()
        pred = self.neuralNet.predict(roi_array)
        frame.levels = NeuralNetUtils.get_levels(pred)
        frame.foam = NeuralNetUtils.get_foam(pred)