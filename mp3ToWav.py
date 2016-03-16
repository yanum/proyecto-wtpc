"""
This file enters a filename ("filename.format_extension")
If the file is not a .wav it convert it to wav format and returns
the same filename with format extension ".wav"
"""

import os
 
from pydub import AudioSegment

class Mp3ToWav(object):
    def convert(self, filename, path):
        self.filename = filename
        self.path = path

        if self.filename.endswith('mp3'):
            mp3dir = os.path.join(self.path,"mp3/")
            # If it doesn't exit, create a directory path+mp3/ to move .mp3 files 
            if not os.path.isdir(mp3dir):
                os.mkdir(mp3dir)

            decomposition = self.filename.split('.')
            # Saves in filename_base the name of the audio file
            self.filename_base = decomposition[0]  
            
            try:
                # Convert audiofile to .wav
                outfilename = self.path+self.filename_base+".wav"
                AudioSegment.from_mp3(self.path+self.filename).export(outfilename, format="wav") 
                print "Estoy convirtiendo archivos audio mp3 a wav"
                os.rename(self.path+filename, mp3dir+filename)
                return outfilename
            
            # Sometimes files may be corrupted and conversion may not be proceeded. 
            # This exception helps to continue the routine
            except:
                print "Error de Conversion"
                return None

        else:
            print "Es un archivo wav"
            return self.path+self.filename

# Test conversion mp3 to wav
def test1():
    path = './audioFiles/canary/'
    filename = 'XC122552 - Atlantic Canary - Serinus canaria.mp3'
    mtow = Mp3ToWav()
    mtow.convert(filename,path)

# Test corrupted file - exception for conversion
def test2():
    path  = './audioFiles/canary/'
    filename = 'Suara+Burung+Kenari+01.mp3'
    mtow = Mp3ToWav()
    mtow.convert(filename,path)

# Test no conversion needed, it is a wav file
def test3():
    path = './audioFiles/albanella/'
    filename = 'call1.wav'
    mtow = Mp3ToWav()
    mtow.convert(filename,path)


if __name__ == '__main__':
    test1()
    test2()
    test3()

