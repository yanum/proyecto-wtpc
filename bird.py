
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
        pass
    
    def set_timeserie(self):
        pass

    def frec_vs_time(self): 
	
   	 plot(self.time,self.sample,label='Time Signal')  

   	 grid(True)
   	 pylab.xlabel("time [s]")
   	 pylab.ylabel("Amplitde")

	
   	
