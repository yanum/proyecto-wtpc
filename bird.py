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
        self.time= np.arange(self.sample.size)*(1./self.rate) # X axis , time
        
    def mp3_to_wav(self)
        pass

    def set_envelope(self):
        pass

    def set_sonogram(self):
        
    sound_info, frame_rate = get_wav_info(self.wav)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % self.bird_name)
    pylab.specgram(sound_info, Fs=self.rate)
    pylab.ylabel('Freq (Hz)')
    pylab.xlabel('Time (seconds)')
    pylab.savefig('spectrogram.png')


def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    wav.close()
    return sound_info
        
        
        

        
    
    def set_timeserie(self):
        pass


    def frec_vs_time(self): 
	
   	 fig=plot(self.time,self.sample,label='Time Signal')  # PLot frecuency vr time

   	 grid(True)
   	 pylab.xlabel("time [s]") # Label of axis x
   	 pylab.ylabel("Amplitde") # Label or axis y
	 return fig