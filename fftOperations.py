from scipy import signal
'''
Author: lmpizarro
'''
class Periodogram(object):
    '''
    A class to calc periodograms of a signal
    '''
    def calc(self, samples, rate): 
        '''
        calc:
        parameters: samples the data array
        rate: the sample rate
        '''
        self.f, self.Pxx_den = signal.periodogram(samples, rate)
        return self.f, self.Pxx_den

class Crosspower(object):
    '''
    A class to calc crosspower of 2 signals
    '''
    def calc(self, samples, samples2, rate): 
        '''
        calc:
        parameters: samples samples2  the data arrays
        rate: the sample rate, must be the same for the 2 arrays
        '''
        self.f, self.Pxx_den = signal.csd(samples, samples2, rate, nperseg = 1024)
        return self.f, self.Pxx_den


"""
This class calculates Fast Fourier Transform (FFT) for the different windows
samples. Then calculates the average FFT and returns a dictionary with info
containing time, sample (average spectrums), and name of rutine.
"""

import numpy as np

import scipy.fftpack as fft

class fFourierTransform(object):

    def meanFFT(self, windowsSample):
        self.windowsSample = windowsSample

        modtf = []
        # Arbitrary timestep to creat frequency array for future periodogram graphs
        timestep = 0.1

        # This loop goes along each element ("window") in the window sample list
        for window in self.windowsSample:

            # Calculates for each window the FFT, then the module (real) of the FFT
            # Append to the new list "modtf" moduloTransfFourier for each window sample.
            tf = fft.fft(window)
            modtf.append( tf * np.conj(tf) )
            n = len(window) 
            self.freq = np.fft.fftfreq(n, d=timestep)
            moduloTransfFourier = np.array(modtf)
        #Calculates the average periodogram for all the window samples
        reduce_fft = np.mean(moduloTransfFourier,axis = 0)

        #Because the periodogram result is folded (like a mirror), only save n/2 values
        self.modulo_Transf_Fourier_Average_de_Windows = (reduce_fft [:len(reduce_fft) / 2])
        self.freq = self.freq[: len(self.freq)/2]
        self.fft_dict = {"time":self.freq,"sample":self.modulo_Transf_Fourier_Average_de_Windows,"rutine": "fFourierTransform"}
        
        return self.modulo_Transf_Fourier_Average_de_Windows, self.freq

	
def verificar_periodogram():
    import scipy.io.wavfile as wav
    import matplotlib.pyplot as plt
    file_name = "audioFiles/albanella/call1.wav" 
    file_name2 = "audioFiles/albanella/call2.wav" 
    file_name3 = "audioFiles/averlaPiccola/call1.wav" 

    (rate,sample) = wav.read(file_name)
    (rate2,sample2) = wav.read(file_name2)
    (rate3,sample3) = wav.read(file_name3)


    per = Periodogram()

    per.calc( sample, rate)

    plt.plot(per.f, per.Pxx_den)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.show()

    per.calc(sample2, rate2)

    plt.plot(per.f, per.Pxx_den)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.show()

    per.calc(sample3, rate3)

    plt.plot(per.f, per.Pxx_den)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.show()


def verificar_crosspower():
    import scipy.io.wavfile as wav
    import matplotlib.pyplot as plt
    file_name = "audioFiles/albanella/call1.wav" 
    file_name2 = "audioFiles/albanella/call2.wav" 


    (rate,sample) = wav.read(file_name)
    (rate2,sample2) = wav.read(file_name2)
 
    cp = Crosspower()

    cp.calc(sample, sample2, rate)

    plt.plot(cp.f, cp.Pxx_den)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('PSD [V**2/Hz]')
    plt.show()

# Test 
def test_fFourierTransform():
    import matplotlib.pyplot as plt  
    fft_out = fFourierTransform()
    windowSample = np.random.random_sample((6, 600))
    fft_out.meanFFT(windowSample)

    print ""
    print fft_out.fft_dict['time'].shape, fft_out.fft_dict['sample'].shape 
    print ""

    plt.plot(fft_out.fft_dict['time'],fft_out.fft_dict['sample'])
    plt.show()



if __name__ == '__main__':
    verificar_crosspower()



