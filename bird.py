import numpy as np

import scipy.io.wavfile as wav
import mp3ToWav

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
        self.time = []
        self.sample = []
        self.windowsTime = []
        self.windowsSample = []
        self.is_working = False                 
        
        
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
            self.__create_windows__(windowDT)
            self.is_working = True
        except TypeError:
            print 'error en conversion'
            self.is_working =  False

        
    
    def __create_windows__(self, windowDT):
        """
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
        self.windowsTime = self.time.reshape((totalWindows,ndata))
        self.windowsSample = self.sample.reshape((totalWindows,ndata))

        # not sure if this can happend
        if self.windowsTime.ndim is not 2:
            raise Exception("the dimension of the windowed arrays should be 2")



    def get_envelope(self, windowSize = 25 ):
        """
        return the envelope of the sample/s. 
        First take a filter and take the absolut value, next create an array 
        with the maximum value per "time" of all the samples then reduce the 
        data number with a factor 'windowLengh' and finally return the filtered
        envelope if 'time' is set true, return the mean value (of time) for
        each data of the filtered envalue
        This method is far to be optimal but try to be redeable

        windowSize: number of data in each window
        """
        # nWindows: number of full windows in the array
        # rest: number of data that doesnt fill the last window
        # nData: number of data in full windows
        nWindows = len(self.windowsTime[0])/windowSize
        rest  = len(self.windowsTime[0]) % windowSize
        nData = nWindows*windowSize


        #taking the absolut value 
        absSignal = np.fabs(self.sample)
        # windows: return list of samples. Each sample is splited in nWindows
        #          windows
        # lastWindow: return a list of the last window of each sample
        #             The shape of this array should be (len(self.sample),rest)
        windows    = np.split(absSignal[:,:nData],nWindows,axis=1)
        lastWindow = absSignal[:,nData:]
        windowsTime    = np.split(self.windowsTime[:,:nData],nWindows,axis=1)
        lastWindowTime = self.windowsTime[:,nData:]

        # the first line take the maximum value of each window of each sample
        # the next line stack all the maximum values 'as it should be'
        envelope = np.amax(windows,axis=2)
        envelope = np.stack(envelope,axis=1)
        # in the case of the time we take the mean value of each window
        envelopeTime = np.mean(windowsTime,axis=2)
        envelopeTime = np.stack(envelopeTime,axis=1)

        # evaluate the maximum value of the last window of each sample
        # returning a row array. The reshape transform the row array to
        # column array to appending to envelope
        try:
            lastData = np.amax(lastWindow, axis=1).reshape(len(self.sample),1)
            lastDataTime = np.mean(lastWindowTime,axis=1).reshape(len(self.windowsTime),1)
            envelope = np.append(envelope,lastData,axis=1)
            envelopeTime = np.append(envelopeTime,lastDataTime,axis=1)
        except ValueError:
            #lastData is empty list. numpy cant do anything with this, so we
            #ignore it
            pass

        return envelopeTime, envelope, 'envelope'

    def set_sonogram(self):
        pass
    
    def set_timeserie(self):
        pass

