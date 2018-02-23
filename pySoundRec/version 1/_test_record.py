import pyaudio
import wave
import datetime

global DEBUG
global audio
global n_records

DEBUG = True
audio = 0
 
def start():
    global audio
    audio = pyaudio.PyAudio()
    
def stop():
    global audio
    assert(str(type(audio)) == "<class 'pyaudio.PyAudio'>")
    audio.terminate()
    
def getInfo():
    global audio
    assert(str(type(audio)) == "<class 'pyaudio.PyAudio'>")
    return audio.get_default_input_device_info()
    
start()
i = getInfo()
stop()
    
FORMAT = pyaudio.paInt32
CHANNELS = int(i['maxInputChannels'])
RATE = int(i['defaultSampleRate'])
CHUNK = 1024
    
def record(timerecord, name):
    assert(type(timerecord) is int)
    assert(timerecord > 0)
    
    global audio
    global FORMAT
    global CHANNELS
    global RATE
    global CHUNK
    
    stream = audio.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    print("* recording")
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * timerecord)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    
    wf = wave.open(name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
if __name__ == "__main__":
    start()
    getInfo()
    record(5, "file.wav")
    stop()