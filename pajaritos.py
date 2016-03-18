import argparse
import discover_files as DF
import sys
import bird as bd
import plotting 

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
        pajarito = bd.Bird(dict, windowDT= 5 )
        if pajarito.is_working:
            audioName = pajarito.audio.split('.')[0]
            specie    = pajarito.bird_name
            print pajarito.bird_name, pajarito.audio
            envelope = pajarito.get_envelope(50)
#            raw = pajarito.get_frecVsTime()
#            sonogram = pajarito.get_sonogram()
#            fft = pajarito.get_fft()
            periodogram = pajarito.get_periodogram()
            
            
#            plotting.plot(sonogram, prefix = './plots/sonogram/',
#                    name=specie+'_'+audioName, show_plot=False)
            plotting.plot(envelope, prefix = './plots/envelope/',
                    name=specie+'_'+audioName, show_plot=False)
            plotting.plot(periodogram, prefix = './plots/periodogram/',
                    name=specie+'_'+audioName, show_plot=False)
#            plotting.plot(fft, prefix = './plots/fft_density/',
#                    name=specie+'_'+audioName, show_plot=False)
#            plotting.plot(raw, prefix = './plots/raw/',
#                    name=specie+'_'+audioName, show_plot=False)


