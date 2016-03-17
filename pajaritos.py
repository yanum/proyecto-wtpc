import argparse
import discover_files as DF
import sys
import bird as bd



'''
This is a program to process some audio files

'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some audio files.')

    parser.add_argument('-r', action='store', dest='audio_folder',   
                    help='the audio files folder')

    args = parser.parse_args()


    if args.audio_folder != None:
        print args.audio_folder
        audio_files = DF.Discover_Files(args.audio_folder)
        audio_files.get_paths()
    else:
        print "Give me a folder, please!"
        sys.exit(1)

    import matplotlib.pyplot as plt
   
    for dict in audio_files.file_list:
        pajarito = bd.Bird(dict, windowDT= 3 )
        if pajarito.is_working:
            print pajarito.bird_name, pajarito.audio
            env = pajarito.get_envelope()
            
            fft = pajarito.get_fft()
            periodogram = pajarito.get_periodogram()
            frecvstime = pajarito.get_frecVsTime()
            plt.plot(periodogram['time'],periodogram['sample'])
            plt.show()


