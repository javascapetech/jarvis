import sounddevice as sd
import numpy as np

threshold = 40.0
clapTimes = 0


def detect_clap(indata, frames, time, status):
    global clapTimes
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > threshold:
        print("Clapped")
        clapTimes = clapTimes + 1


def listen_for_claps():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)


def MainClap():
    global clapTimes
    clapTimes = 0
    while True:
        print(clapTimes)
        listen_for_claps()
        if clapTimes >= 2:
            return True
        else:
            pass
