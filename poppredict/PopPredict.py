import tensorflow as tf
import numpy as np

class PopPredict():
    """
    PopPredict class - superclass of the keras sequential Model

    """
    def __init__(self, path=None):
        if path:
            self._model = tf.keras.models.load_model(path, compile=True)
        else:
            # create input layer that has size=12 for the 12 audio features
            # add a hidden later
            self._model = tf.keras.models.Sequential()
            self._model.add(tf.keras.Input(shape=(12,)))
            self._model.add(tf.keras.layers.Dense(12, activation='relu'))
            self._model.add(tf.keras.layers.Dense(1))
    
    def compile(self, loss='mse', optimizer='adam', metrics=['accuracy']):
        self._model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
    
    def fit(self, x, y, **kwargs):
        """
        Fit (or train) the neural network to the data
        :param x: the inputs to the model
        :param y: the model outputs
        """
        self._model.fit(x, y, **kwargs)
    
    def save(self, path):
        """
        Save a model after training
        """
        self._model.save(path)
    
    def evaluate(self, x, y, **kwargs):
        """
        Validate, test, or evaluate the model
        :param x: the inputs to validate
        :param y: the outputs to validate
        """
        loss, accuracy = self._model.evaluate(x,y)
        return loss, accuracy
    
    def predict(self, inputs, **kwargs):
        """
        Make a prediction with the model
        :param inputs: The inputs to the model
        """
        prediction = self._model.predict(inputs)
        return prediction

    def summary(self):
        self._model.summary()
