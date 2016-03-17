
"""
This class calculates Fast Fourier Transform (FFT) for the different windows
samples. Then calculates the average FFT and returns a dictionary with info
containing time, sample (average spectrums), and name of rutine.
"""

import numpy as np

from scipy.fftpack as fft

class fFourierTransform(object):

    def fFourierTransform(self, windowsSample):
        self.windowsSample = windowsSample

	modtf = []
        # Arbitrary timestep to creat frequency array for future periodogram graphs
        timestep = 0.1

        # This loop goes along each element ("window") in the window sample list
        for window in self.windowsSample:

            # Calculates for each window the FFT, then the module (real) of the FFT
            # Append to the new list "modtf" moduloTransfFourier for each window sample.
            tf = fft(window)
            modtf.append( tf * np.conj(tf) )
            n = len(window) 
            self.freq = np.fft.fftfreq(n, d=timestep)
            moduloTransfFourier = np.array(modtf)
        #Calculates the average periodogram for all the window samples
        reduce_fft = np.mean(moduloTransfFourier,axis = 0)

        #Because the periodogram result is folded (like a mirror), only save n/2 values
        self.modulo_Transf_Fourier_Average_de_Windows = (reduce_fft [:len(reduce_fft) / 2])
        return self.modulo_Transf_Fourier_Average_de_Windows

    def fft(self): 
	
        self.fft = {"time":self.freq,"sample":self.modulo_Transf_Fourier_Average_de_Windows,"routine": "fFourierTransform")
        return self.fFT


# Test 
"""def test():
       fft_out = fFourierTransform()
       fft_out.fFourierTransform(windowSample)


if __name__ == '__main__':
    test()

"""
