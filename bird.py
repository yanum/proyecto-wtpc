
import numpy as np

class Bird(object):
    """
    Modulo de objeto de pajaro.
    Aqui se obtienen las propiedades del canto
    """
    def __init__(self, bird_dict):
        self.wav = bird_dict['path']            # absolute path of wav file
        self.bird_name = bird_dict['especie']   # directory name
        self.bird_image = bird_dict['imagen']   # image path
        


    def set_envelope(self):
        pass

    def set_sonogram(self):
        pass
    
    def set_timeserie(self):
        pass


