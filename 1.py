import wave
import numpy as np

#Cargar  archivo wav en la variable 
GM = wave.open('good-morningMan.wav', 'r')

frames = GM.readframes(-1)


#Convierte el audio good morning de bytes a enteros
ondaconvertida = np.frombuffer(frames, dtype='int16')

print(ondaconvertida[:10])