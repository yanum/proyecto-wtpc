""" This routine makes the plots, it receives the plot class
    frecVsTime, or envelope or sonogram and it saves the plots
"""

# Here we load the libraries needed 
import matplotlib.pyplot as plt 

def plot ( rutine , show_plot=True):
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
        plt.savefig("signal_vs_time.pdf")
        if show_plot == True:
            plt.show()
    elif rutine_name == "envelope":
        fig , ax = plt.subplots()
        for i in range (len(axis_x)):
            ax.plot(axis_x[i] , axis_y[i])
        ax.set_ylabel('Envelope Freq (Hz)')
        ax.set_xlabel('Time (seconds)')
        
        plt.savefig("envelope_of_signal.pdf")    
        if show_plot == True:
            plt.show()
            
    else if rutine_name == "sonogram":
        fig , ax = plt.subplots()
        sample_rate = rutine ["rate"]
        for i in range (len(axis_x)):
            ax.specgram(axis_y[i],Fs=sample_rate)
            ax.set_ylabel(' Frequencies')
            ax.set_xlabel(' Time (seconds)')
            ax.colorbar()
            plt.savefig("sonogram_{}".format(i))
