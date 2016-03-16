# proyecto-wtpc: Pajaritos

## Análisis sistemático de archivos de audio almacenados en directorios.

# Integrantes del grupo de trabajo

* Adriana
* Carla
* Raúl 
* Yanina
* Luis María





### Objetos:

* Bird:  encapsula los detalles de un canto de un ave
* Discover_Files: determina los archivos tipo sonido presentes
* mp3ToWav : convierte los archivos mp3 (si existen) a wav 


### Módulos

* bird.py
   depende de:
   * numpy: provee biblioteca de cálculo númerico en python
   * scipy: provee biblioteca para procesamiento de señales
   * mp3ToWav: objeto que determina el tipo de archivo y lo
     convierte a wav si es necesario

* discover_files.py  
   depende de:
   * os: provee rutinas de sistema operativo
   * sys: provee acceso a objetos usados o mantenidos por el intérprete y a
     funciones que interactuan fuertemente con el intérprete

  

* main.py  
   depende de:
   * bird: mantiene detalles del canto del ave 
   * sys:


* mp3ToWav.py
   depende de:
   * os:
   * pydub: usado para convertir archivos mp3 a wav


