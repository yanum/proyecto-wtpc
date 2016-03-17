import sys,traceback
import numpy as np

class DimensionError(Exception):
    """
    the dimension of the input doesnt match with the expected
    """


def envelope(signals,windowSize=25):
    """
    input:
    > signals: set of signal/s 
    > windowSize: number of data in each window

    return:
     > the envelope of the signal/s. 
    First take the absolut value, next create an array with the maximum value 
    per "time" of all the samples then reduce the data number with a factor 
    'windowLengh' and finally return the filtered envelope if 'time' is set
    true, return the mean value (of time) for each data of the filtered envalue
    This method is far to be optimal but try to be redeable

    """
    try:
        if signals.ndim > 2:
            raise DimensionError("The function is expecting a 2 dimensional array\
                [set of signals] or 1 dimensional array")
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                limit=2, file=sys.stdout)
        print "unexpected error"
        sys.exit(1)


    # nSignals: number of signals
    # nWindows: number of full windows in the array
    # rest: number of data that doesnt fill the last window
    # nData: number of data in full windows
    if signals.ndim == 1:
        nSignals = 1
        nWindows = len(signals)/windowSize
        ndim = 1
    else:
        nSignals = len(signals)
        nWindows = len(signals[0])/windowSize
        ndim = 2
    nData = nWindows*windowSize


    #taking the absolut value 
    absSignal = np.fabs(signals)
    # windows: return list of samples. Each sample is splited in nWindows
    #          windows
    # lastWindow: return a list of the last window of each sample
    #             The shape of this array should be (len(self.sample),rest)
    if signals.ndim == 1:
        windows    = np.split(absSignal[:nData],nWindows,axis=0)
        lastWindow = absSignal[nData:]
    else:
        windows    = np.split(absSignal[:,:nData],nWindows,axis=1)
        lastWindow = absSignal[:,nData:]

    # the first line take the maximum value of each window of each sample
    # the next line stack all the maximum values 'as it should be'
    envelope = np.amax(windows,axis=ndim)
    envelope = np.stack(envelope,axis=ndim-1)

    # evaluate the maximum value of the last window of each sample
    # returning a row array. The reshape transform the row array to
    # column array to appending to envelope
    try:
        if signals.ndim == 1:
            lastData = np.amax(lastWindow)
            envelope = np.append(envelope,lastData)
        else:
            lastData = np.amax(lastWindow, axis=1).reshape(nSignals,1)
            envelope = np.append(envelope,lastData,axis=1)
    except ValueError:
        #lastData is empty list. numpy cant do anything with this, so we
        #ignore it
        pass

    return envelope


def meanFilter(signals,windowSize=25):
    """
    input:
    > signals: set of signal/s 
    > windowSize: number of data in each window

    return:
     > an array with the mean value of each window of each signal. 
    First take the absolut value, next create an array with the maximum value 
    per "time" of all the samples then reduce the data number with a factor 
    'windowLengh' and finally return the filtered envelope if 'time' is set
    true, return the mean value (of time) for each data of the filtered envalue
    This method is far to be optimal but try to be redeable

    """
    try:
        if signals.ndim > 2:
            raise DimensionError("The function is expecting a 2 dimensional array\
                [set of signals] or 1 dimensional array")
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                limit=2, file=sys.stdout)
        print "unexpected error"
        sys.exit(1)


    # nSignals: number of signals
    # nWindows: number of full windows in the array
    # rest: number of data that doesnt fill the last window
    # nData: number of data in full windows
    if signals.ndim == 1:
        nSignals = 1
        nWindows = len(signals)/windowSize
        ndim = 1
    else:
        nSignals = len(signals)
        nWindows = len(signals[0])/windowSize
        ndim = 2
    nData = nWindows*windowSize


    # windows: return list of samples. Each sample is splited in nWindows
    #          windows
    # lastWindow: return a list of the last window of each sample
    #             The shape of this array should be (len(self.sample),rest)
    if signals.ndim == 1:
        windows    = np.split(signals[:nData],nWindows,axis=0)
        lastWindow = signals[nData:]
    else:
        windows    = np.split(signals[:,:nData],nWindows,axis=1)
        lastWindow = signals[:,nData:]

    # the first line take the maximum value of each window of each sample
    # the next line stack all the maximum values 'as it should be'
    filteredSignal = np.mean(windows,axis=ndim)
    filteredSignal = np.stack(filteredSignal,axis=ndim-1)

    # evaluate the maximum value of the last window of each sample
    # returning a row array. The reshape transform the row array to
    # column array to appending to filteredSignal
    try:
        if signals.ndim == 1:
            lastData = np.amax(lastWindow)
            filteredSignal = np.append(filteredSignal,lastData)
        else:
            lastData = np.amax(lastWindow, axis=1).reshape(nSignals,1)
            filteredSignal = np.append(filteredSignal,lastData,axis=1)
    except ValueError:
        #lastData is empty list. numpy cant do anything with this, so we
        #ignore it
        pass

    return filteredSignal



if __name__ == '__main__':
    
    signals = np.random.random_sample((6,666))
    print signals.ndim
    print envelopeSignals(signals).shape
    print ""
    signal = np.copy(signals[0])
    print envelopeSignal(signal).shape
    BIGsignal = np.random.random_sample((2,6,666))

    
    print signal.shape
    print signals[0,:].shape
    print ""
    print envelope(signal) == envelope(signals)
    print ""
    print envelope(signals[0,:])
