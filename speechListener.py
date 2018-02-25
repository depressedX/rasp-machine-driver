# coding:utf-8

import sounddevice as sd
from scipy.io import wavfile
from aip import AipSpeech

# 你的 APPID AK SK
APP_ID = '10852445'
API_KEY = '182GRNeNziPXFTB19MivWkal'
SECRET_KEY = 'VpD9biDAKMWReNvfnOkyXgfuyzdaSLVb'


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def recorder(length, fs=16000):
    recording = sd.rec(frames=fs * length, samplerate=fs, blocking=True, channels=1)
    return recording


client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
asr = client.asr(get_file_content('test.wav'), 'wav', 16000, {
    'lan': 'en',
})
print(asr)
