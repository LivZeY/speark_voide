from tensorflow.keras.optimizers import Adam
import numpy as np
import tensorflow.keras as keras
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint
from models import Models
from data_set import myScpdataset
from tf_uitls import getMels
import os
from tensorflow.keras import optimizers

callbacks_list=[
    keras.callbacks.EarlyStopping(
        monitor='accuracy',
        patience=50,
    ),
    keras.callbacks.ModelCheckpoint(
        filepath='speechmfcc_model_checkpoint.h5',
        monitor='val_loss',
        save_best_only=True
    ),
    keras.callbacks.TensorBoard(
        log_dir='speechmfcc_train_log'
    )
]

myscpset1 = myScpdataset(r'./testscp.txt')# 初始化数据集
myscpset = myScpdataset(r'./trainscp.txt')# 初始化数据集
x_train,y_train=getMels(myscpset,4)
x_test,y_test=getMels(myscpset1,4)
model = Models()
batchSize=1
opt = optimizers.Adam(learning_rate=0.0001)
model.compile(loss='categorical_crossentropy', optimizer=opt,metrics=['accuracy'])
model.fit(x=x_train,y=y_train,batch_size=6,epochs=200,validation_data=(x_test, y_test), callbacks=callbacks_list)
model.save('model_tf.h5')#loss: 0.0421 - accuracy: 1.0000 - val_loss: 0.3727 - val_accuracy: 0.9667