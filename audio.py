import pyaudio
import wave

# 录音参数
CHUNK = 1024    
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 1.5
OUTPUT_FILENAME = ''#"./voxceleb1_part_data/"cl
WAVE_OUTPUT_FILENAME='./'
# 打开录音
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
'''
录入id0001,id0002,id0003说话者的音频文件
其中每个说话者训练集和说话集分别为30语音
'''
for k in range(0,7):
    print("第"+str(k%3+1)+"个说话人")
    # if k<4:
    #     WAVE_OUTPUT_FILENAME=OUTPUT_FILENAME+'test/'
    # else:
    #     WAVE_OUTPUT_FILENAME=OUTPUT_FILENAME+'train/'
    for j in range(1,31):
        i = input("按下回车键开机录音，录音3秒中：")
        print("开始录音......")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("录音已结束!")
        if j<10:
            wf = wave.open(WAVE_OUTPUT_FILENAME+'id000'+str(k%3+1)+'/'+str(j)+'.wav', 'wb')
        else:
            wf = wave.open(WAVE_OUTPUT_FILENAME+'id000'+str(k%3+1)+'/'+str(j)+'.wav', 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
