import numpy as np
import wave
from scipy.io.wavfile import read,write

def load_wav_file(filename):
    sampleFrequency, inputSequence = read(filename)
    return sampleFrequency, inputSequence
def write_wav_file(filename, rate, data):
    write(filename=filename, rate=rate, data=data)
