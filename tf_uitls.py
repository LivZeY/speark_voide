import os
import librosa
import numpy as np
from keras.utils import to_categorical

def getMels(myscpset,timelen=4):
    mels = [] # 存储 K个 mel谱 的列表
    y_label=[]
    mels=np.array(mels)
    y_label=np.array(y_label)
    x=[]
    y=[]
    x1=[]
    y1=[]
    for batch in myscpset:
        wav,label=batch
        x.append(wav)
        y.append(label)
    x=np.array(x)
    y=np.array(y)
    count=0
    for i in range(len(myscpset)):
        waveform,sample_rate = librosa.load(x[i],sr=16000)
        if len(waveform) >= sample_rate * timelen:
            # 此时音频时长满足时间要求，直接截取采样点
            waveform = waveform[0:int(sample_rate * timelen)]
        else:
            # 此时音频时长不满足时间要求，补齐
            waveform = waveform.tolist()
            for j in range(timelen*sample_rate-len(waveform)):
                waveform.append(0)
            waveform=np.array(waveform)
        mel=librosa.feature.melspectrogram(y=waveform, sr=sample_rate)
        # mel谱维度本来是 （ feature size ,frames  ），扩充一维，变成 （1,  feature size ,frames）
        if i==19 or i==39:
            count+=1
        x1.append(mel)
        y1.append(y[i])
    x1=np.array(x1)
    y1=np.array(y1)
    mels=x1.reshape(len(myscpset),-1)
    y_label=to_categorical(y1,3)
    return mels,y_label

if __name__=="__main__":

    pass
