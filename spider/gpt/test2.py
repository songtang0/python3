from nltk.audio.audioio import AudioIO
from nltk.corpus import stopwords
import numpy as np
import speech_recognition as sr

# 初始化语音识别器
r = sr.Recognizer()
with sr.Microphone() as source:
    print("请说话...")
    audio = r.listen(source)

# 将文本转换为语音
def translate_to_audio(text):
    # 去除停用词
    stop_words = set(stopwords.words(text.lower()))
    text = text.replace(" ", "").lower()
    # 将文本转换为拼音
    phones = nltk.phonetic. pronounce(text)
    # 将拼音转换为字符串
    phonetic_str = ''.join([p for p in phones if p not in stop_words])
    # 将字符串转换为语音
    audio_file = AudioIO(f"{phonetic_str}.wav")
    audio_file.play()
    audio_file.close()

# 将文本转换为语音
translate_to_audio("Hello, world!")
