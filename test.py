#!/bin/python2
import bird 
import matplotlib.pyplot as plt
dic = {'path': './audioFiles/albanella/','filename':'call2.wav','especie':'albanella','image_name':'albanellaM.jpg'}

pajaro = bird.Bird(dic,1)

#print pajaro.time
#print pajaro.sample

envelopeTime,envelope,name = pajaro.get_envelope(23)

print pajaro.time.shape, pajaro.sample.shape
print envelope.shape, envelopeTime.shape


for i in range(len(pajaro.time)):
    plt.plot( envelopeTime[i], envelope[i])
    plt.plot( pajaro.time[i], pajaro.sample[i])
#plt.plot(envelopeTime,envelope)
plt.show()
