
import numpy as np
import scipy.io.wavefile as wav

class Bird(object):
    """
    Modulo de objeto de pajaro.
    Aqui se obtienen las propiedades del canto
    """
    def __init__(self, bird_dict):
        self.dir = bird_dict['path']            # absolute path of dir
    	self.wav = bird_dict['filename']        # wav filename
        self.bird_name = bird_dict['especie']   # directory name
        self.bird_image = bird_dict['imagen_name']   # image filename
	    if self.wav == 'mp3':
            mp3_to_wav(self)
        (self.rate,self.sample) = wav.read(self.dir+self.wav)

    def mp3_to_wav(self)
        pass

    def get_envelope(self, windowLength = 50, time=False, lowPassFilter=False, plot=False):
        """
        return the envelope of the sample/s. 
        First take a filter and take the absolut value, 
        next create an array with the maximum value per "time" of all the samples
        then reduce the data number with a factor 'windowLengh'
        and finally return the filtered envelope
        if 'time' is set true, return the mean value (of time) for each data of the filtered envalue
        this method is far to be optimal but try to be redeable
        """
        #filtering the signal (maybe this should be another method)
        filteredSignal = self.sample
        if lowPassFilter:
            pass
        #taking the absolut value 
        absSignal = np.fabs(filteredSignal)
        maximumSignal = np.maximum(absSignal)
        envelope = np.array([ np.amax(maximumSignal[w:w+windowLenght])\
                for w in range(maximumSignal.shape/windowLength)])

        if time:
            pass
#           envelopeTime = np.array([np.mean(self.time[w:w+windowLength]\
#                       for w in range(maximumSignal.shape/windowLength)])
        else:
            envelopeTime = np.array([i in range(envelope.shape)])

        if plot:
            # if plot then return plot object (not sure if this could be done)
            pass

        return envelopeTime, envelope, 'envelope'


    def set_sonogram(self):
        pass
    
    def set_timeserie(self):
        pass


