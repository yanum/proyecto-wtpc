# USAGE: ./list-sounds [SOUND_DIRECTORY]

# http://pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/

import os
import sys
import re
import time
import subprocess

# input() workaround to support Python 2. Python 3 renamed raw_input() => input().
# Alias input() to raw_input() if raw_input() exists (Python 2).
try:
    input = raw_input
except NameError:
    pass


class Discover_Files(object):

    def __init__(self, root_dir, first_level_dir='./', files_extensions=['mp3', 'wav', 'aif', 'ogg']):
        self.root_dir = root_dir
	self.first_level_dir = first_level_dir
	self.files_extensions = files_extensions
	self.files_directory = self.root_dir 
	self.file_list =[]
	self.counter = 0


    def get_paths(self):
        # Get the absolute path of the movie_directory parameter
        movie_directory = os.path.abspath(self.files_directory)

        # Get a list of files in movie_directory
        try:
            movie_directory_files = os.listdir(movie_directory)
        except:
            print "the folder doesn't exist"
            sys.exit('Bye, bye!!')

        # Traverse through all files
        for filename in movie_directory_files:
            filepath = os.path.join(movie_directory, filename)

            # Check if it's a normal file or directory
            if os.path.isfile(filepath):

                # Check if the file has an extension of typical video files
                for movie_extension in self.files_extensions:
                    # Not a movie file, ignore
                    if not filepath.endswith(movie_extension):
                        continue

                    # We have got a video file! Increment the counter
                    self.counter += 1
              
                    split_fp= filepath.split('/')
                    especie =  split_fp[len(split_fp) - 2]
                    tail =  split_fp[len(split_fp) - 1]
                    folder = ""
                    for s in range(0,len(split_fp) -1):
                       folder += split_fp[s] + '/'
                    listado =  os.listdir(folder)
                    image_name = ''
                    for l in listado:
                        if l.endswith('jpg'):
                           image_name = l
                    '''     
                    if filepath.endswith('mp3'):
                        print "mp3", filepath, folder +  tail.split('.')[0] + '.wav'

                        try:
                            tail =  tail.split('.')[0] + '.wav'
                            AudioSegment.from_mp3(filepath).export(folder + tail , format="wav")
                            os.remove(filepath)
                        except:
                           print "Error de Conversion"
                           tail = "error_conversion"
                    '''
		    self.file_list.append({'path':'{0}'.format(folder),
				           'file_size':os.path.getsize(filepath), 
				           'filename':tail,
                                           'root_dir' :self.root_dir,
                                           'especie': especie,
                                           'image_name': image_name
			                  })

            elif os.path.isdir(filepath):
                # We got a directory, enter into it for further processing
		self.files_directory = filepath
                self.get_paths()

def test():
    DF = Discover_Files("./audioFiles" )
    DF.get_paths()

    print len(DF.file_list)

    for d in DF.file_list:
        print d

if __name__ == '__main__':
    test()

