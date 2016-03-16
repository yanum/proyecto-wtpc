
import matplotlib.pyplot as plt

def plot ( rutine , show_plot=True):
    axis_x = rutine ["time"]
    axis_y = rutine ["sample"]
    rutine_name = rutine["rutine"]
     
    if rutine_name == "frecVsTime":
        fig , ax = plt.subplots()
        for i in range (len(axis_x)):
            ax.plot(axis_x[i] , axis_y[i])
        ax.set_ylabel('Freq (Hz)')
        ax.set_xlabel('Time (seconds)') 
        
        plt.savefig("image.pdf")
        if show_plot == True:
            plt.show()

