''' Read a wav file and convert it to an array (sample)
 Saves also the sample rate (int)'''
import scipy.io.wavfile as wav
filename_wav = "call1.wav" #Insert the wav filename
(rate,sample) = wav.read(filename_wav) 

