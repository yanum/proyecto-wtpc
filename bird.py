import numpy as np
import scipy.io.wavfile as wav
import mp3ToWav
import aux_functions as aux

import fFourierTransform as fft

class Bird(object):
    """
    Modulo de objeto de pajaro.
    Aqui se obtienen las propiedades del canto
    """
    def __init__(self, bird_dict, windowDT=1):
        print "="*80
        self.dir = bird_dict['path']            # absolute path of dir
        self.audio = bird_dict['filename']        # wav filename
        self.bird_name = bird_dict['especie']   # directory name
        self.bird_image = bird_dict['image_name']   # image filename
        self.time = []
        self.sample = []
        self.windowsTime = []
        self.windowsSample = []
        self.is_working = False                 
        self.frecVsTime={} #empty dictionary 
        self.envelope = {}
        self.sonogram = {}
        self.fft = {}
        """
        Read audio files (.mp3 or .wav) 
        If audio file is a .mp3 it converts it to .wav format
        Returns a wav file: outWavFile 
        """
        mtow = mp3ToWav.Mp3ToWav()
        outWavFile = mtow.convert(self.audio,self.dir)
        try: 
            # Read a wav file and return the rate & sample as numpy.array
            (self.rate,self.sample) = wav.read(outWavFile)
            # create and array of time from knowing the frequency rate and the
            # number of data of the sample
            self.time = np.arange(len(self.sample))/float(self.rate)
            # divide the sample & time arrays in windows of timeSize = windowDT
            self.is_working = True
            self.__create_windows__(windowDT)
        except TypeError:
            print 'Error in convertion of {}/{}'.format(self.bird_name,self.audio)
            self.is_working =  False
        except:
            print "i dont know how to handle this !!"
            self.is_working = False
       
    
    def __create_windows__(self, windowDT):
        """
        __create_windows__ a private method to create windows for
        processing the signal
        divide the sample & time arrays in windows of timeSize = windowDT
        doesn't delete the sample & time arrays
        """
        
        if self.time[-1] > windowDT:
            ndata = 0
            while self.time[ndata] < windowDT :
                ndata += 1

        else:
            # if the windowDT is bigger than the max time of the sample
            print 'changing windows size to {}'.format(self.time[-1])
            ndata = len(self.time)

        totalWindows = len(self.time)/ndata
        self.windowsTime = self.time[:totalWindows*ndata]
        self.windowsSample = self.sample[:totalWindows*ndata]

        # the total data inside windowed arrays is <= than the 'real one'
        # this 'cause we dont want to handle with different sizes of windows
        # (thinking in the end of data that don't fill the last window
        try:
            self.windowsTime = self.windowsTime.reshape((totalWindows,ndata))
            self.windowsSample = self.windowsSample.reshape((totalWindows,ndata))
        except ValueError:
            print "Cant handle the resharp if windowDT is bigger than \
max time of the sample {}/{}".format(self.bird_name,self.audio)
            self.is_working = False
        # not sure if this can happend
        #if self.windowsTime.ndim is not 2:
        #    raise Exception("the dimension of the windowed arrays should be 2")
        if self.windowsSample.ndim is not 2:
            print "windowsSample.ndim is not 2"
            self.is_working = False
        if self.windowsTime.ndim is not 2:
            print "windowsTime.ndim is not 2"
            self.is_working = False


    def get_envelope(self, windowSize = 25 ):
        envelope = aux.envelope(self.windowsSample, windowSize)
        envelopeTime = aux.meanFilter(self.windowsTime, windowSize)
        self.envelope = {'time':envelopeTime,'sample':envelope,'rutine':'envelope'}
        return self.envelope

    def get_sonogram(self):
        self.sonogram = {'time': self.windowsTime, 'sample': self.windowsSample,
                        'rate':self.rate, "rutine":'sonogram'}
        return self.sonogram
    
    def get_frecVsTime(self): 
        # dictionary with info for plotting 
        self.frecVsTime= {"time":self.windowsTime, "sample": self.windowsSample,
        "rutine": "frecVsTime"}
        return self.frecVsTime

    def get_fft(self):
        sampleFFT = fft.fFourierTransform()
        sampleFFT.meanFFT(self.windowsSample)
        self.fft = sampleFFT.fft_dict
        return self.fft
       
