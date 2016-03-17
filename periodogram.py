import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

from scipy import signal

file_name = "audioFiles/albanella/call1.wav" 
file_name2 = "audioFiles/albanella/call2.wav" 
file_name3 = "audioFiles/averlaPiccola/call1.wav" 

(rate,sample) = wav.read(file_name)
(rate2,sample2) = wav.read(file_name2)
(rate3,sample3) = wav.read(file_name3)

class Periodogram(object):

     def calc(samples, rate): 
         self.f, self.Pxx_den = signal.periodogram(samples, rate)


per = Periodogram(object):

plt.plot(f, Pxx_den)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

f, Pxx_den = signal.periodogram(sample2, rate2)

plt.plot(f, Pxx_den)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

f, Pxx_den = signal.periodogram(sample3, rate3)

plt.plot(f, Pxx_den)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()



