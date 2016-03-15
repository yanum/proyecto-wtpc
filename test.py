import bird 

dic = {'path': './albanella/','filename':'call2.wav','especie':'albanella','imagen_name':'albanellaM.jpg'}

pajaro = bird.Bird(dic,1)

print pajaro.time
print pajaro.sample

envelope = pajaro.get_envelope()

print envelope
