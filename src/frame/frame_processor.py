from frame.frame import Frame
from neural.neural_netUtils import NeuralNetUtils

class FrameProcessor:
    def __init__(self, neuralNet):
        self.neuralNet = neuralNet

    def process(self, frame):
        roi_array = frame.roi_array()
        pred = self.neuralNet.predict(roi_array)
        frame.levels = NeuralNetUtils.get_levels(pred)
        frame.foam = NeuralNetUtils.get_foam(pred)
        return frame