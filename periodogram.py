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



if __name__ == '__main__':
    verificar_crosspower()



