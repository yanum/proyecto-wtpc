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
        self.bird_image = bird_dict['imagen_name']   # image filename
        if self.audio == 'mp3':
            mp3_to_wav(self)
        (self.rate,self.sample) = wav.read(self.dir+self.audio)

        self.time = np.arange(len(self.sample))/float(self.rate)
        
        self.__create_windows__(windowDT)


    
    def __create_windows__(self, windowDT):
        ndata = 0
        while self.time[ndata] < windowDT :
            ndata += 1


        totalWindows = len(self.time)/ndata
        self.time = self.time[:totalWindows*ndata]
        self.sample = self.sample[:totalWindows*ndata]

        self.time = self.time.reshape((totalWindows,ndata))
        self.sample = self.sample.reshape((totalWindows,ndata))



    def get_envelope(self, windowTimeLength = 5, ):
        """
        windowTimeLength in seconds
        return the envelope of the sample/s. 
        First take a filter and take the absolut value, 
        next create an array with the maximum value per "time" of all the samples
        then reduce the data number with a factor 'windowLengh'
        and finally return the filtered envelope
        if 'time' is set true, return the mean value (of time) for each data of the filtered envalue
        this method is far to be optimal but try to be redeable
        """
        ndata=0
        while self.time[ndata] < windowTimeLength/self.rate :
            ndata += 1

        totalWindows = len(self.time)/ndata
        
        sample = self.sample[:totalWindows*ndata]
        time = self.time[:totalWindows*ndata]
        
        #taking the absolut value 
        absSignal = np.fabs(sample)
        maximumSignal = np.maximum(absSignal)

        envelope = maximumSignal.resharp((totalWindows,ndata))
        envelopeTime = time.resharp((totalWindows,ndata))

        return envelopeTime, envelope, 'envelope'

    def set_sonogram(self):
        pass
    
    def set_timeserie(self):
        pass


