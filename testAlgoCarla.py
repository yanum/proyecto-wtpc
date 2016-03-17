import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

from scipy import signal
import scipy.fftpack as fft
import numpy as np
from scipy.fftpack import fft

file_name = "audioFiles/albanella/call1.wav" 
file_name2 = "audioFiles/albanella/call2.wav" 
file_name3 = "audioFiles/averlaPiccola/call1.wav" 

(rate,sample) = wav.read(file_name)
(rate2,sample2) = wav.read(file_name2)
(rate3,sample3) = wav.read(file_name3)


print len(sample)

reduce_fft = np.zeros(6000)
deltaT = 1.0 / float(rate)
tiempoTotal = len(sample) * deltaT
print 'fmax', fmax
for i in range(10):
    tf = fft(sample[i*6000:(i+1)*6000])
    modtf = tf * np.conj(tf)
    reduce_fft =reduce_fft +  modtf

reduce_fft = reduce_fft / 10


plt.plot(reduce_fft[:len(reduce_fft) / 2])
plt.show()
