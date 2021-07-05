from tensorflow.keras import layers
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.models import Sequential

import tensorflow as tf
def Models():
    model = Sequential()
    # model.add(layers.PReLU())
    model.add(Dense(256, input_shape=(None,16128),activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(256,activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(256,activation='relu'))
    model.add(Dropout(0.5))

    # model.add(Dense(128,activation='relu'))
    # model.add(Dropout(0.5))

    # model.add(Dense(64,activation='relu'))
    # model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax'))
    model.summary()
    return model
