
"""

This class calculates Fast Fourier Transform (FFT) for the different windows
samples. Then calculates the average FFT and returns a dictionary with info
containing time, sample (average spectrums), and name of rutine.
"""

import numpy as np

from scipy.fftpack as fft

class fFourierTransform(object):

    def fFourierTransform(self, windowSample):
        self.windowSample = windowSample
        self.windowTimeSample = windowTimeSample

	modtf = []

        for window in self.windowSample:
            tf = fft(window)
            modtf.append( tf * np.conj(tf) )
	self.moduloTransfFourier = np.array(modtf)
        self.modulo_Transf_Fourier_Average_de_Windows = 

        return self.modulo_Transf_Fourier_Average_de_Windows self.moduloTransfFourier

    def fft(self): 
	
        self.fft = {"time":self.windowTimeSample,"sample":self.sample,"routine": "fFourierTransform")
        return self.fFT


# Test 
"""def test():
    path = './audioFiles/albanella/'
    filename = 'call1.wav'
    fft_out = fFourierTransform()
    fft_out.fFourierTransform(windowSample,path)


if __name__ == '__main__':
    test()

"""
