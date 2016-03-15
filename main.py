import argparse


parser = argparse.ArgumentParser(description='Process some audio files.')

parser.add_argument('-r', action='store', dest='audio_folder',   
                    help='the audio files folder')

args = parser.parse_args()


print(args.audio_folder)



