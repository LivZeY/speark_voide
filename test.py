from models import Models
from tf_uitls import getMels
from tensorflow.keras.models import load_model
import pyaudio
import wave
import numpy as np

# 录音参数
CHUNK = 1024    
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = ".\speech1.wav"
# 打开录音

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
i = input("按下回车键开机录音，录音5秒中：")
print("开始录音......")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("录音已结束!")
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
print("正在识别请稍后...")

model=load_model('model_tf_02.h5')
mels,y=getMels([('./speech.wav',0)],4)
result=model.predict(mels)
# print(result)
maxflags=np.argmax(result, axis=1)[0]
if int(maxflags)==0:
    print("说话人为：id0001")
elif int(maxflags)==1:
    print("说话人为：id0002")
else:
    print("说话人为：id0003")
