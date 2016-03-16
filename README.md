# proyecto-wtpc: Pajaritos

## Análisis sistemático de archivos de audio almacenados en directorios.


### Objetos:

* Bird:  encapsula los detalles de un canto de un ave
* Discover_Files: determina los archivos tipo sonido presentes
* mp3ToWav : convierte los archivos mp3 (si existen) a wav 


### Módulos

* bird.py
   depende de:
   * numpy
   * scipy
   * mp3ToWav

* discover_files.py  
   depende de:
   * os
   * sys

  

* main.py  
   depende de:
   * bird
   * sys


* mp3ToWav.py
   depende de:
   * os
   * pydub


