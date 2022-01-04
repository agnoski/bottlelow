from tensorflow.keras.models import load_model
import cv2
from cv2 import cvtColor
import numpy as np

class NeuralNet:
    def __init__(self, model_path:str):
        self.path_dir = 'weights'
        self.model = load_model(model_path)

    def set_model(self, model_path):
        self.model = load_model(model_path)

    def __preprocess(self, frame):
        frame = cvtColor(frame, cv2.COLOR_BGR2GRAY) #RGB2GRAY=6 ; BGR2GRAY=7
        frame = np.expand_dims(frame/255.0, axis=0)
        frame = np.expand_dims(frame, axis=3)
        return frame
    
    def predict(self, arr):
        arr = self.__preprocess(arr)
        return self.model.predict(arr)

    '''
    def set_train_callback(self, callback):
        self.train_callbacks = [FitCallback(callback)]

    def train(self, frame_lists:FrameList) -> str:
        trainer = Trainer()
        trainer.set_data(frame_lists)
        trainer.train(self.train_callbacks)
        model_name = 'weight_test.h5'
        path = trainer.save(model_name)
        self.set_model(path)
    '''