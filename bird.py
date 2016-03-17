import numpy as np

import scipy.io.wavfile as wav
import mp3ToWav

import aux-functions as aux-f
class Bird(object):
    """
    Modulo de objeto de pajaro.
    Aqui se obtienen las propiedades del canto
    """
    def __init__(self, bird_dict, windowDT=1):
        self.dir = bird_dict['path']            # absolute path of dir
        self.audio = bird_dict['filename']        # wav filename
        self.bird_name = bird_dict['especie']   # directory name
        self.bird_image = bird_dict['image_name']   # image filename

        """
        Read audio files (.mp3 or .wav) 
        If audio file is a .mp3 it converts it to .wav format
        Returns a wav file: outWavFile 
        """
        mtow = mp3ToWav.Mp3ToWav()
        outWavFile = mtow.convert(self.audio,self.dir)

        """
        Read a wav file and convert it to an array (sample)
        Saves also the sample rate (int)'''
        """
        try:
            (self.rate,self.sample) = wav.read(outWavFile)
            self.time = np.arange(len(self.sample))/float(self.rate)
        
            self.__create_windows__(windowDT)
        except:
            pass



    
    def __create_windows__(self, windowDT):
        if self.time[-1] > windowDT:
            ndata = 0
            while self.time[ndata] < windowDT :
                ndata += 1

        else:
            print 'changing windows size to {}'.format(self.time[-1])
            ndata = len(self.time)


        totalWindows = len(self.time)/ndata
        self.time = self.time[:totalWindows*ndata]
        self.sample = self.sample[:totalWindows*ndata]

        self.time = self.time.reshape((totalWindows,ndata))
        self.sample = self.sample.reshape((totalWindows,ndata))



    def get_envelope(self, windowSize = 25 ):
        envelope = aux-f.envelope(self.windowSample, windowSize)
        envelopeTime = aux-f.meanFilter(self.windowsTime, windowSize)
        self.envelope = {'time':envelopeTime,'sample':envelope,'rutine':'envelope'}
        return self.envelope

    def set_sonogram(self):
        pass
    
    def set_timeserie(self):
        pass

