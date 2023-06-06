import speech_recognition as sr

# 初始化语音识别器
r = sr.Recognizer()

# 读取麦克风输入
with sr.Microphone() as source:
    print("请说话...")
    audio = r.listen(source)

# 使用文本转语音库将文本转换为语音
from speech_recognition import speech_recognition as sr

# 初始化语音转文字库
r = sr.Recognizer()

# 读取麦克风输入
with sr.Microphone() as source:
    print("请说话...")
    audio = r.listen(source)

# 将文本转换为语音
text_to_speech = sr.Technician(lang='en-US')
text_to_speech.add_text_audio(audio_file='output.wav', lang='en-US')
text_to_speech.run_check()

# 播放语音
play_audio(audio_file='output.wav')
