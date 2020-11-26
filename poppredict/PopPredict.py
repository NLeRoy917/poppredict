import tensorflow as tf
import numpy as np

class PopPredict():
    """
    PopPredict class - superclass of the keras sequential Model

    """
    def __init__(self):
        
        self._model = tf.keras.models.Sequential()

        # create input layer that has size=12 for the 12 audio features
        # add a hidden later
        self._model.add(tf.keras.Input(shape=(12,)))
        self._model.add(tf.keras.layers.Dense(12, activation='relu'))
        self._model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    
    def compile(self, loss='mse', optimizer='adam', metrics=['accuracy']):
        self._model.compile(optimizer=optimizer, loss=loss, metrics=['metrics'])

    
    def summary(self):
        self._model.summary()
