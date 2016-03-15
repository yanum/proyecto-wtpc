import numpy as np
import scipy.io.wavfile as wav

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
        if self.audio == 'mp3':
            mp3_to_wav(self)
        (self.rate,self.sample) = wav.read(self.dir+self.audio)

        self.time = np.arange(len(self.sample))/float(self.rate)
        
        self.__create_windows__(windowDT)


    
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



    def get_envelope(self, windowTimeLength = 5, ):
        pass

    def set_sonogram(self):
        pass
    
    def set_timeserie(self):
        pass

