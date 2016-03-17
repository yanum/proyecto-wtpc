import matplotlib.pyplot as plt

from scipy import signal


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


def verificar():
    import scipy.io.wavfile as wav
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


if __name__ == '__main__':
    verificar()



