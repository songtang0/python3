import pyaudio
import speech_recognition as sr
from speech_recognition import AudioBuffer

# 初始化语音识别器
r = sr.Recognizer()

# 读取音频文件
with AudioBuffer(file("input.wav")) as audio:
    audio_str = r.listen(audio)

# 将文本转换为声音
result = r.recognize_google(audio_str)
print("声音转换为:", result)

# 使用 PyAudio 播放声音
import numpy as np
import pyaudio

# 创建 PyAudio 对象
pa = pyaudio.PyAudio()

# 获取默认通道 (主通道)
stream = pa.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    frames_per_buffer=1024,
    input_buffer_size=1024
)

# 读取声音数据
frames = stream.read(1024)

# 将读取的数据转换为 numpy 数组
data = np.frombuffer(frames, np.int16).reshape([-1, 1])

# 使用 scipy.audio.ioaudio 库将 numpy 数组转换为声音文件
import scipy.audio
ioaudio = scipy.audio.ioaudio()
ioaudio.write(data, format='int16', channels=1, rate=44100, frames_per_buffer=1024)

# 关闭 PyAudio 对象和 Stream
stream.close()
pa.quit()