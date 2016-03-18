
# Here we load the libraries needed 
import matplotlib.pyplot as plt 

def plot ( rutine , show_plot=True, prefix = '',name = '', ext='png'):
    """ 
    This routine makes the plots, it receives the plot class
    frecVsTime, or envelope or sonogram and it saves the plots
    """
    axis_x = rutine ["time"]
    axis_y = rutine ["sample"]
    rutine_name = rutine["rutine"]
# We plot the signal frec vs time     
    if rutine_name == "frecVsTime":
        fig , ax = plt.subplots()
        for i in range (len(axis_x)):
            ax.plot(axis_x[i] , axis_y[i])
            ax.set_ylabel('Freq (Hz)')
            ax.set_xlabel('Time (seconds)') 
# We save the plot as .pdf        
            plt.savefig("%ssignal_%s_%03i.%s" % (prefix,name,i,ext) )
            if show_plot == True:
                plt.show()
    elif rutine_name == "envelope":
        fig , ax = plt.subplots()
        for i in range (len(axis_x)):
            ax.plot(axis_x[i] , axis_y[i])
            ax.set_ylabel('Envelope Freq (Hz)')
            ax.set_xlabel('Time (seconds)')

            plt.savefig("%senvelope_%s_%03i.%s" % (prefix,name,i,ext))    
            if show_plot == True:
                plt.show()

    elif rutine_name == "sonogram":
        fig , ax = plt.subplots()
        sample_rate = rutine ["rate"]
        for i in range (len(axis_x)):
            ax.specgram(axis_y[i],Fs=sample_rate)
            ax.set_ylabel(' Frequencies')
            ax.set_xlabel(' Time (seconds)')
# ax.colorbar()
            plt.savefig("%ssonogram_%s_%03i.%s" % (prefix,name,i,ext))
            if show_plot == True:
                plt.show()

    elif rutine_name == "periodogram":
        fig , ax = plt.subplots()
        ax.plot(axis_x , axis_y)
        ax.set_ylabel(' Spectral Density')
        ax.set_xlabel(' Frequency [Hz]')
# ax.colorbar()
        plt.savefig("%speriodogram_%s_.%s" % (prefix,name,ext))
        if show_plot == True:
            plt.show()

    elif rutine_name == "fFourierTransform":
        fig , ax = plt.subplots()
        for i in range (len(axis_x)):
            ax.plot(axis_x[i] , axis_y[i])
            ax.set_ylabel(' Spectral Density')
            ax.set_xlabel(' ')
# ax.colorbar()
            plt.savefig("%sfft_%s_%03i.%s" % (prefix,name,i,ext))
            if show_plot == True:
                plt.show()


